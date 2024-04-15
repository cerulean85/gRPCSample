import os, sys, config
current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
conf = config.get_config(path=current_path)

sys.path.append(current_path + '/proto')

import grpc
import network as net

from proto import bee4_pb2
from proto import bee4_pb2_grpc

def get_worker_stub():
    worker_conf = conf["server"]["worker"]
    worker_addr = worker_conf["addr"]
    worker_port = worker_conf["port"]
    channel = grpc.insecure_channel(f"{worker_addr}:{worker_port}")
    stub = bee4_pb2_grpc.Bee4ServiceStub(channel)
    return stub

def are_you_idle():
    
    stub = get_worker_stub()
    result = stub.AreYouIdle(bee4_pb2.EmptyParam())

    print(result)
    print(result)
    print(result)
    print(result)
    print(result)
    print(result)
    print(result)

    return result

def deliver():
    stub = get_worker_stub()
    result = stub.Deliver(bee4_pb2.Feed(
      no = 999,
      botType = "please",
      script = "No Contents",
      botAnswer = "No Contents!"
    ))
    
    print(result)
    print(result)

    return result

if __name__ == '__main__':
    # deliver()

    manager_conf = conf["server"]["manager"]
    worker_addr = manager_conf["addr"]
    worker_port = manager_conf["port"]

    net.start_rpc_server(worker_addr, worker_port)

