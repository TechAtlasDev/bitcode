from binance.client import Client
from ..utils.vars import api_key, api_secret

from ..objects import Object

class BinanceClient:
  def __init__(self):
    self.client = Client(api_key, api_secret)
  
  def query(self, object:Object) -> list[object]:
    return object._fetch_(self.client)