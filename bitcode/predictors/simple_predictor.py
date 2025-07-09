from .base import BasePredictor
import numpy as np

class SimplePredictor(BasePredictor):
    """
    Clase que tiene el enfoque de predecir el valor numérico próximo basándose en su set de datos.
    """

    def predict(self) -> np.array:
        """
        Predice el siguiente precio usando el promedio simple de los últimos N precios.
        """
        return sum(self.dataset) / len(self.dataset)