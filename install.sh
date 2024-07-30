#!/bin/bash

# Update package list and install required packages
echo "Updating package list..."
sudo apt-get update

echo "Installing required packages..."
sudo apt-get install -y python3 python3-pip git

# Remove the existing directory if it exists
if [ -d "btc_action_bot" ]; then
  echo "Removing existing btc_action_bot directory..."
  rm -rf btc_action_bot
fi

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

# Check if TELEGRAM_API_TOKEN is provided
if [[ -z "$TELEGRAM_API_TOKEN" ]]; then
  echo "Error: No Telegram API Token provided."
  exit 1
fi

# Replace placeholder with the user-provided token in the Python script
echo "Updating the bot script with the provided Telegram API Token..."
sed -i "s/YOUR_TELEGRAM_API_TOKEN/$TELEGRAM_API_TOKEN/" bot.py

# Verify token replacement
if grep -q "YOUR_TELEGRAM_API_TOKEN" bot.py; then
  echo "Error: Failed to update the bot script with the provided Telegram API Token."
  exit 1
fi

# Run the bot using nohup
echo "Starting the bot using nohup..."
nohup python3 bot.py &

echo "Bot is running in the background. You can log out now."
