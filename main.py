import asyncio
from strategy import get_signal
from telegram_bot import send_signal


async def main():

    result = get_signal()

    if result is None:
        return

    signal, pair = result

    pair_name = pair.replace("=X", "")

    if signal == "BUY":

        await send_signal(
            f"🟢 BUY SIGNAL\n"
            f"Pair: {pair_name}\n"
            f"Entry: Next Candle\n"
            f"Expiry: 2 Minute"
        )

    elif signal == "SELL":

        await send_signal(
            f"🔴 SELL SIGNAL\n"
            f"Pair: {pair_name}\n"
            f"Entry: Next Candle\n"
            f"Expiry: 2 Minute"
        )


asyncio.run(main())
