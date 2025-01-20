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
    from .file.file_request_builder import FileRequestBuilder
    from .html.html_request_builder import HtmlRequestBuilder
    from .insert.insert_request_builder import InsertRequestBuilder
    from .text.text_request_builder import TextRequestBuilder
    from .upload.upload_request_builder import UploadRequestBuilder

class MyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/@my
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/@my{?applyFilterOption*,filterType*,searchInContent*,userIdOrGroupId*,withsubfolders*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MyRequestBuilderGetQueryParameters]] = None) -> Optional[int]:
        """
        Returns the detailed list of files and folders located in the "My documents" section.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_content_dto.system.int32 import Int32

        return await self.request_adapter.send_async(request_info, Int32, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MyRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the detailed list of files and folders located in the "My documents" section.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> MyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MyRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def file(self) -> FileRequestBuilder:
        """
        The file property
        """
        from .file.file_request_builder import FileRequestBuilder

        return FileRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def html(self) -> HtmlRequestBuilder:
        """
        The html property
        """
        from .html.html_request_builder import HtmlRequestBuilder

        return HtmlRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def insert(self) -> InsertRequestBuilder:
        """
        The insert property
        """
        from .insert.insert_request_builder import InsertRequestBuilder

        return InsertRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def text(self) -> TextRequestBuilder:
        """
        The text property
        """
        from .text.text_request_builder import TextRequestBuilder

        return TextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def upload(self) -> UploadRequestBuilder:
        """
        The upload property
        """
        from .upload.upload_request_builder import UploadRequestBuilder

        return UploadRequestBuilder(self.request_adapter, self.path_parameters)
    
    from uuid import UUID

    @dataclass
    class MyRequestBuilderGetQueryParameters():
        from uuid import UUID

        """
        Returns the detailed list of files and folders located in the "My documents" section.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "apply_filter_option":
                return "applyFilterOption"
            if original_name == "filter_type":
                return "filterType"
            if original_name == "search_in_content":
                return "searchInContent"
            if original_name == "user_id_or_group_id":
                return "userIdOrGroupId"
            if original_name == "withsubfolders":
                return "withsubfolders"
            return original_name
        
        # Specifies whether to return only files, only folders or all elements from the specified folder
        apply_filter_option: Optional[int] = None

        # Filter type
        filter_type: Optional[int] = None

        # Specifies whether to return sections with or without subfolders
        search_in_content: Optional[bool] = None

        # User or group ID
        user_id_or_group_id: Optional[UUID] = None

        # Specifies whether to return sections with or without subfolders
        withsubfolders: Optional[bool] = None

    
    @dataclass
    class MyRequestBuilderGetRequestConfiguration(RequestConfiguration[MyRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

