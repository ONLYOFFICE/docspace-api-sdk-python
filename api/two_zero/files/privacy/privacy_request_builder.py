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
    from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_content_dto.system.int32 import Int32
    from .available.available_request_builder import AvailableRequestBuilder

class PrivacyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/@privacy
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PrivacyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/@privacy{?filterType*,searchInContent*,userIdOrGroupId*,withsubfolders*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[PrivacyRequestBuilderGetQueryParameters]] = None) -> Optional[int]:
        """
        Returns the detailed list of files and folders located in the "Private Room" section.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_content_dto.system.int32 import Int32

        return await self.request_adapter.send_primitive_async(request_info, "int", None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[PrivacyRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the detailed list of files and folders located in the "Private Room" section.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> PrivacyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PrivacyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PrivacyRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def available(self) -> AvailableRequestBuilder:
        """
        The available property
        """
        from .available.available_request_builder import AvailableRequestBuilder

        return AvailableRequestBuilder(self.request_adapter, self.path_parameters)
    
    from uuid import UUID

    @dataclass
    class PrivacyRequestBuilderGetQueryParameters():
        from uuid import UUID

        """
        Returns the detailed list of files and folders located in the "Private Room" section.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "filter_type":
                return "filterType"
            if original_name == "search_in_content":
                return "searchInContent"
            if original_name == "user_id_or_group_id":
                return "userIdOrGroupId"
            if original_name == "withsubfolders":
                return "withsubfolders"
            return original_name
        
        # Filter type
        filter_type: Optional[int] = None

        # Specifies whether to return sections with or without subfolders
        search_in_content: Optional[bool] = None

        # User or group ID
        user_id_or_group_id: Optional[UUID] = None

        # Specifies whether to return sections with or without subfolders
        withsubfolders: Optional[bool] = None

    
    @dataclass
    class PrivacyRequestBuilderGetRequestConfiguration(RequestConfiguration[PrivacyRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

