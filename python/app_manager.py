import threading
import controller.bee4_manager_controller as manager_controller
import conf.service_config as service_conf

if __name__ == '__main__':
    threading.Thread(target=manager_controller.deliver_loop).start()
    manager_conf = service_conf.get_server_conf(target="manager")
    manager_addr = manager_conf["addr"]
    manager_port = manager_conf["port"]
    manager_controller.start_server(manager_addr, manager_port)

