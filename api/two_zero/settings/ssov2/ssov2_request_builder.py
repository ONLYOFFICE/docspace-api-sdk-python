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
    from .....models.a_s_c.web.api.api_model.requests_dto.sso_settings_requests_dto import SsoSettingsRequestsDto
    from .....models.success_api_response_of_a_s_c.web.studio.user_controls.management.single_sign_on_settings.sso_settings_v2 import SsoSettingsV2
    from .constants.constants_request_builder import ConstantsRequestBuilder
    from .default.default_request_builder import DefaultRequestBuilder

class Ssov2RequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/ssov2
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new Ssov2RequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/ssov2", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SsoSettingsV2]:
        """
        Resets the SSO settings of the current portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SsoSettingsV2]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.studio.user_controls.management.single_sign_on_settings.sso_settings_v2 import SsoSettingsV2

        return await self.request_adapter.send_async(request_info, SsoSettingsV2, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SsoSettingsV2]:
        """
        Returns the current portal SSO settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SsoSettingsV2]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.studio.user_controls.management.single_sign_on_settings.sso_settings_v2 import SsoSettingsV2

        return await self.request_adapter.send_async(request_info, SsoSettingsV2, None)
    
    async def post(self,body: SsoSettingsRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SsoSettingsV2]:
        """
        Saves the SSO settings for the current portal.
        param body: SSO settings request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SsoSettingsV2]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.studio.user_controls.management.single_sign_on_settings.sso_settings_v2 import SsoSettingsV2

        return await self.request_adapter.send_async(request_info, SsoSettingsV2, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Resets the SSO settings of the current portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the current portal SSO settings.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: SsoSettingsRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Saves the SSO settings for the current portal.
        param body: SSO settings request parameters
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
    
    def with_url(self,raw_url: str) -> Ssov2RequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: Ssov2RequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return Ssov2RequestBuilder(self.request_adapter, raw_url)
    
    @property
    def constants(self) -> ConstantsRequestBuilder:
        """
        The constants property
        """
        from .constants.constants_request_builder import ConstantsRequestBuilder

        return ConstantsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def default(self) -> DefaultRequestBuilder:
        """
        The default property
        """
        from .default.default_request_builder import DefaultRequestBuilder

        return DefaultRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class Ssov2RequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class Ssov2RequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class Ssov2RequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

