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
    from ......models.a_s_c.files.core.api_models.request_dto.delete_room_request import DeleteRoomRequest
    from ......models.a_s_c.files.core.api_models.request_dto.update_room_request import UpdateRoomRequest
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32
    from .archive.archive_request_builder import ArchiveRequestBuilder
    from .cover.cover_request_builder import CoverRequestBuilder
    from .indexexport.indexexport_request_builder import IndexexportRequestBuilder
    from .link.link_request_builder import LinkRequestBuilder
    from .links.links_request_builder import LinksRequestBuilder
    from .logo.logo_request_builder import LogoRequestBuilder
    from .news.news_request_builder import NewsRequestBuilder
    from .pin.pin_request_builder import PinRequestBuilder
    from .reorder.reorder_request_builder import ReorderRequestBuilder
    from .resend.resend_request_builder import ResendRequestBuilder
    from .share.share_request_builder import ShareRequestBuilder
    from .tags.tags_request_builder import TagsRequestBuilder
    from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder
    from .unpin.unpin_request_builder import UnpinRequestBuilder

class RoomsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/rooms/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RoomsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/rooms/{id}", path_parameters)
    
    async def delete(self,body: DeleteRoomRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FileOperationDto]:
        """
        Removes a room with the ID specified in the request.
        param body: Parameters for deleting a room
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
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Returns the room information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    async def put(self,body: UpdateRoomRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Renames a room with the ID specified in  the request.
        param body: Parameters for updating a room
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
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    def to_delete_request_information(self,body: DeleteRoomRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes a room with the ID specified in the request.
        param body: Parameters for deleting a room
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
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the room information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: UpdateRoomRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Renames a room with the ID specified in  the request.
        param body: Parameters for updating a room
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
    
    def with_url(self,raw_url: str) -> RoomsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RoomsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RoomsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def archive(self) -> ArchiveRequestBuilder:
        """
        The archive property
        """
        from .archive.archive_request_builder import ArchiveRequestBuilder

        return ArchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cover(self) -> CoverRequestBuilder:
        """
        The cover property
        """
        from .cover.cover_request_builder import CoverRequestBuilder

        return CoverRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def indexexport(self) -> IndexexportRequestBuilder:
        """
        The indexexport property
        """
        from .indexexport.indexexport_request_builder import IndexexportRequestBuilder

        return IndexexportRequestBuilder(self.request_adapter, self.path_parameters)
    
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
    def logo(self) -> LogoRequestBuilder:
        """
        The logo property
        """
        from .logo.logo_request_builder import LogoRequestBuilder

        return LogoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def news(self) -> NewsRequestBuilder:
        """
        The news property
        """
        from .news.news_request_builder import NewsRequestBuilder

        return NewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def pin(self) -> PinRequestBuilder:
        """
        The pin property
        """
        from .pin.pin_request_builder import PinRequestBuilder

        return PinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reorder(self) -> ReorderRequestBuilder:
        """
        The reorder property
        """
        from .reorder.reorder_request_builder import ReorderRequestBuilder

        return ReorderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resend(self) -> ResendRequestBuilder:
        """
        The resend property
        """
        from .resend.resend_request_builder import ResendRequestBuilder

        return ResendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def share(self) -> ShareRequestBuilder:
        """
        The share property
        """
        from .share.share_request_builder import ShareRequestBuilder

        return ShareRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tags(self) -> TagsRequestBuilder:
        """
        The tags property
        """
        from .tags.tags_request_builder import TagsRequestBuilder

        return TagsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unarchive(self) -> UnarchiveRequestBuilder:
        """
        The unarchive property
        """
        from .unarchive.unarchive_request_builder import UnarchiveRequestBuilder

        return UnarchiveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unpin(self) -> UnpinRequestBuilder:
        """
        The unpin property
        """
        from .unpin.unpin_request_builder import UnpinRequestBuilder

        return UnpinRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RoomsItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RoomsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RoomsItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

