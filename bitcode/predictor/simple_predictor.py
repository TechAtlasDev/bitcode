from typing import List
from ..core.bot import Bitbot


class SimplePredictor:
    """
    Un predictor simple para el precio de BTC/USDT basado en el promedio de los últimos N precios.
    """
    def __init__(self, symbol: str = "BTCUSDT", window: int = 5):
        self.symbol = symbol
        self.window = window
        self.bot = Bitbot()

    def get_last_prices(self) -> List[float]:
        last_trades = self.bot.get_lastTickers(self.symbol, limit=self.window)
        return [trade.price for trade in last_trades]

    def predict_next(self) -> float:
        """
        Predice el siguiente precio usando el promedio simple de los últimos N precios.
        """
        prices = self.get_last_prices()
        if not prices:
            raise ValueError("No se pudieron obtener precios recientes.")
        return sum(prices) / len(prices)
