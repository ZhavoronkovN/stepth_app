# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import stepth_pb2 as stepth__pb2


class StepthServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Beep = channel.unary_unary(
                '/stepth_service.StepthService/Beep',
                request_serializer=stepth__pb2.EmptyRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.LoadImage = channel.unary_stream(
                '/stepth_service.StepthService/LoadImage',
                request_serializer=stepth__pb2.LoadImageRequest.SerializeToString,
                response_deserializer=stepth__pb2.ImageResponse.FromString,
                )
        self.LoadImageToCurrent = channel.unary_stream(
                '/stepth_service.StepthService/LoadImageToCurrent',
                request_serializer=stepth__pb2.LoadImageRequest.SerializeToString,
                response_deserializer=stepth__pb2.ImageResponse.FromString,
                )
        self.LoadDepth = channel.unary_unary(
                '/stepth_service.StepthService/LoadDepth',
                request_serializer=stepth__pb2.LoadImageRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.LoadDepthFromAdditional = channel.unary_unary(
                '/stepth_service.StepthService/LoadDepthFromAdditional',
                request_serializer=stepth__pb2.LoadImageRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.HighlightDepth = channel.unary_stream(
                '/stepth_service.StepthService/HighlightDepth',
                request_serializer=stepth__pb2.HighlightRequest.SerializeToString,
                response_deserializer=stepth__pb2.ImageResponse.FromString,
                )
        self.InvertDepth = channel.unary_unary(
                '/stepth_service.StepthService/InvertDepth',
                request_serializer=stepth__pb2.EmptyRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.HighlightMask = channel.unary_stream(
                '/stepth_service.StepthService/HighlightMask',
                request_serializer=stepth__pb2.HighlightRequest.SerializeToString,
                response_deserializer=stepth__pb2.ImageResponse.FromString,
                )
        self.InvertMask = channel.unary_unary(
                '/stepth_service.StepthService/InvertMask',
                request_serializer=stepth__pb2.EmptyRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.CutDepth = channel.unary_unary(
                '/stepth_service.StepthService/CutDepth',
                request_serializer=stepth__pb2.CutDepthRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.ImageMod = channel.unary_stream(
                '/stepth_service.StepthService/ImageMod',
                request_serializer=stepth__pb2.ImageModRequest.SerializeToString,
                response_deserializer=stepth__pb2.ImageResponse.FromString,
                )
        self.SaveImage = channel.unary_unary(
                '/stepth_service.StepthService/SaveImage',
                request_serializer=stepth__pb2.ImageSaveRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.SaveDepth = channel.unary_unary(
                '/stepth_service.StepthService/SaveDepth',
                request_serializer=stepth__pb2.ImageSaveRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )
        self.SaveMask = channel.unary_unary(
                '/stepth_service.StepthService/SaveMask',
                request_serializer=stepth__pb2.ImageSaveRequest.SerializeToString,
                response_deserializer=stepth__pb2.StringResponse.FromString,
                )


class StepthServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Beep(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadImageToCurrent(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadDepth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def LoadDepthFromAdditional(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HighlightDepth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvertDepth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HighlightMask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InvertMask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CutDepth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ImageMod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveDepth(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveMask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_StepthServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Beep': grpc.unary_unary_rpc_method_handler(
                    servicer.Beep,
                    request_deserializer=stepth__pb2.EmptyRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'LoadImage': grpc.unary_stream_rpc_method_handler(
                    servicer.LoadImage,
                    request_deserializer=stepth__pb2.LoadImageRequest.FromString,
                    response_serializer=stepth__pb2.ImageResponse.SerializeToString,
            ),
            'LoadImageToCurrent': grpc.unary_stream_rpc_method_handler(
                    servicer.LoadImageToCurrent,
                    request_deserializer=stepth__pb2.LoadImageRequest.FromString,
                    response_serializer=stepth__pb2.ImageResponse.SerializeToString,
            ),
            'LoadDepth': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadDepth,
                    request_deserializer=stepth__pb2.LoadImageRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'LoadDepthFromAdditional': grpc.unary_unary_rpc_method_handler(
                    servicer.LoadDepthFromAdditional,
                    request_deserializer=stepth__pb2.LoadImageRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'HighlightDepth': grpc.unary_stream_rpc_method_handler(
                    servicer.HighlightDepth,
                    request_deserializer=stepth__pb2.HighlightRequest.FromString,
                    response_serializer=stepth__pb2.ImageResponse.SerializeToString,
            ),
            'InvertDepth': grpc.unary_unary_rpc_method_handler(
                    servicer.InvertDepth,
                    request_deserializer=stepth__pb2.EmptyRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'HighlightMask': grpc.unary_stream_rpc_method_handler(
                    servicer.HighlightMask,
                    request_deserializer=stepth__pb2.HighlightRequest.FromString,
                    response_serializer=stepth__pb2.ImageResponse.SerializeToString,
            ),
            'InvertMask': grpc.unary_unary_rpc_method_handler(
                    servicer.InvertMask,
                    request_deserializer=stepth__pb2.EmptyRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'CutDepth': grpc.unary_unary_rpc_method_handler(
                    servicer.CutDepth,
                    request_deserializer=stepth__pb2.CutDepthRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'ImageMod': grpc.unary_stream_rpc_method_handler(
                    servicer.ImageMod,
                    request_deserializer=stepth__pb2.ImageModRequest.FromString,
                    response_serializer=stepth__pb2.ImageResponse.SerializeToString,
            ),
            'SaveImage': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveImage,
                    request_deserializer=stepth__pb2.ImageSaveRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'SaveDepth': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveDepth,
                    request_deserializer=stepth__pb2.ImageSaveRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
            'SaveMask': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveMask,
                    request_deserializer=stepth__pb2.ImageSaveRequest.FromString,
                    response_serializer=stepth__pb2.StringResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'stepth_service.StepthService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class StepthService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Beep(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/Beep',
            stepth__pb2.EmptyRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stepth_service.StepthService/LoadImage',
            stepth__pb2.LoadImageRequest.SerializeToString,
            stepth__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadImageToCurrent(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stepth_service.StepthService/LoadImageToCurrent',
            stepth__pb2.LoadImageRequest.SerializeToString,
            stepth__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadDepth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/LoadDepth',
            stepth__pb2.LoadImageRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def LoadDepthFromAdditional(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/LoadDepthFromAdditional',
            stepth__pb2.LoadImageRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HighlightDepth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stepth_service.StepthService/HighlightDepth',
            stepth__pb2.HighlightRequest.SerializeToString,
            stepth__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvertDepth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/InvertDepth',
            stepth__pb2.EmptyRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HighlightMask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stepth_service.StepthService/HighlightMask',
            stepth__pb2.HighlightRequest.SerializeToString,
            stepth__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InvertMask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/InvertMask',
            stepth__pb2.EmptyRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CutDepth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/CutDepth',
            stepth__pb2.CutDepthRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ImageMod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/stepth_service.StepthService/ImageMod',
            stepth__pb2.ImageModRequest.SerializeToString,
            stepth__pb2.ImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/SaveImage',
            stepth__pb2.ImageSaveRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveDepth(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/SaveDepth',
            stepth__pb2.ImageSaveRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveMask(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/stepth_service.StepthService/SaveMask',
            stepth__pb2.ImageSaveRequest.SerializeToString,
            stepth__pb2.StringResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)