from telethon import TelegramClient, events
from dotenv import load_dotenv
import os

load_dotenv()

api_id: str | None = os.getenv("API_ID")
api_hash: str | None = os.getenv("API_HASH")
bot_token: str | None = os.getenv("BOT_TOKEN")

assert api_id is not None, "API_ID is not set"
assert api_hash is not None, "API_HASH is not set"
assert bot_token is not None, "BOT_TOKEN is not set"

client = TelegramClient("anon", int(api_id), api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage)  # type: ignore
async def handler(event):
    print(event.raw_text)
    await event.response("Sup boy?")


client.run_until_disconnected()
