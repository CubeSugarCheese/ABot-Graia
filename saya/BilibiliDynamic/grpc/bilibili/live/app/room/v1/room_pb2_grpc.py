# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import room_pb2 as room__pb2


class StudioListStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetStudioList = channel.unary_unary(
                '/bilibili.live.app.room.v1.StudioList/GetStudioList',
                request_serializer=room__pb2.GetStudioListReq.SerializeToString,
                response_deserializer=room__pb2.GetStudioListResp.FromString,
                )


class StudioListServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetStudioList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StudioListServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetStudioList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetStudioList,
                    request_deserializer=room__pb2.GetStudioListReq.FromString,
                    response_serializer=room__pb2.GetStudioListResp.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'bilibili.live.app.room.v1.StudioList', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StudioList(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetStudioList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/bilibili.live.app.room.v1.StudioList/GetStudioList',
            room__pb2.GetStudioListReq.SerializeToString,
            room__pb2.GetStudioListResp.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
