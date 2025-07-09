from bitcode.predictors.base import BasePredictor
import numpy

predictor = BasePredictor()
print (predictor.dataset)

predictor.add_dataset_value(numpy.array([1, 2, 3]))
print (predictor.dataset)

predictor.add_dataset_value(numpy.array([4, 5, 6]), 0)
print (predictor.dataset)

predictor.add_dataset_value(10)
print (predictor.dataset)

predictor.add_dataset_value(10.10)
print (predictor.dataset)

predictor.add_dataset_value([10, 20])
print (predictor.dataset)
