
import proto.bee4_pb2
import proto.bee4_pb2_grpc

class Bee4Service(proto.bee4_pb2_grpc.Bee4ServiceServicer):

  def AreYouIdle(self, request, context):
    print("AreYouIdel?")
    return proto.bee4_pb2.NodeCondition(idle=True)
  
  def Deliver(self, request, context):

    print(request.no)
    print(request.botType)
    print(request.script)
    print(request.botAnswer)

    return proto.bee4_pb2.Feed(
      no = 1,
      botType = "chatgpt",
      script = "This is Script.",
      botAnswer = "Nothing"
    )