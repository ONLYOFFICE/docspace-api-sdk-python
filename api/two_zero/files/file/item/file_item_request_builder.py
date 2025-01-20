from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.a_s_c.files.core.api_models.request_dto.delete import Delete
    from ......models.a_s_c.files.core.api_models.request_dto.update_file import UpdateFile
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_dto.system.int32 import Int32
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto
    from .checkconversion.checkconversion_request_builder import CheckconversionRequestBuilder
    from .comment.comment_request_builder import CommentRequestBuilder
    from .copyas.copyas_request_builder import CopyasRequestBuilder
    from .edit.edit_request_builder import EditRequestBuilder
    from .edit_session.edit_session_request_builder import Edit_sessionRequestBuilder
    from .history.history_request_builder import HistoryRequestBuilder
    from .isformpdf.isformpdf_request_builder import IsformpdfRequestBuilder
    from .link.link_request_builder import LinkRequestBuilder
    from .links.links_request_builder import LinksRequestBuilder
    from .lock.lock_request_builder import LockRequestBuilder
    from .log.log_request_builder import LogRequestBuilder
    from .openedit.openedit_request_builder import OpeneditRequestBuilder
    from .presigned.presigned_request_builder import PresignedRequestBuilder
    from .presigneduri.presigneduri_request_builder import PresigneduriRequestBuilder
    from .protectusers.protectusers_request_builder import ProtectusersRequestBuilder
    from .restoreversion.restoreversion_request_builder import RestoreversionRequestBuilder
    from .saveaspdf.saveaspdf_request_builder import SaveaspdfRequestBuilder
    from .saveediting.saveediting_request_builder import SaveeditingRequestBuilder
    from .startedit.startedit_request_builder import StarteditRequestBuilder
    from .startfilling.startfilling_request_builder import StartfillingRequestBuilder
    from .trackeditfile.trackeditfile_request_builder import TrackeditfileRequestBuilder

class FileItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/file/{file-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FileItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/file/{file%2Did}{?version*}", path_parameters)
    
    async def delete(self,body: Delete, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FileOperationDto]:
        """
        Deletes a file with the ID specified in the request.
        param body: Parameters for deleting a file
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FileOperationDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto

        return await self.request_adapter.send_async(request_info, FileOperationDto, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FileItemRequestBuilderGetQueryParameters]] = None) -> Optional[int]:
        """
        Returns the detailed information about a file with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    async def put(self,body: UpdateFile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Updates the information of the selected file with the parameters specified in the request.
        param body: Parameters for updating a file
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    def to_delete_request_information(self,body: Delete, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a file with the ID specified in the request.
        param body: Parameters for deleting a file
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FileItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the detailed information about a file with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: UpdateFile, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the information of the selected file with the parameters specified in the request.
        param body: Parameters for updating a file
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> FileItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FileItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FileItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def checkconversion(self) -> CheckconversionRequestBuilder:
        """
        The checkconversion property
        """
        from .checkconversion.checkconversion_request_builder import CheckconversionRequestBuilder

        return CheckconversionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def comment(self) -> CommentRequestBuilder:
        """
        The comment property
        """
        from .comment.comment_request_builder import CommentRequestBuilder

        return CommentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copyas(self) -> CopyasRequestBuilder:
        """
        The copyas property
        """
        from .copyas.copyas_request_builder import CopyasRequestBuilder

        return CopyasRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edit(self) -> EditRequestBuilder:
        """
        The edit property
        """
        from .edit.edit_request_builder import EditRequestBuilder

        return EditRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def edit_session(self) -> Edit_sessionRequestBuilder:
        """
        The edit_session property
        """
        from .edit_session.edit_session_request_builder import Edit_sessionRequestBuilder

        return Edit_sessionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def history(self) -> HistoryRequestBuilder:
        """
        The history property
        """
        from .history.history_request_builder import HistoryRequestBuilder

        return HistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def isformpdf(self) -> IsformpdfRequestBuilder:
        """
        The isformpdf property
        """
        from .isformpdf.isformpdf_request_builder import IsformpdfRequestBuilder

        return IsformpdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def link(self) -> LinkRequestBuilder:
        """
        The link property
        """
        from .link.link_request_builder import LinkRequestBuilder

        return LinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def links(self) -> LinksRequestBuilder:
        """
        The links property
        """
        from .links.links_request_builder import LinksRequestBuilder

        return LinksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def lock(self) -> LockRequestBuilder:
        """
        The lock property
        """
        from .lock.lock_request_builder import LockRequestBuilder

        return LockRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log(self) -> LogRequestBuilder:
        """
        The log property
        """
        from .log.log_request_builder import LogRequestBuilder

        return LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def openedit(self) -> OpeneditRequestBuilder:
        """
        The openedit property
        """
        from .openedit.openedit_request_builder import OpeneditRequestBuilder

        return OpeneditRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presigned(self) -> PresignedRequestBuilder:
        """
        The presigned property
        """
        from .presigned.presigned_request_builder import PresignedRequestBuilder

        return PresignedRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def presigneduri(self) -> PresigneduriRequestBuilder:
        """
        The presigneduri property
        """
        from .presigneduri.presigneduri_request_builder import PresigneduriRequestBuilder

        return PresigneduriRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def protectusers(self) -> ProtectusersRequestBuilder:
        """
        The protectusers property
        """
        from .protectusers.protectusers_request_builder import ProtectusersRequestBuilder

        return ProtectusersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restoreversion(self) -> RestoreversionRequestBuilder:
        """
        The restoreversion property
        """
        from .restoreversion.restoreversion_request_builder import RestoreversionRequestBuilder

        return RestoreversionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def saveaspdf(self) -> SaveaspdfRequestBuilder:
        """
        The saveaspdf property
        """
        from .saveaspdf.saveaspdf_request_builder import SaveaspdfRequestBuilder

        return SaveaspdfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def saveediting(self) -> SaveeditingRequestBuilder:
        """
        The saveediting property
        """
        from .saveediting.saveediting_request_builder import SaveeditingRequestBuilder

        return SaveeditingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startedit(self) -> StarteditRequestBuilder:
        """
        The startedit property
        """
        from .startedit.startedit_request_builder import StarteditRequestBuilder

        return StarteditRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startfilling(self) -> StartfillingRequestBuilder:
        """
        The startfilling property
        """
        from .startfilling.startfilling_request_builder import StartfillingRequestBuilder

        return StartfillingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def trackeditfile(self) -> TrackeditfileRequestBuilder:
        """
        The trackeditfile property
        """
        from .trackeditfile.trackeditfile_request_builder import TrackeditfileRequestBuilder

        return TrackeditfileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FileItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FileItemRequestBuilderGetQueryParameters():
        """
        Returns the detailed information about a file with the ID specified in the request.
        """
        # File version
        version: Optional[int] = None

    
    @dataclass
    class FileItemRequestBuilderGetRequestConfiguration(RequestConfiguration[FileItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FileItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

