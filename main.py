import asyncio
from telegram_bot import send_signal

async def main():
    await send_signal(
        "🟢 BUY SIGNAL\nPair: EURUSD\nEntry: Next Candle\nExpiry: 2 Minute"
    )

asyncio.run(main())
