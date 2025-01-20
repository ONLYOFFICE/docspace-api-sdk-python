from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item.with_user_item_request_builder import WithUserItemRequestBuilder

class LogoutallRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/security/activeconnections/logoutall
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LogoutallRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/security/activeconnections/logoutall", path_parameters)
    
    def by_user_id(self,user_id: UUID) -> WithUserItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.security.activeconnections.logoutall.item collection
        param user_id: User ID
        Returns: WithUserItemRequestBuilder
        """
        if user_id is None:
            raise TypeError("user_id cannot be null.")
        from .item.with_user_item_request_builder import WithUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userId"] = user_id
        return WithUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    

