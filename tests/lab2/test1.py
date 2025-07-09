import os
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

from bitcode.utils.utils_time import now_in_num
from bitcode.predictor import simple_predictor
from bitcode.enums import Symbols
from bitcode.core.bot import Binance
from bitcode.objects import Kline

# --- Predicción ---
predictor = simple_predictor.SimplePredictor(symbol=Symbols.BTCUSDT, window=300)
try:
    prediccion = predictor.predict_next()
    print(f"Prediccion: {prediccion:.2f}") # Formatear para mejor lectura
except Exception as e:
    print(f"Error al generar la predicción: {e}")
    prediccion = None

# --- Obtención del Valor Real ---
binance = Binance()
last_kline = None
true_val = None

try:
    # Obteniendo las ultimas velas desde hace los 2 ultimos minutos
    # Esto asume que estás buscando la última vela de 1 minuto completa.
    now_2_minutes_ago_ms = now_in_num(120) 
    
    # La consulta debe ser lo suficientemente amplia para asegurar que obtengamos al menos 1 vela.
    # Un 'limit=1' puede ser útil si bitcode lo soporta para obtener la *última* directamente.
    # Si no, pedir un rango y tomar la última ([-1]) es el camino.
    klines_data = binance.query(Kline(Symbols.BTCUSDT, start_str=now_2_minutes_ago_ms))
    
    if klines_data:
        last_kline = klines_data[-1]
        true_val = last_kline.close
        print(f"Valor real: {float(true_val):.2f}") # Formatear para mejor lectura
    else:
        print("Valor real: No data available (No se encontraron klines en el rango solicitado)")

except IndexError: # Especificamos IndexError para cuando la lista está vacía
    print("Valor real: No data available (Lista de klines vacía. Verifique el rango y la disponibilidad de datos.)")
except Exception as e: # Cualquier otro error de red o de la API
    print(f"Valor real: No data available (Error durante la consulta a Binance: {e})")

# Opcional: Comparación de resultados (solo si la predicción y el valor real existen)
if prediccion is not None and true_val is not None:
    difference = abs(prediccion - float(true_val))
    percentage_difference = (difference / float(true_val)) * 100 if float(true_val) != 0 else 0
    print(f"Diferencia absoluta (Predicción vs Real): {difference:.2f} USDT")
    print(f"Diferencia porcentual: {percentage_difference:.2f}%")