import requests
import json
import time
import hashlib
import hmac
import urllib.parse

# Binance API keys
api_key = 'cOmCONWJRpxWr9XGwwJoKPLQSWeWIwMjoobgqXKG6cqO6GmtIaXdsMEjsHXJcNQU'
api_secret = 'AC4x9ihiOezuEtqz0lRcO5QOHgGQUwFZ3TOyJw38SXmsePIM1KmNWeVYw0H4nXO2'

# Telegram bot token and chat ID
telegram_bot_token = '6811110812:AAFNJp5kcSh0KZ71Yizf8Y3rPBarz-ywopM'
telegram_chat_id = '1385370555'

# Variable to store the last message sent
last_message = {}

# Function to create signature for request
def generate_signature(data):
    return hmac.new(api_secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

# Function to get future account balance
def get_future_balance(api_key, api_secret):
    try:
        # Construct request URL
        base_url = 'https://fapi.binance.com'
        endpoint = '/fapi/v2/account'
        url = base_url + endpoint
        
        # Add API key, timestamp, and signature to request headers
        timestamp = int(time.time() * 1000)
        recv_window = 10000  # Adjust the value as needed, in milliseconds
        query_string = urllib.parse.urlencode({'timestamp': timestamp})
        signature = generate_signature(query_string)
        headers = {
            'X-MBX-APIKEY': api_key,
            'recvWindow': str(recv_window)  # Convert recvWindow to string
        }
        
        # Send request
        response = requests.get(url, headers=headers, params={'timestamp': timestamp, 'signature': signature})
        data = response.json()
        
        # Parse response
        if 'assets' in data:
            assets = data['assets']
            for asset in assets:
                asset_name = asset['asset']
                balance = float(asset['walletBalance'])
                yield asset_name, balance
        else:
            print("Failed to fetch future account balances:", data)
    except Exception as e:
        print("An error occurred:", e)

# Function to send message to Telegram
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    data = {
        "chat_id": telegram_chat_id,
        "text": message
    }
    response = requests.post(url, data=data)
    return response.json()

# Function to monitor balance changes
def monitor_balance(api_key, api_secret):
    prev_balances = {}  # Dictionary to store previous balances
    global last_message
    while True:
        for asset, balance in get_future_balance(api_key, api_secret):
            if prev_balances.get(asset) != balance:
                message = f"{asset}: Balance ${balance:.2f} USDT"
                print(message)
                send_telegram_message(message)
                last_message[asset] = message
                prev_balances[asset] = balance
        time.sleep(300)  # Wait for 5 seconds before checking again

# Main function to run the bot
def main():
    print("Monitoring Future Balances for increase or no change compared to $100 USDT:")
    monitor_balance_increase(api_key, api_secret)

if __name__ == "__main__":
    main()
