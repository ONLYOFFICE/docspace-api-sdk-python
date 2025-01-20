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
    from ......models.a_s_c.files.core.api_models.request_dto.create_folder import CreateFolder
    from ......models.a_s_c.files.core.api_models.request_dto.delete_folder import DeleteFolder
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32
    from .link.link_request_builder import LinkRequestBuilder
    from .log.log_request_builder import LogRequestBuilder
    from .order.order_request_builder import OrderRequestBuilder
    from .path.path_request_builder import PathRequestBuilder

class FolderItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/folder/{folder-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FolderItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/folder/{folder%2Did}", path_parameters)
    
    async def delete(self,body: DeleteFolder, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FileOperationDto]:
        """
        Deletes a folder with the ID specified in the request.
        param body: Parameters for deleting a folder
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
        from models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto

        return await self.request_adapter.send_async(request_info, FileOperationDto, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Returns the detailed information about a folder with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[int]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_async(request_info, Int32, None)
    
    async def post(self,body: CreateFolder, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Creates a new folder with the title specified in the request. The parent folder ID can be also specified.
        param body: Parameters for creating a folder: Title (string) - new folder title
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
        from models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_async(request_info, Int32, None)
    
    async def put(self,body: CreateFolder, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[int]:
        """
        Renames the selected folder with a new title specified in the request.
        param body: Parameters for creating a folder: Title (string) - new folder title
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
        from models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.int32 import Int32

        return await self.request_adapter.send_async(request_info, Int32, None)
    
    def to_delete_request_information(self,body: DeleteFolder, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a folder with the ID specified in the request.
        param body: Parameters for deleting a folder
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
        Returns the detailed information about a folder with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: CreateFolder, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new folder with the title specified in the request. The parent folder ID can be also specified.
        param body: Parameters for creating a folder: Title (string) - new folder title
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
    
    def to_put_request_information(self,body: CreateFolder, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Renames the selected folder with a new title specified in the request.
        param body: Parameters for creating a folder: Title (string) - new folder title
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
    
    def with_url(self,raw_url: str) -> FolderItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FolderItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FolderItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def link(self) -> LinkRequestBuilder:
        """
        The link property
        """
        from .link.link_request_builder import LinkRequestBuilder

        return LinkRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def log(self) -> LogRequestBuilder:
        """
        The log property
        """
        from .log.log_request_builder import LogRequestBuilder

        return LogRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def order(self) -> OrderRequestBuilder:
        """
        The order property
        """
        from .order.order_request_builder import OrderRequestBuilder

        return OrderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def path(self) -> PathRequestBuilder:
        """
        The path property
        """
        from .path.path_request_builder import PathRequestBuilder

        return PathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FolderItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FolderItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FolderItemRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FolderItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

