import sys
sys.path.append(r'E:\gRPCSample\python\proto')

from proto.Bee4Service import Bee4Service
from proto import bee4_pb2_grpc
from concurrent import futures
import grpc

def start_rpc_server(addr, port):
    print("Started gRPC Server... {}:{}".format(addr, port))
    proc = Bee4Service()
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    bee4_pb2_grpc.add_Bee4ServiceServicer_to_server(proc, server)
    server.add_insecure_port("{}:{}".format(addr, port))
    server.start()
    server.wait_for_termination()

# from proto.WorkProtocol import WorkProtocol
# from proto import WorkProtocolService_pb2_grpc
# from concurrent import futures
# import grpc

# def start_rpc_server(addr, port):
#     print("Started gRPC Server... {}:{}".format(addr, port))
#     proc = WorkProtocol()
#     server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
#     WorkProtocolService_pb2_grpc.add_WorkProtocolServiceServicer_to_server(proc, server)
#     server.add_insecure_port("{}:{}".format(addr, port))
#     server.start()
#     server.wait_for_termination()
