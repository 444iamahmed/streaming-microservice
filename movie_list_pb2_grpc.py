# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import movie_list_pb2 as movie__list__pb2


class ListStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetList = channel.unary_unary(
                '/List/GetList',
                request_serializer=movie__list__pb2.MovieListRequest.SerializeToString,
                response_deserializer=movie__list__pb2.MovieListResponse.FromString,
                )
        self.AddToList = channel.unary_unary(
                '/List/AddToList',
                request_serializer=movie__list__pb2.ListItem.SerializeToString,
                response_deserializer=movie__list__pb2.BoolValue.FromString,
                )
        self.RemoveFromList = channel.unary_unary(
                '/List/RemoveFromList',
                request_serializer=movie__list__pb2.ListItem.SerializeToString,
                response_deserializer=movie__list__pb2.BoolValue.FromString,
                )


class ListServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddToList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveFromList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ListServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetList,
                    request_deserializer=movie__list__pb2.MovieListRequest.FromString,
                    response_serializer=movie__list__pb2.MovieListResponse.SerializeToString,
            ),
            'AddToList': grpc.unary_unary_rpc_method_handler(
                    servicer.AddToList,
                    request_deserializer=movie__list__pb2.ListItem.FromString,
                    response_serializer=movie__list__pb2.BoolValue.SerializeToString,
            ),
            'RemoveFromList': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveFromList,
                    request_deserializer=movie__list__pb2.ListItem.FromString,
                    response_serializer=movie__list__pb2.BoolValue.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'List', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class List(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/List/GetList',
            movie__list__pb2.MovieListRequest.SerializeToString,
            movie__list__pb2.MovieListResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddToList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/List/AddToList',
            movie__list__pb2.ListItem.SerializeToString,
            movie__list__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveFromList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/List/RemoveFromList',
            movie__list__pb2.ListItem.SerializeToString,
            movie__list__pb2.BoolValue.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
