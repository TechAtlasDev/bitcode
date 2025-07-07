import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../bitcode')))

from bitcode.predictor.simple_predictor import SimplePredictor

def test_predict_next():
    predictor = SimplePredictor(symbol="BTCUSDT", window=3)
    try:
        pred = predictor.predict_next()
        print(f"Predicción de precio BTC/USDT (promedio simple últimas 3): {pred}")
        assert pred > 0
    except Exception as e:
        print(f"Error en la predicción: {e}")
        assert False

if __name__ == "__main__":
    test_predict_next()
