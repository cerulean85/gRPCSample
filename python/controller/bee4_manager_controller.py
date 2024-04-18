from service.Bee4ServiceManager import *
import time

service_manager = Bee4ServiceManager()

def are_you_idle():
    response = service_manager.are_you_idle()
    return response

def deliver_loop():
  while True:
    response = service_manager.deliver()
    print(response)
    time.sleep(3)

def start_server(addr, port):
  service_manager.start_service(addr, port)
