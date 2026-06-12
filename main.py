import asyncio
from strategy import get_signals
from telegram_bot import send_signal

async def main():

    signals = get_signals()

    if not signals:
        return

    for signal, pair in signals:

        pair_name = pair.replace("=X", "")

        if signal == "BUY":

            await send_signal(
                f"🟢 BUY SIGNAL\n"
                f"Pair: {pair_name}\n"
                f"Entry: Next Candle\n"
                f"Expiry: 5 Minute"
            )

        elif signal == "SELL":

            await send_signal(
                f"🔴 SELL SIGNAL\n"
                f"Pair: {pair_name}\n"
                f"Entry: Next Candle\n"
                f"Expiry: 5 Minute"
            )

asyncio.run(main())
