from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .invite.invite_request_builder import InviteRequestBuilder
    from .item.with_user_item_request_builder import WithUserItemRequestBuilder

class UsersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/portal/users
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new UsersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/portal/users", path_parameters)
    
    def by_user_i_d(self,user_i_d: UUID) -> WithUserItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.portal.users.item collection
        param user_i_d: User ID
        Returns: WithUserItemRequestBuilder
        """
        if user_i_d is None:
            raise TypeError("user_i_d cannot be null.")
        from .item.with_user_item_request_builder import WithUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userID"] = user_i_d
        return WithUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def invite(self) -> InviteRequestBuilder:
        """
        The invite property
        """
        from .invite.invite_request_builder import InviteRequestBuilder

        return InviteRequestBuilder(self.request_adapter, self.path_parameters)
    

