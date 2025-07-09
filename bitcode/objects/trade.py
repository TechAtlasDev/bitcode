from .base import Object
from enum import Enum

class GlobalTrade(Object):
  def __init__(self, symbol:str|Enum, limit:int=10):
    self.symbol = symbol.value if isinstance(symbol, Enum) else symbol
    self.limit = limit

    self.id:int = 0
    self.price:float
    self.qty:float
    self.quoteQty:float
    self.time:int
    self.isBuyerMaker:bool
    self.isBestMatch:bool
  
  def _fetch_(self, client) -> list:
    response = client.get_recent_trades(symbol=self.symbol, limit=self.limit)
    trades = []

    for trade_json in response:
      trade = GlobalTrade(self.symbol)
      trade.id = trade_json["id"]
      trade.price = trade_json["price"]
      trade.qty = trade_json["qty"]
      trade.quoteQty = trade_json["quoteQty"]
      trade.time = trade_json["time"]
      trade.isBuyerMaker = trade_json["isBuyerMaker"]
      trade.isBestMatch = trade_json["isBestMatch"]
      
      trades.append(trade)

    return trades
  
  def __repr__(self):
    return f"{self.__class__.__name__}(symbol={self.symbol}, id={self.id})"