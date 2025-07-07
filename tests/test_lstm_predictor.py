from bitcode.predictor.lstm_predictor import LSTMPredictor

def test_lstm_predict_next():
    predictor = LSTMPredictor(symbol="BTCUSDT", window=10)
    try:
        pred = predictor.predict_next()
        print(f"Predicción LSTM de precio BTC/USDT: {pred}")
        assert pred > 0
    except Exception as e:
        print(f"Error en la predicción LSTM: {e}")
        assert False

if __name__ == "__main__":
    test_lstm_predict_next()
