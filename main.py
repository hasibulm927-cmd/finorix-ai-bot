import asyncio
from strategy import get_signal
from telegram_bot import send_signal

async def main():

    signal = get_signal()

    if signal == "BUY":
        await send_signal(
            "🟢 BUY SIGNAL\nPair: EURUSD\nEntry: Next Candle\nExpiry: 2 Minute"
        )

    elif signal == "SELL":
        await send_signal(
            "🔴 SELL SIGNAL\nPair: EURUSD\nEntry: Next Candle\nExpiry: 2 Minute"
        )

    else:
        print("WAIT")

asyncio.run(main())
