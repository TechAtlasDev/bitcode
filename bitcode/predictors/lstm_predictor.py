import numpy as np

from .base import BasePredictor
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout

class LSTMPredictor(BasePredictor):
    def __init__(self) -> None:
        super().__init__()
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None

    def __build_model__(self, input_length: int) -> Sequential:
        model = Sequential()
        
        model.add(LSTM(64, return_sequences=True, input_shape=(input_length, 1)))
        model.add(Dropout(0.2))
        
        model.add(LSTM(32))
        model.add(Dropout(0.2))
        
        model.add(Dense(1))

        model.compile(optimizer='adam', loss='mse')
        return model

    def predict(self) -> float:
        if self.dataset is None or len(self.dataset) < 3:
            raise ValueError("Dataset insuficiente para predicción con LSTM.")

        data = self.dataset.reshape(-1, 1)
        scaled = self.scaler.fit_transform(data)

        n_steps = 30
        X, y = [], []
        for i in range(len(scaled) - n_steps):
            X.append(scaled[i:i + n_steps])
            y.append(scaled[i + n_steps])

        if len(X) == 0:
            raise ValueError("No hay suficientes datos para crear secuencias.")

        X = np.array(X)
        y = np.array(y)

        self.model = self.__build_model__(n_steps)

        self.model.fit(X, y, epochs=100, batch_size=16)

        last_seq = scaled[-n_steps:].reshape(1, n_steps, 1)
        pred_scaled = self.model.predict(last_seq)

        last_known = scaled[-1]
        pred = self.scaler.inverse_transform(np.vstack([last_known, pred_scaled]))[-1][0]

        return float(pred)
