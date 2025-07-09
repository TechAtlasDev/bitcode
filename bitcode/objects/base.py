from .abs import ObjectABC
from binance.client import Client

class Object(ObjectABC):
  def __init__(self):
    pass

  def _fetch_(self, client:Client):
    pass

  def __str__(self):
    return f"{self.__class__.__name__}()"