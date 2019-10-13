# deeptrading-tfserving-python

<!---
Client from https://github.com/epigramai/tfserving-python-predict-client
-->

## Working in process. Do not use yet!!

## Tensorflow serving client
This is a tensorflow serving client implementation from https://github.com/epigramai/tfserving-python-predict-client.

The predict client is meant to be used with a model served by TensorFlow Serving. Because tfserving model server runs a gRPC service, it cannot be requested by just sending a normal HTTP request. The predict_client package is a grcp client that can request the service.

Read the author blog posts about TensorFlow Serving:

[Part 1](https://medium.com/p/a79726f7c103/) and [Part 2](https://medium.com/p/682eaf7469e7/)

and also my post serie: Deeptrading with tensorflow specially:
https://todotrader.com/deep-trading-with-tensorflow-viii/


### Install
`pip install git+ssh://git@github.com/epigramai/tfserving-python-predict-client.git`

### If you need a model server
There is one here https://github.com/bitnami/bitnami-docker-tensorflow-serving

## How to use
Check out the examples.

### predict_client.prod_client ProdClient
def __init__(self, host, model_name, model_version):
 - host: the host (e.g. localhost:9000)
 - model_name: your model name, e.g. 'mnist'
 - model_version: model version, e.g. 1.
 
ProdClient.predict(self, request_data, request_timeout=10):
 - request_data: A list of input tensors, see the example.
 - request_timeout: timeout sent to the grcp stub
 
 `from predict_client.prod_client import ProdClient`
 
 `client = ProdClient('localhost:9000', 'mnist', 1)`
 
 `client.predict(request_data)`
 
 The predict function returns a dictionary with keys and values for each output tensor. The values in the dictionary will have the same shapes as
 the output tensor's shape. If an error occurs, predict will return an empty dict.
 
### predict_client.inmemory_client InMemoryClient
def __init__(self, model_path):
 - model_path
 
InMemoryClient.predict(self, request_data, request_timeout=None):
 - request_data and request_timeout same as ProdClient, except request_timeout not used in this client.
 
 `from predict_client.inmemory_client import InMemoryClient`
 
 `client = InMemoryClient('path/to/model.pb')`
 
 `client.predict(request_data)`
 
The predict function returns a dictionary with keys and values for each output tensor. The values in the dictionary will have the same shapes as
the output tensor's shape. If an error occurs, predict will return an empty dict.
  
### predict_client.mock_client MockClient
def __init__(self, mock_response):
 - mock_response
 
MockClient.predict(self, request_data, request_timeout=None):
 - request_data and request_timeout same as ProdClient, except request_timeout not used in mock client.
 
 `from predict_client.mock_client import MockClient` 
 
 `client = MockClient(mock_response)`
 
 `client.predict(request_data)`
 
The mock client predict function simply returns the mock response.


## Development

### Generate python code from .proto files
`pip install grpcio-tools`
`python -m grpc_tools.protoc -I protos/ --python_out=predict_client/pbs --grpc_python_out=predict_client/pbs protos/*`
