import os
import proto.service_rpc as service_rpc
import conf.service_config as service_conf

current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
conf = service_conf.get_config(path=current_path)

worker_config = conf["server"]["worker"]
worker_addr = worker_config["addr"]
worker_port = worker_config["port"]

if __name__ == '__main__':
    service_rpc.start_rpc_server(worker_addr, worker_port)
