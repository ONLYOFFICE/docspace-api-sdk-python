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
    from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.active_connections_dto import ActiveConnectionsDto
    from .logout.logout_request_builder import LogoutRequestBuilder
    from .logoutall.logoutall_request_builder import LogoutallRequestBuilder
    from .logoutallchangepassword.logoutallchangepassword_request_builder import LogoutallchangepasswordRequestBuilder
    from .logoutallexceptthis.logoutallexceptthis_request_builder import LogoutallexceptthisRequestBuilder

class ActiveconnectionsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/security/activeconnections
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ActiveconnectionsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/security/activeconnections", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[ActiveConnectionsDto]:
        """
        Returns all the active connections to the portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ActiveConnectionsDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.active_connections_dto import ActiveConnectionsDto

        return await self.request_adapter.send_async(request_info, ActiveConnectionsDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns all the active connections to the portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> ActiveconnectionsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: ActiveconnectionsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return ActiveconnectionsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def logout(self) -> LogoutRequestBuilder:
        """
        The logout property
        """
        from .logout.logout_request_builder import LogoutRequestBuilder

        return LogoutRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logoutall(self) -> LogoutallRequestBuilder:
        """
        The logoutall property
        """
        from .logoutall.logoutall_request_builder import LogoutallRequestBuilder

        return LogoutallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logoutallchangepassword(self) -> LogoutallchangepasswordRequestBuilder:
        """
        The logoutallchangepassword property
        """
        from .logoutallchangepassword.logoutallchangepassword_request_builder import LogoutallchangepasswordRequestBuilder

        return LogoutallchangepasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logoutallexceptthis(self) -> LogoutallexceptthisRequestBuilder:
        """
        The logoutallexceptthis property
        """
        from .logoutallexceptthis.logoutallexceptthis_request_builder import LogoutallexceptthisRequestBuilder

        return LogoutallexceptthisRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ActiveconnectionsRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

