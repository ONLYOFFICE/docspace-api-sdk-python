from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .events.events_request_builder import EventsRequestBuilder
    from .login.login_request_builder import LoginRequestBuilder
    from .mappers.mappers_request_builder import MappersRequestBuilder
    from .settings.settings_request_builder import SettingsRequestBuilder
    from .types.types_request_builder import TypesRequestBuilder

class AuditRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/security/audit
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AuditRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/security/audit", path_parameters)
    
    @property
    def events(self) -> EventsRequestBuilder:
        """
        The events property
        """
        from .events.events_request_builder import EventsRequestBuilder

        return EventsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def login(self) -> LoginRequestBuilder:
        """
        The login property
        """
        from .login.login_request_builder import LoginRequestBuilder

        return LoginRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mappers(self) -> MappersRequestBuilder:
        """
        The mappers property
        """
        from .mappers.mappers_request_builder import MappersRequestBuilder

        return MappersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def settings(self) -> SettingsRequestBuilder:
        """
        The settings property
        """
        from .settings.settings_request_builder import SettingsRequestBuilder

        return SettingsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def types(self) -> TypesRequestBuilder:
        """
        The types property
        """
        from .types.types_request_builder import TypesRequestBuilder

        return TypesRequestBuilder(self.request_adapter, self.path_parameters)
    

