import ccxt
import pandas as pd
import numpy as np
import time
import ta

# Define your Binance API key, secret, symbols, and time interval
BINANCE_API_KEY = 'veiqd07BuRmMlxy3eeRLLKNyDnFrIphTcqgSM7XTRUCzQWTyqxK4sPtfVZioaVHi'
BINANCE_API_SECRET = 'N4myBDNkkD203gxxpo8NLQgdZxdvzm7N7PpBjBU0DiTtctTLaFQEVev51N4P5R5g'
symbols = [
    'AAVEUSDT', 'ACEUSDT', 'ACHUSDT', 'ADAUSDT', 'AEVOUSDT', 'AGIXUSDT', 'AGLDUSDT', 'AIUSDT', 'ALGOUSDT', 'ALICEUSDT', 'ALPHAUSDT', 'ALTUSDT', 'AMBUSDT', 'ANKRUSDT', 'APEUSDT', 'API3USDT', 'APTUSDT', 'ARBUSDT', 'ARKUSDT', 'ARKMUSDT', 'ARPAUSDT', 'ARUSDT', 'ASTRUSDT', 'ATAUSDT', 'ATOMUSDT', 'AUDIOUSDT', 'AUCTIONUSDT', 'AXLUSDT', 'AVAXUSDT', 'AXSUSDT'
]

# Add more symbols if needed
time_interval = '5m'  # Time interval for fetching candlestick data

# Create a Binance Futures client
exchange = ccxt.binance({
    'apiKey': BINANCE_API_KEY,
    'secret': BINANCE_API_SECRET,
    'enableRateLimit': True,
    'options': {
        'defaultType': 'future',  # Set the default type to futures
    }
})

# Define MACD strategy parameters
short_window = 8
long_window = 17
signal_window = 9

# Track the last order type placed for each symbol
last_order_types = {symbol: None for symbol in symbols}
open_orders = {symbol: None for symbol in symbols}
open_positions = {symbol: None for symbol in symbols}
close_positions = {symbol: None for symbol in symbols}

# Fixed quantity in USDT worth of contracts
fixed_quantity_usdt = 6

# Function to fetch historical data for futures with MACD calculation
def fetch_ohlcv(symbol, timeframe, limit):
    try:
        ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

def calculate_macd(close_prices, short_window=12, long_window=26, signal_window=9):
    short_sma = close_prices.rolling(window=short_window, min_periods=1).mean()
    long_sma = close_prices.rolling(window=long_window, min_periods=1).mean()
    macd_line = short_sma - long_sma
    signal_line = macd_line.rolling(window=signal_window, min_periods=1).mean()
    histogram = macd_line - signal_line
    
    return macd_line, signal_line, histogram

# Function to fetch historical data for BTCUSDT with StochRSI calculation
def fetch_btcusdt_stochrsi(timeframe, limit):
    try:
        # Fetch OHLCV data for BTCUSDT pair
        ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe, limit=limit)
        df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])

        # Calculate StochRSI
        stoch_rsi_indicator = ta.momentum.StochRSIIndicator(df['close'])
        df['stoch_rsi'] = stoch_rsi_indicator.stochrsi()
        df['stoch_rsi_k'] = stoch_rsi_indicator.stochrsi_k()
        df['stoch_rsi_d'] = stoch_rsi_indicator.stochrsi_d()

        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
        df.set_index('timestamp', inplace=True)
        return df
    except Exception as e:
        print(f"Error fetching data for BTCUSDT: {e}")
        return None

# Function to place a market buy order
def place_market_buy_order(symbol, quantity):
    try:
        order = exchange.create_market_buy_order(
            symbol=symbol,
            amount=quantity
        )
        print(f"Market Buy Order placed for {symbol}: {order}")
        last_order_types[symbol] = 'BUY'
        open_positions[symbol] = 'BUY'
        return order
    except Exception as e:
        print(f"Error placing Market Buy Order for {symbol}: {e}")
        open_positions[symbol] = 'ABCD'
        last_order_types[symbol] = 'BUY'
        return None

# Function to place a market sell order
def place_market_sell_order(symbol, quantity):
    try:
        order = exchange.create_market_sell_order(
            symbol=symbol,
            amount=quantity
        )
        print(f"Market Sell Order placed for {symbol}: {order}")
        open_positions[symbol] = 'SELL'
        last_order_types[symbol] = 'SELL'
        return order
    except Exception as e:
        print(f"Error placing Market Sell Order for {symbol}: {e}")
        open_positions[symbol] = 'EFGH'
        last_order_types[symbol] = 'SELL'
        return None

# Function to close long position
def close_long_position(symbol, quantity):
    try:
        order = exchange.create_market_sell_order(
            symbol=symbol,
            amount=quantity
        )
        print(f"Closed Long Position for {symbol}: {order}")
        open_positions[symbol] = 'Bought'
        return order
    except Exception as e:
        print(f"Error closing Long Position for {symbol}: {e}")
        open_positions[symbol] = 'Bought'
        return None

# Function to close short position
def close_short_position(symbol, quantity):
    try:
        order = exchange.create_market_buy_order(
            symbol=symbol,
            amount=quantity
        )
        print(f"Closed Short Position for {symbol}: {order}")
        open_positions[symbol] = 'sold'
        return order
    except Exception as e:
        print(f"Error closing Short Position for {symbol}: {e}")
        open_positions[symbol] = 'sold'
        return None

# Main trading function for futures with MACD strategy
def macd_strategy():
    while True:
        try:
            for symbol in symbols:
                # Fetch historical data for MACD calculation
                macd_data = fetch_ohlcv(symbol, '5m', 100)

                if macd_data is None:
                    continue  # Skip to the next symbol if there's an error fetching MACD data

                # Fetch historical data for StochRSI calculation
                stochrsi_data = fetch_btcusdt_stochrsi('5m', 100)

                if stochrsi_data is None:
                    continue  # Skip to the next symbol if there's an error fetching StochRSI data

                # Check if there's enough data for MACD and StochRSI calculations
                if len(macd_data) < long_window or len(stochrsi_data) < 14:  # StochRSI requires at least 14 periods
                    print(f"Not enough data for {symbol}. Waiting for more data...")
                    continue

                # Fetch the latest candlestick for each symbol
                latest_candle = exchange.fetch_ohlcv(symbol, '5m', limit=1)
                latest_open = latest_candle[0][1]

                # Calculate the quantity based on the fixed USDT value
                quantity = fixed_quantity_usdt / float(latest_open)

                # Calculate MACD
                macd_line, signal_line, histogram = calculate_macd(macd_data['close'])

                # Calculate StochRSI
                stoch_rsi_k = stochrsi_data['stoch_rsi_k']
                stoch_rsi_d = stochrsi_data['stoch_rsi_d']

                # Print MACD and StochRSI values
                print(f"MACD Line for {symbol}: {macd_line.iloc[-2]}")
                print(f"Signal Line for {symbol}: {signal_line.iloc[-2]}")
                print(f"Histogram for {symbol}: {histogram.iloc[-2]}")
                print(f"StochRSI K: {stoch_rsi_k.iloc[-2]}")
                print(f"StochRSI D: {stoch_rsi_d.iloc[-2]}")

                # Make trading decisions for each symbol
                if (
                    histogram.iloc[-2] >= histogram.iloc[-3] and
                    histogram.iloc[-3] <= histogram.iloc[-4] and
                    stoch_rsi_k.iloc[-2] <= 0.4 and
                    last_order_types[symbol] != 'BUY'
                ):
                    print(f'{symbol} Buy Signal (Short EMA cross over Open)')
                    # Implement your buy logic here for futures
                    # For example, place a market buy order
                    open_orders[symbol] = place_market_buy_order(symbol, quantity)
                    open_positions[symbol] = 'BUY'
                    last_order_types[symbol] = 'BUY'

                elif (
                    close_positions[symbol] == 'BUY' and 
                    histogram.iloc[-2] <= histogram.iloc[-3] and
                    histogram.iloc[-3] >= histogram.iloc[-4]
                ):
                    print(f'{symbol} Long Exit Signal')
                    # Close existing long position if short EMA crosses below long EMA
                    close_long_position(symbol, quantity)

                elif (
                    histogram.iloc[-2] <= histogram.iloc[-3] and
                    histogram.iloc[-3] >= histogram.iloc[-4] and
                    stoch_rsi_k.iloc[-2] >= 0.6 and
                    last_order_types[symbol] != 'SELL'
                ):
                    print(f'{symbol} Sell Signal (Short EMA cross under Open)')
                    # Implement your sell logic here for futures
                    # For example, place a market sell order
                    open_orders[symbol] = place_market_sell_order(symbol, quantity)
                    open_positions[symbol] = 'SELL'
                    last_order_types[symbol] = 'SELL'

                elif (
                    close_positions[symbol] == 'SELL' and
                    histogram.iloc[-2] >= histogram.iloc[-3] and
                    histogram.iloc[-3] <= histogram.iloc[-4]
                ):
                    print(f'{symbol} Short Exit Signal')
                    # Close existing short position if short EMA crosses above long EMA
                    close_short_position(symbol, quantity)


            # Sleep for some time (e.g., 15 minutes) before checking again
            time.sleep(60)

        except Exception as e:
            print(f'An error occurred: {e}')
            time.sleep(60)  # Wait for a minute before trying again

# Run the trading strategy
macd_strategy()
