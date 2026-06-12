import yfinance as yf
from ta.trend import EMAIndicator, MACD
from ta.momentum import RSIIndicator


def check_pair(symbol):

    data = yf.download(
        symbol,
        period="5d",
        interval="5m",
        progress=False,
        auto_adjust=True
    )

    if data.empty:
        return None

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

    # BUY SIGNAL
    if (
        latest_ema9 > latest_ema21
        and latest_rsi > 50
        and latest_macd > latest_signal
    ):
        return ("BUY", symbol)

    # SELL SIGNAL
    elif (
        latest_ema9 < latest_ema21
        and latest_rsi < 50
        and latest_macd < latest_signal
    ):
        return ("SELL", symbol)

    return None


def get_signal():

    try:

        pairs = [
            "EURUSD=X",
            "GBPUSD=X",
            "AUDUSD=X",
            "USDJPY=X",
            "USDCAD=X",
            "USDCHF=X",
            "NZDUSD=X",
            "EURJPY=X"
        ]

        for pair in pairs:

            result = check_pair(pair)

            if result is not None:
                return result

        return None

    except Exception as e:
        print("ERROR:", e)
        return None
