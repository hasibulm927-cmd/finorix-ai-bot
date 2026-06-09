import yfinance as yf
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator


def get_signal():

    try:

        data = yf.download(
            "EURUSD=X",
            period="5d",
            interval="5m",
            progress=False,
            auto_adjust=True
        )

        if data.empty:
            return "WAIT"

        close = data["Close"].squeeze()

        ema9 = EMAIndicator(close=close, window=9).ema_indicator()
        ema21 = EMAIndicator(close=close, window=21).ema_indicator()

        rsi = RSIIndicator(close=close, window=14).rsi()

        macd = MACD(close=close)

        latest_ema9 = float(ema9.iloc[-1])
        latest_ema21 = float(ema21.iloc[-1])

        latest_rsi = float(rsi.iloc[-1])

        latest_macd = float(macd.macd().iloc[-1])
        latest_signal = float(macd.macd_signal().iloc[-1])

        if (
            latest_ema9 > latest_ema21
            and latest_rsi > 55
            and latest_macd > latest_signal
        ):
            return "BUY"

        elif (
            latest_ema9 < latest_ema21
            and latest_rsi < 45
            and latest_macd < latest_signal
        ):
            return "SELL"

        else:
            return "WAIT"

    except Exception as e:
        print("ERROR:", e)
        return "WAIT"