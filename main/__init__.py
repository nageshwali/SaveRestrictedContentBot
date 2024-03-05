from pyrogram import Client
from telethon.sync import TelegramClient
from decouple import config
import logging

# Set up logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.INFO)

# Read configurations
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)

# Start Pyrogram bot
bot = Client("SaveRestrictedBot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Start Telethon userbot
userbot = TelegramClient("SaveRestrictedUserbot", session=SESSION, api_id=API_ID, api_hash=API_HASH)

# Define a flag to track if userbot started successfully
userbot_started = False

async def main():
    global userbot_started
    try:
        await bot.start()
        await userbot.start()
        userbot_started = True
    except Exception as e:
        logging.error(f"Error starting clients: {e}")

# Run the main function
if __name__ == "__main__":
    bot.loop.run_until_complete(main())
    if not userbot_started:
        logging.error("Userbot failed to start! Please check your session configuration.")
