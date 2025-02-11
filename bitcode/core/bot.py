from binance.client import Client
from ..abstractions.analytics import Ticker, SimpleTicker

from ..utils.vars import api_key, api_secret

class Bitbot:
  def __init__(self):
    key = api_key
    secret = api_secret
    self.client = Client(key, secret)

  def getTicker(self, symbol:str) -> SimpleTicker:
    ticker = self.client.get_symbol_ticker(symbol=symbol)
    return SimpleTicker(ticker)

  def get_balance(self, symbol):
    balance = self.client.get_asset_balance(asset=symbol)
    return balance
  
  def get_price(self, symbol):
    price = self.client.get_symbol_ticker(symbol=symbol)
    return price['price']
  
  def get_orderbook(self, symbol):
    orderbook = self.client.get_order_book(symbol=symbol)
    return orderbook
  
  def get_lastTickers(self, symbol, limit=10):
    tickers = self.client.get_recent_trades(symbol=symbol, limit=limit)
    return [Ticker(ticker) for ticker in tickers]