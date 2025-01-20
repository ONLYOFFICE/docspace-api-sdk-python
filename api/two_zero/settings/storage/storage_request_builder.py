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
    from .....models.a_s_c.web.api.api_model.requests_dto.storage_requests_dto import StorageRequestsDto
    from .....models.success_api_response_of_a_s_c.data.storage.configuration.storage_settings import StorageSettings
    from .....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.storage_dto import StorageDto
    from .backup.backup_request_builder import BackupRequestBuilder
    from .cdn.cdn_request_builder import CdnRequestBuilder
    from .progress.progress_request_builder import ProgressRequestBuilder
    from .s3.s3_request_builder import S3RequestBuilder

class StorageRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/storage
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new StorageRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/storage", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[bytes]:
        """
        Resets the storage settings to the default parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: bytes
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_primitive_async(request_info, "bytes", None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StorageDto]:
        """
        Returns a list of all the portal storages.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StorageDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.storage_dto import StorageDto

        return await self.request_adapter.send_async(request_info, StorageDto, None)
    
    async def put(self,body: StorageRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[StorageSettings]:
        """
        Updates a storage with the parameters specified in the request.
        param body: Storage settings request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StorageSettings]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.data.storage.configuration.storage_settings import StorageSettings

        return await self.request_adapter.send_async(request_info, StorageSettings, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Resets the storage settings to the default parameters.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of all the portal storages.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: StorageRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates a storage with the parameters specified in the request.
        param body: Storage settings request parameters
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
    
    def with_url(self,raw_url: str) -> StorageRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: StorageRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return StorageRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def backup(self) -> BackupRequestBuilder:
        """
        The backup property
        """
        from .backup.backup_request_builder import BackupRequestBuilder

        return BackupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cdn(self) -> CdnRequestBuilder:
        """
        The cdn property
        """
        from .cdn.cdn_request_builder import CdnRequestBuilder

        return CdnRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def progress(self) -> ProgressRequestBuilder:
        """
        The progress property
        """
        from .progress.progress_request_builder import ProgressRequestBuilder

        return ProgressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def s3(self) -> S3RequestBuilder:
        """
        The s3 property
        """
        from .s3.s3_request_builder import S3RequestBuilder

        return S3RequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class StorageRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class StorageRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class StorageRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

