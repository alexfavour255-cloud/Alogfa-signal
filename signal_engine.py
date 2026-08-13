def trading_signal(price, ema_fast, ema_slow, rsi):
    if ema_fast > ema_slow and rsi < 70:
        return "BUY"

    if ema_fast < ema_slow and rsi > 30:
        return "SELL"

    return "WAIT"


# Test
signal = trading_signal(
    price=100,
    ema_fast=102,
    ema_slow=100,
    rsi=55
)

print("Trading signal:", signal)
