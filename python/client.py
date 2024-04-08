import sys
sys.path.append(r'C:\Users\zhkim\AppData\Local\Packages\CanonicalGroupLimited.Ubuntu20.04LTS_79rhkp1fndgsc\LocalState\rootfs\home\zhkim\git\Programs\gRPCSample\python\proto')

import os
import grpc
import config as cfg
from proto import helloworld_pb2
from proto import helloworld_pb2_grpc


if __name__ == '__main__':

    addr = "127.0.0.1"
    port = 9091
    channel = grpc.insecure_channel(f"{addr}:{port}")
    stub = helloworld_pb2_grpc.SimpleStub(channel)

    result = stub.SayHello(helloworld_pb2.HelloRequest(name="ㅎㅎㅎㅎ"))

    print(result)


    # current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    # conf = cfg.get_config(path=current_path)
    # addr = conf["server"]["worker"]["addr"]
    # port = conf["server"]["worker"]["port"]
    # channel = grpc.insecure_channel(f"{addr}:{port}")
    # stub = WorkProtocolService_pb2_grpc.WorkProtocolServiceStub(channel)
    #
    # reponseList = [ { "message": "111" }, { "message": "222" } ]
    # result = stub.echo(WorkProtocolService_pb2.Works(workList=reponseList))
    # result = stub.collectUrls(WorkProtocolService_pb2.Works(workList=reponseList))
    # print(result)
