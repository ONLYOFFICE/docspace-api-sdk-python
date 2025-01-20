from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item.get_item_request_builder import GetItemRequestBuilder

class GetRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/customnavigation/get
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GetRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/customnavigation/get", path_parameters)
    
    def by_id(self,id: UUID) -> GetItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.settings.customnavigation.get.item collection
        param id: Id
        Returns: GetItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.get_item_request_builder import GetItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return GetItemRequestBuilder(self.request_adapter, url_tpl_params)
    

