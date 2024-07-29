# Bitcoin Price Bot

This is a Telegram bot that monitors the Bitcoin price using Binance's API and reports price changes along with candlestick patterns in a Telegram chat.

## Features

- **Price Monitoring**: Continuously monitors Bitcoin price and calculates percentage changes.
- **Severity Reporting**: Reports the severity of price changes based on predefined thresholds.
- **Candlestick Patterns**: Identifies and reports candlestick patterns from the recent data.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/bitcoin-price-bot.git
    ```

2. Install the required Python packages:

    ```bash
    pip install pyTelegramBotAPI requests pandas ta
    ```

3. Replace `YOUR_TELEGRAM_API_TOKEN` in the script with your actual Telegram bot API token.

## Usage

1. Run the bot script:

    ```bash
    python bot.py
    ```

2. Start the bot by sending the `/start` command in your Telegram chat.

## Configuration

- **TELEGRAM_API_TOKEN**: Your Telegram bot token.
- **BINANCE_API_URL**: API URL for fetching Bitcoin price.
- **BINANCE_CANDLESTICK_API_URL**: API URL for fetching candlestick data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- [Technical Analysis Library (TA)](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)
