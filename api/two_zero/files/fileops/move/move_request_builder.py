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
    from ......models.a_s_c.files.core.api_models.request_dto.batch_request_dto import BatchRequestDto
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_entry_dto import FileEntryDto
    from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto

class MoveRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/fileops/move
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MoveRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/fileops/move{?inDto*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[MoveRequestBuilderGetQueryParameters]] = None) -> Optional[FileEntryDto]:
        """
        Checks a batch of files and folders for conflicts when moving or copying them to the folder with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FileEntryDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_entry_dto import FileEntryDto

        return await self.request_adapter.send_async(request_info, FileEntryDto, None)
    
    async def put(self,body: BatchRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FileOperationDto]:
        """
        Moves all the selected files and folders to the folder with the ID specified in the request.
        param body: Request parameters for copying/moving files
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FileOperationDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto

        return await self.request_adapter.send_async(request_info, FileOperationDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[MoveRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Checks a batch of files and folders for conflicts when moving or copying them to the folder with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: BatchRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Moves all the selected files and folders to the folder with the ID specified in the request.
        param body: Request parameters for copying/moving files
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
    
    def with_url(self,raw_url: str) -> MoveRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MoveRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MoveRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MoveRequestBuilderGetQueryParameters():
        """
        Checks a batch of files and folders for conflicts when moving or copying them to the folder with the ID specified in the request.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "in_dto":
                return "inDto"
            return original_name
        
        # Request parameters for copying/moving files
        in_dto: Optional[str] = None

    
    @dataclass
    class MoveRequestBuilderGetRequestConfiguration(RequestConfiguration[MoveRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MoveRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

