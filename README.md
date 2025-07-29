# Telegram Training Bot

A Telegram bot designed to help users track their training objectives and goals.

## Features

- Track training objectives (marathon, weight loss, etc.)
- User authorization system
- CSV file handling for training data
- Persistent user data storage

## Setup

1. Clone this repository:
`ash
git clone <your-repo-url>
cd telegram-training-bot
`

2. Create a virtual environment:
`ash
python -m venv venv
venv\Scripts\activate  # On Windows
# or
source venv/bin/activate  # On Linux/Mac
`

3. Install dependencies:
`ash
pip install -r requirements.txt
`

4. Create a .env file with your bot token:
`
TELEGRAM_BOT_TOKEN=your_bot_token_here
`

5. Run the bot:
`ash
python AI_train_bot.py
`

## Configuration

- Update config.py with authorized user IDs
- Modify training objectives in the bot logic as needed

## Files

- AI_train_bot.py - Main bot file
- config.py - Configuration settings
- memory.py - User data persistence
- handlers/ - Command handlers
- core/ - Core functionality
- equirements.txt - Python dependencies

## License

This project is open source and available under the [MIT License](LICENSE).
