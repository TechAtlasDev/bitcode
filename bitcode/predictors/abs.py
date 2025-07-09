from abc import ABC, abstractmethod
import numpy as np

class PredictorABC(ABC):
  def __init__(self) -> None:
    super().__init__()
  
  @abstractmethod
  def predict(self) -> np.array:
    """
    Predecir el siguiente precio.
    """
    pass