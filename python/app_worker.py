import sys
sys.path.append(r'E:\gRPCSample\python\proto')

import os
import network as net
import config as cfg
import config as cfg

if __name__ == '__main__':
    current_path = os.path.dirname(os.path.realpath(__file__)).replace("\\", "/")
    conf = cfg.get_config(path=current_path)

    worker_config = conf["server"]["worker"]
    worker_addr = worker_config["addr"]
    worker_port = worker_config["port"]

    net.start_rpc_server(worker_addr, worker_port)
