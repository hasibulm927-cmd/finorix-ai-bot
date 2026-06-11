import asyncio
from strategy import get_signal
from telegram_bot import send_signal

async def main():

    signal = get_signal()

    if signal == "BUY":
        await send_signal(
            "🟢 BUY SIGNAL\n"
            "Pair: EURUSD\n"
            "Entry: Next Candle\n"
            "Expiry: 2 Minute"
        )

    elif signal == "SELL":
        await send_signal(
            "🔴 SELL SIGNAL\n"
            "Pair: EURUSD\n"
            "Entry: Next Candle\n"
            "Expiry: 2 Minute"
        )

asyncio.run(main())
