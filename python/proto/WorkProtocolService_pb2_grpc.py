# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import WorkProtocolService_pb2 as WorkProtocolService__pb2


class WorkProtocolServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.echo = channel.unary_unary(
                '/net.kkennib.grpc.WorkProtocolService/echo',
                request_serializer=WorkProtocolService__pb2.Works.SerializeToString,
                response_deserializer=WorkProtocolService__pb2.Works.FromString,
                )
        self.collectUrls = channel.unary_unary(
                '/net.kkennib.grpc.WorkProtocolService/collectUrls',
                request_serializer=WorkProtocolService__pb2.Works.SerializeToString,
                response_deserializer=WorkProtocolService__pb2.WorkResponse.FromString,
                )
        self.collectDocs = channel.unary_unary(
                '/net.kkennib.grpc.WorkProtocolService/collectDocs',
                request_serializer=WorkProtocolService__pb2.Works.SerializeToString,
                response_deserializer=WorkProtocolService__pb2.WorkResponse.FromString,
                )
        self.extractTexts = channel.unary_unary(
                '/net.kkennib.grpc.WorkProtocolService/extractTexts',
                request_serializer=WorkProtocolService__pb2.Works.SerializeToString,
                response_deserializer=WorkProtocolService__pb2.WorkResponse.FromString,
                )
        self.extractContents = channel.unary_unary(
                '/net.kkennib.grpc.WorkProtocolService/extractContents',
                request_serializer=WorkProtocolService__pb2.Works.SerializeToString,
                response_deserializer=WorkProtocolService__pb2.WorkResponse.FromString,
                )
        self.request = channel.unary_unary(
                '/net.kkennib.grpc.WorkProtocolService/request',
                request_serializer=WorkProtocolService__pb2.Works.SerializeToString,
                response_deserializer=WorkProtocolService__pb2.Works.FromString,
                )


class WorkProtocolServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def echo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def collectUrls(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def collectDocs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def extractTexts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def extractContents(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def request(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_WorkProtocolServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'echo': grpc.unary_unary_rpc_method_handler(
                    servicer.echo,
                    request_deserializer=WorkProtocolService__pb2.Works.FromString,
                    response_serializer=WorkProtocolService__pb2.Works.SerializeToString,
            ),
            'collectUrls': grpc.unary_unary_rpc_method_handler(
                    servicer.collectUrls,
                    request_deserializer=WorkProtocolService__pb2.Works.FromString,
                    response_serializer=WorkProtocolService__pb2.WorkResponse.SerializeToString,
            ),
            'collectDocs': grpc.unary_unary_rpc_method_handler(
                    servicer.collectDocs,
                    request_deserializer=WorkProtocolService__pb2.Works.FromString,
                    response_serializer=WorkProtocolService__pb2.WorkResponse.SerializeToString,
            ),
            'extractTexts': grpc.unary_unary_rpc_method_handler(
                    servicer.extractTexts,
                    request_deserializer=WorkProtocolService__pb2.Works.FromString,
                    response_serializer=WorkProtocolService__pb2.WorkResponse.SerializeToString,
            ),
            'extractContents': grpc.unary_unary_rpc_method_handler(
                    servicer.extractContents,
                    request_deserializer=WorkProtocolService__pb2.Works.FromString,
                    response_serializer=WorkProtocolService__pb2.WorkResponse.SerializeToString,
            ),
            'request': grpc.unary_unary_rpc_method_handler(
                    servicer.request,
                    request_deserializer=WorkProtocolService__pb2.Works.FromString,
                    response_serializer=WorkProtocolService__pb2.Works.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'net.kkennib.grpc.WorkProtocolService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class WorkProtocolService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def echo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.kkennib.grpc.WorkProtocolService/echo',
            WorkProtocolService__pb2.Works.SerializeToString,
            WorkProtocolService__pb2.Works.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def collectUrls(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.kkennib.grpc.WorkProtocolService/collectUrls',
            WorkProtocolService__pb2.Works.SerializeToString,
            WorkProtocolService__pb2.WorkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def collectDocs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.kkennib.grpc.WorkProtocolService/collectDocs',
            WorkProtocolService__pb2.Works.SerializeToString,
            WorkProtocolService__pb2.WorkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def extractTexts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.kkennib.grpc.WorkProtocolService/extractTexts',
            WorkProtocolService__pb2.Works.SerializeToString,
            WorkProtocolService__pb2.WorkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def extractContents(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.kkennib.grpc.WorkProtocolService/extractContents',
            WorkProtocolService__pb2.Works.SerializeToString,
            WorkProtocolService__pb2.WorkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def request(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/net.kkennib.grpc.WorkProtocolService/request',
            WorkProtocolService__pb2.Works.SerializeToString,
            WorkProtocolService__pb2.Works.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
