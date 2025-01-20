from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

class TypeRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/type
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TypeRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/type", path_parameters)
    
    def by_type(self,type: int) -> WithTypeItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.people.type.item collection
        param type: New user type
        Returns: WithTypeItemRequestBuilder
        """
        if type is None:
            raise TypeError("type cannot be null.")
        from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["type"] = type
        return WithTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    

