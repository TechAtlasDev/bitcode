from bitcode.core.bot import Binance
from bitcode.objects import Kline

from bitcode.enums import Symbols

binance = Binance()
klines:list[Kline] = binance.query(Kline(Symbols.BTCUSDT, interval="1m", limit=1000))

for kline in klines:
  print (f"{kline}, Precio final: {kline.close}")

from bitcode.utils.graph import Graph

graficador = Graph()
graficador.graficar_secuencia_puntos([int(kline.close.split(".")[0]) for kline in klines], y=[kline.openTime for kline in klines])