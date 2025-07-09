from abc import ABC, abstractmethod
from binance.client import Client

class ObjectABC(ABC):
  def __init__(self):
    super().__init__()

  @abstractmethod
  def _fetch_(self, client:Client):
    pass

  @abstractmethod
  def __str__(self):
    return super().__str__()