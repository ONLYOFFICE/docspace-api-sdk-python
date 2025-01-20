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
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from .....models.a_s_c.web.api.api_model.requests_dto.web_item_security_requests_dto import WebItemSecurityRequestsDto
    from .....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.security_dto import SecurityDto
    from .access.access_request_builder import AccessRequestBuilder
    from .administrator.administrator_request_builder import AdministratorRequestBuilder
    from .item.security_item_request_builder import SecurityItemRequestBuilder
    from .loginsettings.loginsettings_request_builder import LoginsettingsRequestBuilder
    from .modules.modules_request_builder import ModulesRequestBuilder
    from .password.password_request_builder import PasswordRequestBuilder

class SecurityRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/security
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SecurityRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/security{?ids}", path_parameters)
    
    def by_id(self,id: UUID) -> SecurityItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.settings.security.item collection
        param id: Id
        Returns: SecurityItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.security_item_request_builder import SecurityItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return SecurityItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[SecurityRequestBuilderGetQueryParameters]] = None) -> Optional[SecurityDto]:
        """
        Returns the security settings for the modules specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SecurityDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.security_dto import SecurityDto

        return await self.request_adapter.send_async(request_info, SecurityDto, None)
    
    async def put(self,body: WebItemSecurityRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SecurityDto]:
        """
        Sets the security settings to the module with the ID specified in the request.
        param body: Module request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SecurityDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_model.response_dto.security_dto import SecurityDto

        return await self.request_adapter.send_async(request_info, SecurityDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[SecurityRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the security settings for the modules specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: WebItemSecurityRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Sets the security settings to the module with the ID specified in the request.
        param body: Module request parameters
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
    
    def with_url(self,raw_url: str) -> SecurityRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SecurityRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SecurityRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def access(self) -> AccessRequestBuilder:
        """
        The access property
        """
        from .access.access_request_builder import AccessRequestBuilder

        return AccessRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def administrator(self) -> AdministratorRequestBuilder:
        """
        The administrator property
        """
        from .administrator.administrator_request_builder import AdministratorRequestBuilder

        return AdministratorRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def loginsettings(self) -> LoginsettingsRequestBuilder:
        """
        The loginsettings property
        """
        from .loginsettings.loginsettings_request_builder import LoginsettingsRequestBuilder

        return LoginsettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def modules(self) -> ModulesRequestBuilder:
        """
        The modules property
        """
        from .modules.modules_request_builder import ModulesRequestBuilder

        return ModulesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password(self) -> PasswordRequestBuilder:
        """
        The password property
        """
        from .password.password_request_builder import PasswordRequestBuilder

        return PasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class SecurityRequestBuilderGetQueryParameters():
        """
        Returns the security settings for the modules specified in the request.
        """
        # List of module IDs
        ids: Optional[List[str]] = None

    
    @dataclass
    class SecurityRequestBuilderGetRequestConfiguration(RequestConfiguration[SecurityRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class SecurityRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

