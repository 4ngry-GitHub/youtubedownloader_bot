# Telegram Audio Downloader Bot

![GitHub](https://github.com/4ngry-GitHub/youtubedownloader_bot.git)
![GitHub issues](https://github.com/4ngry-GitHub/youtubedownloader_bot/issues)

A Telegram bot that allows users to download audio files from video content. This bot is asynchronous and capable of extracting audio from various video formats.

## Features

- Download audio from video files.
- Support for various video formats (e.g., MP4, AVI, MKV).
- Asynchronous processing for improved performance.
- Simple and user-friendly Telegram bot interface.
- Customizable options for audio extraction.

## Getting Started
Create some .env file or envvar with settings accordind settings.py (src/settings.py)
- pip install -r requirements.txt
- python src/main.py

### Prerequisites

- Python 3.8+
- Telegram Bot Token (You can obtain this by talking to the [BotFather](https://core.telegram.org/bots#botfather))
- Install the required dependencies using pip:

```bash
pip install -r requirements.txt
## Usage
# Copy code
git clone https://github.com/yourusername/telegram-audio-downloader-bot.git
cd telegram-audio-downloader-bot
Create a configuration file (e.g., config.ini) and add your Telegram Bot Token:
ini
Copy code
[Telegram]
token = YOUR_BOT_TOKEN_HERE
Run the bot:
bash
Copy code
python main.py
Start a conversation with your bot on Telegram and use the following commands:
/start - Start the bot and get usage instructions.
/download - Send a video file to extract audio.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to help improve this project. Please read our contributing guidelines for more details.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the aiogram and pytube libraries for making it easy to create.
