import pandas as pd
from binance.client import Client



def pegar_historico(par, intervalo, data_inicio):

    client = Client()
    klines = client.get_historical_klines(par, intervalo, data_inicio)
    
    df = pd.DataFrame(klines, columns=[
    "timestamp", "open", "high", "low", "close", "volume",
    "close_time", "quote_asset_volume", "number_of_trades",
    "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
    ])

    # Converter timestamp para datetime
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    cols = ["open", "high", "low", "close", "volume"]
    df[cols] = df[cols].astype(float)
    return df