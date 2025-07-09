import numpy as np

from bitcode import BinanceClient
from bitcode.objects import Kline
from bitcode.enums import Symbols

from bitcode.predictors.lstm_predictor import LSTMPredictor

# Obteniendo las Klines más recientes
binance = BinanceClient()
klines:list[Kline] = binance.query(Kline(symbol=Symbols.BTCUSDT, limit=365, interval="1d"))

close = np.array([float(kline.close) for kline in klines])
time = np.array([int(kline.closeTime) for kline in klines])

# Creando el modelo
predictor = LSTMPredictor()

predictor.add_dataset_value(close.reshape(-1, 1))

prediccion = predictor.predict()
print (f"Valor predicho: {prediccion}")

last_kline:Kline = binance.query(Kline(symbol=Symbols.BTCUSDT, limit=1))[-1]
print (f"Valor real: {last_kline.close}")


print (f"[-------------]")
print (f"Diferencia: {float(last_kline.close)-prediccion}")
print (f"Diferencia porcentual: {float(abs(float(last_kline.close)-prediccion)/float(last_kline.close)*100):2f}%")
