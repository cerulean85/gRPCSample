import sys
sys.path.append(r'C:\Users\zhkim\Desktop\git\test\proto')

import os
import grpc
import config as cfg
from proto import WorkProtocolService_pb2
from proto import WorkProtocolService_pb2_grpc


if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    conf = cfg.get_config(path=current_path)
    addr = conf["server"]["worker"]["addr"]
    port = conf["server"]["worker"]["port"]
    channel = grpc.insecure_channel(f"{addr}:{port}")
    stub = WorkProtocolService_pb2_grpc.WorkProtocolServiceStub(channel)

    reponseList = [ { "message": "111" }, { "message": "222" } ]
    result = stub.echo(WorkProtocolService_pb2.Works(workList=reponseList))
    result = stub.collectUrls(WorkProtocolService_pb2.Works(workList=reponseList))
    print(result)
