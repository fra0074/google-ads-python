# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.ads.google_ads.v6.proto.resources import media_file_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_media__file__pb2
from google.ads.google_ads.v6.proto.services import media_file_service_pb2 as google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2


class MediaFileServiceStub(object):
    """Proto file describing the Media File service.

    Service to manage media files.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetMediaFile = channel.unary_unary(
                '/google.ads.googleads.v6.services.MediaFileService/GetMediaFile',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.GetMediaFileRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_media__file__pb2.MediaFile.FromString,
                )
        self.MutateMediaFiles = channel.unary_unary(
                '/google.ads.googleads.v6.services.MediaFileService/MutateMediaFiles',
                request_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.MutateMediaFilesRequest.SerializeToString,
                response_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.MutateMediaFilesResponse.FromString,
                )


class MediaFileServiceServicer(object):
    """Proto file describing the Media File service.

    Service to manage media files.
    """

    def GetMediaFile(self, request, context):
        """Returns the requested media file in full detail.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def MutateMediaFiles(self, request, context):
        """Creates media files. Operation statuses are returned.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MediaFileServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetMediaFile': grpc.unary_unary_rpc_method_handler(
                    servicer.GetMediaFile,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.GetMediaFileRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_media__file__pb2.MediaFile.SerializeToString,
            ),
            'MutateMediaFiles': grpc.unary_unary_rpc_method_handler(
                    servicer.MutateMediaFiles,
                    request_deserializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.MutateMediaFilesRequest.FromString,
                    response_serializer=google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.MutateMediaFilesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'google.ads.googleads.v6.services.MediaFileService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MediaFileService(object):
    """Proto file describing the Media File service.

    Service to manage media files.
    """

    @staticmethod
    def GetMediaFile(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.MediaFileService/GetMediaFile',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.GetMediaFileRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_resources_dot_media__file__pb2.MediaFile.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def MutateMediaFiles(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/google.ads.googleads.v6.services.MediaFileService/MutateMediaFiles',
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.MutateMediaFilesRequest.SerializeToString,
            google_dot_ads_dot_googleads_dot_v6_dot_services_dot_media__file__service__pb2.MutateMediaFilesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
