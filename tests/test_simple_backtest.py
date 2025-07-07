import numpy as np
from bitcode.predictor.simple_predictor import SimplePredictor
from bitcode.core.bot import Bitbot
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt

def backtest_simple(symbol="BTCUSDT", window=10, test_size=10):
    bot = Bitbot()
    n_prices = window + test_size
    last_trades = bot.get_lastTickers(symbol, limit=n_prices)
    prices = np.array([trade.price for trade in last_trades])
    available = len(prices)
    if available <= window:
        print(f"No hay suficientes precios históricos para probar. Solo hay {available}, ventana={window}.")
        print("Reduce el tamaño de la ventana o espera a que haya más trades.")
        return
    max_test = available - window
    if test_size > max_test:
        print(f"Solo hay datos para {max_test} pruebas. Ajustando test_size a {max_test}.")
        test_size = max_test
    preds = []
    y_true = []
    for i in range(test_size):
        train_seq = prices[i:i+window]
        real_next = prices[i+window]
        predictor = SimplePredictor(symbol=symbol, window=window)
        predictor.get_last_prices = lambda: train_seq.tolist()
        try:
            pred = predictor.predict_next()
        except Exception as e:
            print(f"Error en la predicción en paso {i}: {e}")
            pred = np.nan
        preds.append(pred)
        y_true.append(real_next)
        print(f"Predicción: {pred:.2f} | Real: {real_next:.2f}")
    preds = np.array(preds)
    y_true = np.array(y_true)
    mask = ~np.isnan(preds)
    preds = preds[mask]
    y_true = y_true[mask]
    if len(preds) == 0:
        print("No se pudo calcular ninguna predicción válida.")
        return
    mae = mean_absolute_error(y_true, preds)
    mse = mean_squared_error(y_true, preds)
    print(f"\nMAE: {mae:.2f} | MSE: {mse:.2f}")
    plt.plot(y_true, label="Real")
    plt.plot(preds, label="Predicho")
    plt.xlabel("Paso de prueba")
    plt.ylabel("Precio BTC/USDT")
    plt.title("Backtest Simple Predictor")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    backtest_simple(symbol="BTCUSDT", window=10, test_size=10)
