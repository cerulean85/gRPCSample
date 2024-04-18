import grpc
import proto.service_rpc as service_rpc
import conf.service_config as service_conf
from proto import bee4_pb2, bee4_pb2_grpc

class Bee4Service:

  def start_service(self, addr, port):
      service_rpc.start_rpc_server(addr, port)    

  def get_worker_stub(self):
    worker_conf = service_conf.get_server_conf(target="worker")
    worker_addr = worker_conf["addr"]
    worker_port = worker_conf["port"]   
    channel = grpc.insecure_channel(f"{worker_addr}:{worker_port}")
    stub = bee4_pb2_grpc.Bee4ServiceStub(channel)
    return stub

  def get_manager_stub(self):
    manager_conf = service_conf.get_server_conf(target="manager")
    manager_addr = manager_conf["addr"]
    manager_port = manager_conf["port"]   
    channel = grpc.insecure_channel(f"{manager_addr}:{manager_port}")
    stub = bee4_pb2_grpc.Bee4ServiceStub(channel)
    return stub