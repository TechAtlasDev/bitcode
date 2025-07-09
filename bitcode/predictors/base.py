from typing import Union
import numpy as np

from .abs import PredictorABC

class BasePredictor(PredictorABC):
  def __init__(self) -> None:
    self.dataset = np.array([])
  
  def add_dataset_value(self, values:Union[list, int, float, np.array], pos:int=-1):
    if isinstance(values, np.ndarray):
      if pos == -1:
        self.dataset = values

      else:
        self.dataset = np.insert(self.dataset, pos, values)

    if isinstance(values, int) or isinstance(values, float):
      self.dataset = np.append(self.dataset, np.array([values]))
    
    if isinstance(values, list):
      self.dataset = np.append(self.dataset, np.array(values))

    return self