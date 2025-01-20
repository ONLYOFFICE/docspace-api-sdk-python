from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item.with_user_item_request_builder import WithUserItemRequestBuilder

class UserRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/group/user
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UserRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/group/user", path_parameters)
    
    def by_userid(self,userid: UUID) -> WithUserItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.group.user.item collection
        param userid: User ID
        Returns: WithUserItemRequestBuilder
        """
        if userid is None:
            raise TypeError("userid cannot be null.")
        from .item.with_user_item_request_builder import WithUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userid"] = userid
        return WithUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    

