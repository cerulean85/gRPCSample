from service.Bee4Service import Bee4Service
import storage.service_rdb as service_rdb
from proto import bee4_pb2

class Bee4ServiceManager(Bee4Service):  
  
  '''
  Are You Idle ?
  '''  
  def are_you_idle(self):    
    stub = self.get_worker_stub()
    response = stub.AreYouIdle(bee4_pb2.EmptyParam())
    print(response)
    return response

  
  
  '''
  Deliver
  
  '''
  def deliver(self, feed = None):
    bot_board_records = service_rdb.get_bot_board_record()
    response = None
    for record in bot_board_records:

      if record.state == "idle":

        print(f"{record.idx}")
        stub = self.get_worker_stub()

        if feed == None:
          feed = bee4_pb2.Feed(
            no = record.idx, botType = record.type,
            script = "No Contents", botAnswer = "No Contents!")

        response = stub.Deliver(feed)
        break
    return response