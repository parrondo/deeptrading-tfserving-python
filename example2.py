import logging
import numpy as np

from predict_client.prod_client import ProdClient

# generate random floating point values
from random import seed
from random import random

# seed random number generator
seed(1)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# In each file/module, do this to get the module name in the logs
logger = logging.getLogger(__name__)

# Make sure you have a model running on localhost:8500
host = '0.0.0.0:8500'
model_name = 'pif'
model_version = 1

client = ProdClient(host, model_name, model_version)

# Generate random numbers between mini and maxi
repetitions = 100
# Change mini and maxi in order to get prices 
mini = 0.9
maxi = 1.5

#Number of repetitions
for _ in range(repetitions):
    # Generating random OHLC data
    o = mini + (random() * (maxi - mini))
    h = o + random()*0.01
    l = o - random()*0.01
    c = (h + l)/2
    # Constructing data array. You can use a batch of M samples.
    # So data must be an array of dimension M x 4
    data = np.array([[o, h, l, c]])

    req_data = [{'in_tensor_name': 'X', 'in_tensor_dtype': 'DT_FLOAT', 'data': data}]
    prediction = client.predict(req_data, request_timeout=10)
    for k in prediction: 
        #ram logger.info('Prediction key: {}, shape: {}'.format(k, prediction[k].shape))
        #ram logger.info('Prediction key: {}, shape: {}'.format(k, prediction[k]))
        print("data =", data, "prediction =", prediction[k])
