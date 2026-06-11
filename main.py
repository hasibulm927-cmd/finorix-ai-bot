from telegram_bot import send_signal
import asyncio

async def main():
    await send_signal("BOT IS RUNNING")

asyncio.run(main())
