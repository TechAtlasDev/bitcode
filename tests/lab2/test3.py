from bitcode import BinanceClient
from bitcode.objects import Kline
from bitcode.enums import Symbols

from bitcode.predictors.simple_predictor import SimplePredictor

predictor = SimplePredictor()

# Obteniendo klines recientes de binance
binance = BinanceClient()
klines:list[Kline] = binance.query(Kline(Symbols.BTCUSDT, limit=10))

predictor.add_dataset_value(
  [float(kline.close) for kline in klines]
)

# Prediciendo el valor de un bitcoin en dólares
prediccion = predictor.predict()
print (prediccion)