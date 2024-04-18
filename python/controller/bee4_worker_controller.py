from service.Bee4ServiceWorker import *
service_worker = Bee4ServiceWorker()

"""
  Generate Answer about Question on feed.
"""
def generate_answer(feed):
  feed_doc = service_worker.get_feed_doc_from_dynamo(feed)
  bot = service_worker.get_generative_bot_module(feed_doc["bot_type"])
  answer = bot(feed_doc["question"])
  return answer