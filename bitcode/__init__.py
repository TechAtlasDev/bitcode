from .core.bot import Bitbot
from .utils.graph import Graph

def getTicker():
  bot = Bitbot() # Creando nuestro bot
  graficador = Graph(
    x="Secuencia", 
    y="Precio", 
    title="Secuencia de valores de bitcoin"
  ) # Creando el graficador

  lista_puntos = []
  lista_tiempo = []
  tickers = bot.get_lastTickers("BTCUSDT", 200)
  for ticker in tickers:
    lista_puntos.append(ticker.price)
    lista_tiempo.append(ticker.time)
  
  graficador.graficar_secuencia_puntos(lista_puntos)