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
    from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto
    from .bulkdownload.bulkdownload_request_builder import BulkdownloadRequestBuilder
    from .checkdestfolder.checkdestfolder_request_builder import CheckdestfolderRequestBuilder
    from .copy.copy_request_builder import CopyRequestBuilder
    from .delete.delete_request_builder import DeleteRequestBuilder
    from .duplicate.duplicate_request_builder import DuplicateRequestBuilder
    from .emptytrash.emptytrash_request_builder import EmptytrashRequestBuilder
    from .markasread.markasread_request_builder import MarkasreadRequestBuilder
    from .move.move_request_builder import MoveRequestBuilder
    from .terminate.terminate_request_builder import TerminateRequestBuilder

class FileopsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/fileops
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FileopsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/fileops", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FileOperationDto]:
        """
        Returns a list of all the active operations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FileOperationDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.file_operation_dto import FileOperationDto

        return await self.request_adapter.send_async(request_info, FileOperationDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of all the active operations.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> FileopsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FileopsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FileopsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def bulkdownload(self) -> BulkdownloadRequestBuilder:
        """
        The bulkdownload property
        """
        from .bulkdownload.bulkdownload_request_builder import BulkdownloadRequestBuilder

        return BulkdownloadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def checkdestfolder(self) -> CheckdestfolderRequestBuilder:
        """
        The checkdestfolder property
        """
        from .checkdestfolder.checkdestfolder_request_builder import CheckdestfolderRequestBuilder

        return CheckdestfolderRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def copy(self) -> CopyRequestBuilder:
        """
        The copy property
        """
        from .copy.copy_request_builder import CopyRequestBuilder

        return CopyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_path(self) -> DeleteRequestBuilder:
        """
        The deletePath property
        """
        from .delete.delete_request_builder import DeleteRequestBuilder

        return DeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def duplicate(self) -> DuplicateRequestBuilder:
        """
        The duplicate property
        """
        from .duplicate.duplicate_request_builder import DuplicateRequestBuilder

        return DuplicateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def emptytrash(self) -> EmptytrashRequestBuilder:
        """
        The emptytrash property
        """
        from .emptytrash.emptytrash_request_builder import EmptytrashRequestBuilder

        return EmptytrashRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def markasread(self) -> MarkasreadRequestBuilder:
        """
        The markasread property
        """
        from .markasread.markasread_request_builder import MarkasreadRequestBuilder

        return MarkasreadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def move(self) -> MoveRequestBuilder:
        """
        The move property
        """
        from .move.move_request_builder import MoveRequestBuilder

        return MoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terminate(self) -> TerminateRequestBuilder:
        """
        The terminate property
        """
        from .terminate.terminate_request_builder import TerminateRequestBuilder

        return TerminateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FileopsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

