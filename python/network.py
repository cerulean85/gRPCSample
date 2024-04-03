import sys
sys.path.append(r'C:\Users\zhkim\Desktop\git\test\proto')
from proto.WorkProtocol import WorkProtocol
from proto import WorkProtocolService_pb2_grpc
from concurrent import futures
import grpc

import sys
sys.path.append("C:/Users/zhkim/Desktop/git/test/proto")

def start_rpc_server(addr, port):
    print("Started gRPC Server... {}:{}".format(addr, port))
    proc = WorkProtocol()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    WorkProtocolService_pb2_grpc.add_WorkProtocolServiceServicer_to_server(proc, server)
    server.add_insecure_port("{}:{}".format(addr, port))
    server.start()
    server.wait_for_termination()
