# Bitcoin Action Bot

This is a Telegram bot designed to monitor Bitcoin price and provide updates on price changes and candlestick patterns using Binance's API.

## Features

- **Price Monitoring**: Continuously tracks Bitcoin prices and calculates percentage changes.
- **Severity Reporting**: Reports the severity of price changes based on predefined thresholds.
- **Candlestick Patterns**: Identifies and reports various candlestick patterns from recent data.

## Installation

To install and run this bot on your Ubuntu server, follow these steps:

1. **Open your terminal.**

2. **Run the installation script**:

    ```bash
    curl -sL https://raw.githubusercontent.com/shantiya401/btc_action_bot/main/install.sh | bash
    ```

3. **Enter your Telegram API Token** when prompted.

## Configuration

- **TELEGRAM_API_TOKEN**: Replace `YOUR_TELEGRAM_API_TOKEN` in the script with your Telegram bot token.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI)
- [Requests](https://requests.readthedocs.io/en/latest/)
- [Pandas](https://pandas.pydata.org/)
- [Technical Analysis Library (TA)](https://technical-analysis-library-in-python.readthedocs.io/en/latest/)
