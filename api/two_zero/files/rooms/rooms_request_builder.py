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
    from .....models.a_s_c.files.core.api_models.request_dto.create_room_request_dto import CreateRoomRequestDto
    from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_content_dto.system.int32 import Int32
    from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32
    from .covers.covers_request_builder import CoversRequestBuilder
    from .indexexport.indexexport_request_builder import IndexexportRequestBuilder
    from .item.rooms_item_request_builder import RoomsItemRequestBuilder
    from .news.news_request_builder import NewsRequestBuilder
    from .resetquota.resetquota_request_builder import ResetquotaRequestBuilder
    from .roomquota.roomquota_request_builder import RoomquotaRequestBuilder
    from .thirdparty.thirdparty_request_builder import ThirdpartyRequestBuilder

class RoomsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/rooms
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RoomsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/rooms{?excludeSubject*,provider*,quotaFilter*,searchArea*,searchInContent*,storageFilter*,subjectFilter*,subjectId*,tags*,type,withSubfolders*,withoutTags*}", path_parameters)
    
    def by_id(self,id: int) -> RoomsItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.files.rooms.item collection
        param id: Room Id
        Returns: RoomsItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.rooms_item_request_builder import RoomsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return RoomsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RoomsRequestBuilderGetQueryParameters]] = None) -> Optional[int]:
        """
        Returns the contents of the "Rooms" section by the parameters specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_content_dto.system.int32 import Int32
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    async def post(self,body: CreateRoomRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Creates a room in the "Rooms" section.
        param body: Request parameters for creating a room
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_content_dto.system.int32 import Int32
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RoomsRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the contents of the "Rooms" section by the parameters specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: CreateRoomRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a room in the "Rooms" section.
        param body: Request parameters for creating a room
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> RoomsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RoomsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RoomsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def covers(self) -> CoversRequestBuilder:
        """
        The covers property
        """
        from .covers.covers_request_builder import CoversRequestBuilder

        return CoversRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def indexexport(self) -> IndexexportRequestBuilder:
        """
        The indexexport property
        """
        from .indexexport.indexexport_request_builder import IndexexportRequestBuilder

        return IndexexportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def news(self) -> NewsRequestBuilder:
        """
        The news property
        """
        from .news.news_request_builder import NewsRequestBuilder

        return NewsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resetquota(self) -> ResetquotaRequestBuilder:
        """
        The resetquota property
        """
        from .resetquota.resetquota_request_builder import ResetquotaRequestBuilder

        return ResetquotaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def roomquota(self) -> RoomquotaRequestBuilder:
        """
        The roomquota property
        """
        from .roomquota.roomquota_request_builder import RoomquotaRequestBuilder

        return RoomquotaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thirdparty(self) -> ThirdpartyRequestBuilder:
        """
        The thirdparty property
        """
        from .thirdparty.thirdparty_request_builder import ThirdpartyRequestBuilder

        return ThirdpartyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class RoomsRequestBuilderGetQueryParameters():
        """
        Returns the contents of the "Rooms" section by the parameters specified in the request.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "exclude_subject":
                return "excludeSubject"
            if original_name == "quota_filter":
                return "quotaFilter"
            if original_name == "search_area":
                return "searchArea"
            if original_name == "search_in_content":
                return "searchInContent"
            if original_name == "storage_filter":
                return "storageFilter"
            if original_name == "subject_filter":
                return "subjectFilter"
            if original_name == "subject_id":
                return "subjectId"
            if original_name == "without_tags":
                return "withoutTags"
            if original_name == "with_subfolders":
                return "withSubfolders"
            if original_name == "provider":
                return "provider"
            if original_name == "tags":
                return "tags"
            if original_name == "type":
                return "type"
            return original_name
        
        # Specifies whether to exclude a subject or not
        exclude_subject: Optional[bool] = None

        # Filter by provider name (None, Box, DropBox, GoogleDrive, kDrive, OneDrive, WebDav)
        provider: Optional[int] = None

        # Filter by quota (Default - 1, Custom - 2)
        quota_filter: Optional[int] = None

        # Room search area (Active, Archive, Any)
        search_area: Optional[int] = None

        # Specifies whether to search within the section contents or not
        search_in_content: Optional[bool] = None

        # Filter by storage (Internal - 1, ThirdParty - 2)
        storage_filter: Optional[int] = None

        # Filter by subject (Owner - 1, Member - 1)
        subject_filter: Optional[int] = None

        # Filter by user ID
        subject_id: Optional[str] = None

        # Tags in the serialized format
        tags: Optional[str] = None

        # Filter by room type
        type: Optional[List[int]] = None

        # Specifies whether to return sections with or without subfolders
        with_subfolders: Optional[bool] = None

        # Specifies whether to search by tags or not
        without_tags: Optional[bool] = None

    
    @dataclass
    class RoomsRequestBuilderGetRequestConfiguration(RequestConfiguration[RoomsRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class RoomsRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

