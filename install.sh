#!/bin/bash

# Update package list and install required packages
echo "Updating package list..."
sudo apt-get update

echo "Installing required packages..."
sudo apt-get install -y python3 python3-pip git

# Clone the repository
echo "Cloning the repository..."
git clone https://github.com/shantiya401/btc_action_bot.git

# Change to the project directory
cd btc_action_bot

# Install Python dependencies
echo "Installing Python dependencies..."
pip3 install pyTelegramBotAPI requests pandas ta

# Request for Telegram API Token
read -p "Please enter your Telegram API Token: " TELEGRAM_API_TOKEN

# Replace placeholder with the user-provided token in the Python script
echo "Updating the bot script with the provided Telegram API Token..."
sed -i "s/YOUR_TELEGRAM_API_TOKEN/$TELEGRAM_API_TOKEN/" bot.py

# Run the bot
echo "Starting the bot..."
python3 bot.py
