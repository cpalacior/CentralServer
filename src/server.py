
from concurrent import futures

import json
import os
from dotenv import load_dotenv
load_dotenv()
import grpc
import Service_pb2
import Service_pb2_grpc

HOST = os.getenv('HOST')

def listResources():
    file = ''
    with open(os.path.dirname(__file__) + '/database/resources.json') as resources:
        file = json.load(resources)
    return file

def getResourcePath(file, resourceName):
    for peer in file:
        for resource in file[peer]["resources"]:
            print(resource, resourceName)
            if str(resource) == resourceName:
                return 'http://' + file[peer]["url"] + ':' + file[peer]["port"]
    return '404'

class ProductService(Service_pb2_grpc.ProductServiceServicer):
    def getResource(self, request, context):
        print("Request is received: " + str(request.resourceName))
        resourcesFile = listResources()
        #print(resourcesFile)
        resourcePath = getResourcePath(resourcesFile, str(request.resourceName))
        return Service_pb2.TransactionResponse(status_code=200, Response= resourcePath)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Service_pb2_grpc.add_ProductServiceServicer_to_server(ProductService(), server)
    server.add_insecure_port(HOST)
    print("Service is running... ")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()