import telebot
import requests
from datetime import datetime
from time import sleep
import pandas as pd
import ta

# API Keys and Setup
TELEGRAM_API_TOKEN = 'YOUR_TELEGRAM_API_TOKEN'
BINANCE_API_URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
BINANCE_CANDLESTICK_API_URL = 'https://api.binance.com/api/v3/klines'

bot = telebot.TeleBot(TELEGRAM_API_TOKEN)

# Global Variables
price_history = []

def get_bitcoin_price():
    response = requests.get(BINANCE_API_URL)
    data = response.json()
    return float(data['price'])

def get_candlestick_data():
    params = {
        'symbol': 'BTCUSDT',
        'interval': '15m',
        'limit': 96  # Last 24 hours (96 * 15 minutes = 24 hours)
    }
    response = requests.get(BINANCE_CANDLESTICK_API_URL, params=params)
    data = response.json()
    df = pd.DataFrame(data, columns=[
        'timestamp', 'open', 'high', 'low', 'close', 'volume', 
        'close_time', 'quote_asset_volume', 'number_of_trades', 
        'taker_buy_base_asset_volume', 'taker_buy_quote_asset_volume', 'ignore'
    ])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('timestamp', inplace=True)
    df = df.astype(float)
    return df

def identify_candlestick_patterns(df):
    patterns = {
        'CDLDOJI': ta.candlestick.CDLDOJI(df['open'], df['high'], df['low'], df['close']),
        'CDLENGULFING': ta.candlestick.CDLENGULFING(df['open'], df['high'], df['low'], df['close']),
        'CDLHANGINGMAN': ta.candlestick.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close']),
        # Add more patterns as needed
    }
    return patterns

def determine_severity(percentage_change):
    if percentage_change > 2:
        return "پامپ 🟢"
    elif percentage_change > 1:
        return "زیاد 🟡"
    elif percentage_change > 0.5:
        return "رو به رشد 🟠"
    elif percentage_change > 0:
        return "عادی 🟣"
    elif percentage_change < -2:
        return "دامپ 🔴"
    elif percentage_change < -1:
        return "ریزش شدید 🟠"
    elif percentage_change < -0.5:
        return "کاهشی 🟤"
    else:
        return "عادی 🟡"

def report_price_changes():
    global price_history
    current_price = get_bitcoin_price()
    now = datetime.now()

    if not price_history:
        price_history.append((now, current_price))
        return

    last_time, last_price = price_history[-1]
    time_diff = (now - last_time).total_seconds() / 3600  # Time difference in hours
    percentage_change = ((current_price - last_price) / last_price) * 100
    severity = determine_severity(percentage_change)

    message = (f"Bitcoin Price Report:\n"
               f"Current Price: ${current_price:.2f}\n"
               f"Percentage Change: {percentage_change:.2f}%\n"
               f"Severity: {severity}\n"
               f"Time: {now.strftime('%Y-%m-%d %H:%M:%S')}")
    bot.send_message(chat_id=message.chat.id, text=message)

    price_history.append((now, current_price))

    # Keep only the last 15 minutes of data
    price_history = [entry for entry in price_history if (now - entry[0]).total_seconds() < 900]

    # Get candlestick data and identify patterns
    df = get_candlestick_data()
    patterns = identify_candlestick_patterns(df)

    for pattern, values in patterns.items():
        last_pattern_value = values.iloc[-1]
        if last_pattern_value != 0:
            message = f"آخرین الگوی {pattern} در تاریخ {now.strftime('%Y-%m-%d')} شناسایی شده است."
            bot.send_message(chat_id=message.chat.id, text=message)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Bitcoin Price Bot is now active.')
    while True:
        report_price_changes()
        sleep(900)  # Wait for 15 minutes before running again

bot.polling()
