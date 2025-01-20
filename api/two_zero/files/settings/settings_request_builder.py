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
    from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.files_settings_dto import FilesSettingsDto
    from .autocleanup.autocleanup_request_builder import AutocleanupRequestBuilder
    from .dafaultaccessrights.dafaultaccessrights_request_builder import DafaultaccessrightsRequestBuilder
    from .downloadtargz.downloadtargz_request_builder import DownloadtargzRequestBuilder
    from .external.external_request_builder import ExternalRequestBuilder
    from .externalsocialmedia.externalsocialmedia_request_builder import ExternalsocialmediaRequestBuilder
    from .openeditorinsametab.openeditorinsametab_request_builder import OpeneditorinsametabRequestBuilder

class SettingsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/settings
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SettingsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/settings", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[FilesSettingsDto]:
        """
        Returns all the file settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[FilesSettingsDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.files_settings_dto import FilesSettingsDto

        return await self.request_adapter.send_async(request_info, FilesSettingsDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all the file settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> SettingsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SettingsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SettingsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def autocleanup(self) -> AutocleanupRequestBuilder:
        """
        The autocleanup property
        """
        from .autocleanup.autocleanup_request_builder import AutocleanupRequestBuilder

        return AutocleanupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def dafaultaccessrights(self) -> DafaultaccessrightsRequestBuilder:
        """
        The dafaultaccessrights property
        """
        from .dafaultaccessrights.dafaultaccessrights_request_builder import DafaultaccessrightsRequestBuilder

        return DafaultaccessrightsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def downloadtargz(self) -> DownloadtargzRequestBuilder:
        """
        The downloadtargz property
        """
        from .downloadtargz.downloadtargz_request_builder import DownloadtargzRequestBuilder

        return DownloadtargzRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def external(self) -> ExternalRequestBuilder:
        """
        The external property
        """
        from .external.external_request_builder import ExternalRequestBuilder

        return ExternalRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def externalsocialmedia(self) -> ExternalsocialmediaRequestBuilder:
        """
        The externalsocialmedia property
        """
        from .externalsocialmedia.externalsocialmedia_request_builder import ExternalsocialmediaRequestBuilder

        return ExternalsocialmediaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def openeditorinsametab(self) -> OpeneditorinsametabRequestBuilder:
        """
        The openeditorinsametab property
        """
        from .openeditorinsametab.openeditorinsametab_request_builder import OpeneditorinsametabRequestBuilder

        return OpeneditorinsametabRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SettingsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

