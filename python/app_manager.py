import os, grpc
import threading, time
import conf.service_config as service_conf
import proto.service_rpc as service_rpc
from proto import bee4_pb2
from proto import bee4_pb2_grpc
import storage.service_rdb as service_rdb

current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
conf = service_conf.get_conf()

manager_conf = service_conf.get_server_conf(target="manager")
manager_addr = manager_conf["addr"]
manager_port = manager_conf["port"]

worker_conf = service_conf.get_server_conf(target="worker")
worker_addr = manager_conf["addr"]
worker_port = manager_conf["port"]




def get_worker_stub():
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

    while True:
        bot_board_records = service_rdb.get_bot_board_record()

        for record in bot_board_records:
            if record.state == "idle":
                print(f"{record.idx}")
                break
        time.sleep(3)

    # stub = get_worker_stub()
    # result = stub.Deliver(bee4_pb2.Feed(
    #   no = 999,
    #   botType = "please",
    #   script = "No Contents",
    #   botAnswer = "No Contents!"
    # ))
    
    # print(result)
    # print(result)

    # return result

if __name__ == '__main__':

    threading.Thread(target=deliver).start()
    

    service_rpc.start_rpc_server(worker_addr, worker_port)

