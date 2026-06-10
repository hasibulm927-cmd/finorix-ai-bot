
import asyncio
from strategy import get_signal
from telegram_bot import send_signal

async def main():

    print("Bot Started")

    signal = get_signal()

    print("Signal =", signal)

    if signal == "BUY":
        await send_signal("BUY SIGNAL")
        print("BUY sent")

    elif signal == "SELL":
        await send_signal("SELL SIGNAL")
        print("SELL sent")

    else:
        print("WAIT")

asyncio.run(main())
