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
    from .....models.a_s_c.web.api.api_models.requests_dto.custom_color_themes_settings_requests_dto import CustomColorThemesSettingsRequestsDto
    from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.custom_color_themes_settings_dto import CustomColorThemesSettingsDto

class ColorthemeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/colortheme
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ColorthemeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/colortheme{?id*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[ColorthemeRequestBuilderDeleteQueryParameters]] = None) -> Optional[CustomColorThemesSettingsDto]:
        """
        Deletes the portal color theme with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomColorThemesSettingsDto]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.custom_color_themes_settings_dto import CustomColorThemesSettingsDto

        return await self.request_adapter.send_async(request_info, CustomColorThemesSettingsDto, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomColorThemesSettingsDto]:
        """
        Returns the portal color theme.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomColorThemesSettingsDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.custom_color_themes_settings_dto import CustomColorThemesSettingsDto

        return await self.request_adapter.send_async(request_info, CustomColorThemesSettingsDto, None)
    
    async def put(self,body: CustomColorThemesSettingsRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[CustomColorThemesSettingsDto]:
        """
        Saves the portal color theme specified in the request.
        param body: Portal theme settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[CustomColorThemesSettingsDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.custom_color_themes_settings_dto import CustomColorThemesSettingsDto

        return await self.request_adapter.send_async(request_info, CustomColorThemesSettingsDto, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[ColorthemeRequestBuilderDeleteQueryParameters]] = None) -> RequestInformation:
        """
        Deletes the portal color theme with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the portal color theme.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: CustomColorThemesSettingsRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Saves the portal color theme specified in the request.
        param body: Portal theme settings
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
    
    def with_url(self,raw_url: str) -> ColorthemeRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ColorthemeRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ColorthemeRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class ColorthemeRequestBuilderDeleteQueryParameters():
        """
        Deletes the portal color theme with the ID specified in the request.
        """
        # Portal theme ID
        id: Optional[int] = None

    
    @dataclass
    class ColorthemeRequestBuilderDeleteRequestConfiguration(RequestConfiguration[ColorthemeRequestBuilderDeleteQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ColorthemeRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class ColorthemeRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

