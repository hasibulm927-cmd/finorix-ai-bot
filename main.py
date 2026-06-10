from telegram_bot import send_signal
import asyncio

async def main():
    await send_signal("TEST MESSAGE FROM GITHUB")

asyncio.run(main())
