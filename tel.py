# main_script.py

import ccxt
import pandas as pd
from ta.trend import ema_indicator
import asyncio
import nest_asyncio
from telegram import Bot
from config import symbols  # Import symbols from config.py

# Binance API credentials
api_key = 'M0l4CVC4p0BYOqtQbuBtRI8yUHf20a0kbzn61QwrJi7ToAbzFek5whlCoTaa8FAf'
api_secret = 'gxdmqiBh9YB5ADYA2h7bRigxZAz2x1HRCkkr88Lx0pdWeilnJmdyxLIuoUSvG4v4'
interval = '15m'  # 1-day candlesticks

# Telegram Bot Token and Chat ID
telegram_token = '6811110812:AAFNJp5kcSh0KZ71Yizf8Y3rPBarz-ywopM'
chat_id = '1385370555'

# Initialize Binance client
binance = ccxt.binance({
    'apiKey': api_key,
    'secret': api_secret,
})

# Dictionary to store the last alert messages for each symbol
last_alert_messages = {}

# Function to get historical candlestick data
def get_historical_data(symbol, interval, limit=250):
    ohlcv = binance.fetch_ohlcv(symbol, interval, limit=limit)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    return df

# Function to check EMA cross
def check_ema_cross(df, short_period=7, long_period=100):
    df['ema_short'] = ema_indicator(df['close'], window=short_period)
    df['ema_long'] = ema_indicator(df['close'], window=long_period)

    cross_over = df['ema_short'][-1] > df['ema_long'][-1] and df['ema_short'][-2] <= df['ema_long'][-2] and df['ema_short'][-3] <= df['ema_long'][-3]
    cross_under = df['ema_short'][-1] < df['ema_long'][-1] and df['ema_short'][-2] >= df['ema_long'][-2] and df['ema_short'][-3] >= df['ema_long'][-3]

    return cross_over, cross_under

# Function to send Telegram message (now defined as async)
async def send_telegram_message(symbol, message):
    # Check if the current message is the same as the previous one for this symbol
    if last_alert_messages.get(symbol) != message:
        await telegram_bot.send_message(chat_id=chat_id, text=message)
        # Update the last alert message for this symbol
        last_alert_messages[symbol] = message

# Main function (now defined as async)
async def main():
    while True:
        for symbol in symbols:
            try:
                historical_data = get_historical_data(symbol, interval)
                cross_over, cross_under = check_ema_cross(historical_data)

                if cross_over:
                    message = f'EMA Cross Over detected on {symbol} ({interval}).'
                    await send_telegram_message(symbol, message)

                if cross_under:
                    message = f'EMA Cross Under detected on {symbol} ({interval}).'
                    await send_telegram_message(symbol, message)

            except Exception as e:
                print(f"Error processing {symbol}: {e}")

        # Sleep for a specified interval before checking again
        await asyncio.sleep(300)  # Adjust the sleep duration as needed

# Initialize Telegram Bot
telegram_bot = Bot(token=telegram_token)

# Use nest_asyncio to allow running asyncio in Jupyter notebooks
nest_asyncio.apply()

# Create and run the event loop
asyncio.run(main())
