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
    from .....models.a_s_c.files.core.api_models.request_dto.settings_request_dto import SettingsRequestDto
    from .....models.a_s_c.files.core.api_models.request_dto.third_party_request_dto import ThirdPartyRequestDto
    from .....models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous
    from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.string import String
    from .....models.success_api_response_of_a_s_c.web.files.services.w_c_f_service.third_party_params import ThirdPartyParams
    from .backup.backup_request_builder import BackupRequestBuilder
    from .capabilities.capabilities_request_builder import CapabilitiesRequestBuilder
    from .common.common_request_builder import CommonRequestBuilder
    from .item.with_provider_item_request_builder import WithProviderItemRequestBuilder
    from .providers.providers_request_builder import ProvidersRequestBuilder

class ThirdpartyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/thirdparty
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ThirdpartyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/thirdparty", path_parameters)
    
    def by_provider_id(self,provider_id: int) -> WithProviderItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.files.thirdparty.item collection
        param provider_id: Provider ID
        Returns: WithProviderItemRequestBuilder
        """
        if provider_id is None:
            raise TypeError("provider_id cannot be null.")
        from .item.with_provider_item_request_builder import WithProviderItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["providerId"] = provider_id
        return WithProviderItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ThirdPartyParams]:
        """
        Returns a list of all the connected third-party accounts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ThirdPartyParams]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.files.services.w_c_f_service.third_party_params import ThirdPartyParams

        return await self.request_adapter.send_async(request_info, ThirdPartyParams, None)
    
    async def post(self,body: ThirdPartyRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[str]:
        """
        List of provider keys: DropboxV2, Box, WebDav, Yandex, OneDrive, SharePoint, GoogleDrive, kDrive.
        param body: Third-party request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[str]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.files.core.api_models.response_dto.folder_dto.system.string import String

        return await self.request_adapter.send_primitive_async(request_info, "str", None)
    
    async def put(self,body: SettingsRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SuccessApiResponseOfAnonymous]:
        """
        Changes the access to the third-party settings.
        param body: Settings request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SuccessApiResponseOfAnonymous]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

        return await self.request_adapter.send_async(request_info, SuccessApiResponseOfAnonymous, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of all the connected third-party accounts.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: ThirdPartyRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        List of provider keys: DropboxV2, Box, WebDav, Yandex, OneDrive, SharePoint, GoogleDrive, kDrive.
        param body: Third-party request parameters
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
    
    def to_put_request_information(self,body: SettingsRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Changes the access to the third-party settings.
        param body: Settings request parameters
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
    
    def with_url(self,raw_url: str) -> ThirdpartyRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ThirdpartyRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ThirdpartyRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def backup(self) -> BackupRequestBuilder:
        """
        The backup property
        """
        from .backup.backup_request_builder import BackupRequestBuilder

        return BackupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def capabilities(self) -> CapabilitiesRequestBuilder:
        """
        The capabilities property
        """
        from .capabilities.capabilities_request_builder import CapabilitiesRequestBuilder

        return CapabilitiesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def common(self) -> CommonRequestBuilder:
        """
        The common property
        """
        from .common.common_request_builder import CommonRequestBuilder

        return CommonRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def providers(self) -> ProvidersRequestBuilder:
        """
        The providers property
        """
        from .providers.providers_request_builder import ProvidersRequestBuilder

        return ProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ThirdpartyRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ThirdpartyRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ThirdpartyRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

