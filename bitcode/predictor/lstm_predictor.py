import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler
from ..core.bot import Bitbot

class LSTMPredictor:
    """
    Predictor basado en LSTM para el precio de BTC/USDT.
    Entrena en caliente cada vez que se llama a predict_next (demo simple).
    """
    def __init__(self, symbol: str = "BTCUSDT", window: int = 20):
        self.symbol = symbol
        self.window = window
        self.bot = Bitbot()
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None

    def get_last_prices(self, n=None):
        n = n or self.window + 1
        last_trades = self.bot.get_lastTickers(self.symbol, limit=n)
        return np.array([trade.price for trade in last_trades]).reshape(-1, 1)

    def build_model(self):
        model = Sequential()
        model.add(LSTM(50, input_shape=(self.window, 1)))
        model.add(Dense(1))
        model.compile(optimizer='adam', loss='mse')
        return model

    def predict_next(self):
        prices = self.get_last_prices(self.window + 1)
        if len(prices) <= self.window:
            raise ValueError("No hay suficientes precios para entrenar el modelo.")
        scaled = self.scaler.fit_transform(prices)
        X = []
        y = []
        for i in range(len(scaled) - self.window):
            X.append(scaled[i:i+self.window])
            y.append(scaled[i+self.window])
        X, y = np.array(X), np.array(y)
        if len(X) == 0:
            raise ValueError("No hay suficientes datos para entrenar el modelo LSTM.")
        self.model = self.build_model()
        self.model.fit(X, y, epochs=10, batch_size=1, verbose=0)
        last_seq = scaled[-self.window:].reshape(1, self.window, 1)
        pred_scaled = self.model.predict(last_seq, verbose=0)
        pred = self.scaler.inverse_transform(np.vstack([scaled[-1:], pred_scaled]))[-1][0]
        return float(pred)
