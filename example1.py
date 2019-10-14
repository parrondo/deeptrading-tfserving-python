#
# Example 1 file
#
# This client send 3 requests to the Tensorflow server.
# The content of the request data is a numpy array with three columns
# representing three OHLC sample data, to test the version 1 of
# the model '07_First_Forex_Prediction'
# Note the 'in_tensor_name': 'X' which must be the same in your model tensor name.
#
# Author: R.M.Parrondo
#https://github.com/parrondo/deeptrading-tfserving-python
#

import logging
import numpy as np

from predict_client.prod_client import ProdClient

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

# In each file/module, do this to get the module name in the logs
logger = logging.getLogger(__name__)

# Make sure you have a model running on localhost:8500
host = '0.0.0.0:8500'
model_name = '07_First_Forex_Prediction'
model_version = 1

client = ProdClient(host, model_name, model_version)
data = np.array([[1.87374825, 1.87106024, 1.87083053, 1.86800846],
                 [1.87224386, 1.8729944 , 1.87405399, 1.8712318 ],
                 [1.86558156, 1.86289375, 1.86008567, 1.86521489]])
req_data = [{'in_tensor_name': 'X', 'in_tensor_dtype': 'DT_FLOAT', 'data': data}]

prediction = client.predict(req_data, request_timeout=10)
for k in prediction:
    logger.info('Prediction key: {}, shape: {}'.format(k, prediction[k].shape))
    logger.info('Prediction key: {}, shape: {}'.format(k, prediction[k]))
