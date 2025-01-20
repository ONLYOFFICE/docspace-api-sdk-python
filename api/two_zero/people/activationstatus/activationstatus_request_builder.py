from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_activationstatus_item_request_builder import WithActivationstatusItemRequestBuilder

class ActivationstatusRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/activationstatus
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ActivationstatusRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/activationstatus", path_parameters)
    
    def by_activationstatus(self,activationstatus: int) -> WithActivationstatusItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.people.activationstatus.item collection
        param activationstatus: Activation status
        Returns: WithActivationstatusItemRequestBuilder
        """
        if activationstatus is None:
            raise TypeError("activationstatus cannot be null.")
        from .item.with_activationstatus_item_request_builder import WithActivationstatusItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["activationstatus"] = activationstatus
        return WithActivationstatusItemRequestBuilder(self.request_adapter, url_tpl_params)
    

