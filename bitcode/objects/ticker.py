from .base import Object

class Ticker(Object):
  def __init__(self, symbol:str):
    self.symbol = symbol
  
  def _fetch_(self, client) -> str:
    return client.get_symbol_ticker(symbol=self.symbol)
  
  def __repr__(self):
    return f"{self.__class__.__name__}(symbol={self.symbol})"