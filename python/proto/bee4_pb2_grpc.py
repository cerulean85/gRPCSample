# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import bee4_pb2 as bee4__pb2


class Bee4ServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AreYouHealthy = channel.unary_unary(
                '/Bee4Service/AreYouHealthy',
                request_serializer=bee4__pb2.EmptyParam.SerializeToString,
                response_deserializer=bee4__pb2.NodeCondition.FromString,
                )
        self.AreYouIdle = channel.unary_unary(
                '/Bee4Service/AreYouIdle',
                request_serializer=bee4__pb2.EmptyParam.SerializeToString,
                response_deserializer=bee4__pb2.NodeCondition.FromString,
                )
        self.Deliver = channel.unary_unary(
                '/Bee4Service/Deliver',
                request_serializer=bee4__pb2.Feed.SerializeToString,
                response_deserializer=bee4__pb2.Feed.FromString,
                )


class Bee4ServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AreYouHealthy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AreYouIdle(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deliver(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Bee4ServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AreYouHealthy': grpc.unary_unary_rpc_method_handler(
                    servicer.AreYouHealthy,
                    request_deserializer=bee4__pb2.EmptyParam.FromString,
                    response_serializer=bee4__pb2.NodeCondition.SerializeToString,
            ),
            'AreYouIdle': grpc.unary_unary_rpc_method_handler(
                    servicer.AreYouIdle,
                    request_deserializer=bee4__pb2.EmptyParam.FromString,
                    response_serializer=bee4__pb2.NodeCondition.SerializeToString,
            ),
            'Deliver': grpc.unary_unary_rpc_method_handler(
                    servicer.Deliver,
                    request_deserializer=bee4__pb2.Feed.FromString,
                    response_serializer=bee4__pb2.Feed.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Bee4Service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Bee4Service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AreYouHealthy(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bee4Service/AreYouHealthy',
            bee4__pb2.EmptyParam.SerializeToString,
            bee4__pb2.NodeCondition.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AreYouIdle(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bee4Service/AreYouIdle',
            bee4__pb2.EmptyParam.SerializeToString,
            bee4__pb2.NodeCondition.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deliver(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Bee4Service/Deliver',
            bee4__pb2.Feed.SerializeToString,
            bee4__pb2.Feed.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
