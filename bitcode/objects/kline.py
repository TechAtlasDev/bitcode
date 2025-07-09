from .base import Object
from enum import Enum

class Kline(Object):
    """
    Inicializa un nuevo objeto Kline para manejar datos de velas (candlestick) del mercado de criptomonedas.
    Este constructor crea un objeto Kline con parámetros específicos para recuperar
    datos de velas desde un exchange de criptomonedas.

    Parámetros
    ----------
    symbol : str | Enum
      El símbolo del par de trading (ej., 'BTCUSDT') o un valor Enum que lo represente
    interval : str, default="1m"
      El intervalo de la vela (ej., "1m", "5m", "1h", "1d")
    start_str : str | int, opcional
      El tiempo de inicio para obtener datos, como cadena o timestamp
    end_str : str | int, opcional
      El tiempo de fin para obtener datos, como cadena o timestamp
    limit : int, default=1000
      Número máximo de velas a recuperar

    Atributos Públicos
    -----------------
    OpenTime : int
      El tiempo de apertura de la vela en timestamp de milisegundos
    Open : str
      El precio de apertura de la vela
    High : str
      El precio más alto durante el período de la vela
    Low : str
      El precio más bajo durante el período de la vela
    Close : str
      El precio de cierre de la vela
    Volume : str
      El volumen negociado durante el período de la vela
    CloseTime : int
      El tiempo de cierre de la vela en timestamp de milisegundos
    QuoteAssetVolume : str
      El volumen en el activo cotizado (ej., USDT en BTCUSDT)
    NumberOfTrades : int
      El número de operaciones ejecutadas durante el período de la vela
    TakerBuyBaseAssetVolume : str
      El volumen del activo base comprado por takers
    TakerBuyQuoteAssetVolume : str
      El volumen del activo cotizado comprado por takers
    Ignore : str
      Un atributo que típicamente se ignora en la respuesta de la API
    """
    def __init__(self, symbol:str|Enum, interval:str="1m", start_str:str|int=None, end_str:str|int=None, limit:int=1000):

      self.symbol = symbol.value if isinstance(symbol, Enum) else symbol
      self._interval_ = interval
      self._start_str_ = start_str
      self._end_str_ = end_str
      self._limit_ = limit

      # -- Public Atts --
      self.openTime: int
      self.open: str
      self.high: str
      self.low: str
      self.close: str
      self.volume: str
      self.closeTime: int
      self.quoteAssetVolume: str
      self.numberOfTrades: int
      self.takerBuyBaseAssetVolume: str
      self.takerBuyQuoteAssetVolume: str
      self.ignore: str
      

    def _fetch_(self, client):
      klines_json = client.get_historical_klines(
        symbol=self.symbol, interval=self._interval_, start_str=self._start_str_, end_str=self._end_str_, limit=self._limit_
      )

      klines = []

      for kline_json in klines_json:
        kline = Kline(self.symbol)

        kline.openTime = kline_json[0]
        kline.open = kline_json[1]
        kline.high = kline_json[2]
        kline.low = kline_json[3]
        kline.close = kline_json[4]
        kline.volume = kline_json[5]
        kline.closeTime = kline_json[6]
        kline.quoteAssetVolume = kline_json[7]
        kline.numberOfTrades = kline_json[8]
        kline.takerBuyBaseAssetVolume = kline_json[9]
        kline.takerBuyQuoteAssetVolume = kline_json[10]
        kline.ignore = kline_json[11]

        klines.append(kline)

      return klines
  
    def __repr__(self):
      return f"{self.__class__.__name__}(symbol={self.symbol})"

    def __str__(self):
      return f"{self.__class__.__name__}(symbol={self.symbol})"