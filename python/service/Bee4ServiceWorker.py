import Bee4Service
import storage.service_rdb as service_rdb
from proto import bee4_pb2

class Bee4ServiceWorker(Bee4Service):  
  
  """
    Read DynamoDB Feed Contents
  """
  def get_feed_doc_from_dynamo(self, feed):
    pass
    

  def get_generative_bot_module(self, bot_type):
    modules = {
      "chat_gpt": self.run_chat_gpt,
      "gemini": self.run_gemini
    }
    return modules[bot_type]

  def run_chat_gpt(self, question):
    pass

  def run_gemini(self, question):
    pass