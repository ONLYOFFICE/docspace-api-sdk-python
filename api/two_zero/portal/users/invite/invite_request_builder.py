from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_employee_type_item_request_builder import WithEmployeeTypeItemRequestBuilder

class InviteRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/portal/users/invite
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new InviteRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/portal/users/invite", path_parameters)
    
    def by_employee_type(self,employee_type: int) -> WithEmployeeTypeItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.portal.users.invite.item collection
        param employee_type: Employee type (All, RoomAdmin, User, DocSpaceAdmin)
        Returns: WithEmployeeTypeItemRequestBuilder
        """
        if employee_type is None:
            raise TypeError("employee_type cannot be null.")
        from .item.with_employee_type_item_request_builder import WithEmployeeTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["employeeType"] = employee_type
        return WithEmployeeTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

