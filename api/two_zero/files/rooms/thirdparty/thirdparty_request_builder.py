from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.thirdparty_item_request_builder import ThirdpartyItemRequestBuilder

class ThirdpartyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/rooms/thirdparty
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ThirdpartyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/rooms/thirdparty", path_parameters)
    
    def by_id(self,id: str) -> ThirdpartyItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.files.rooms.thirdparty.item collection
        param id: ID of the folder in the third-party storage in which the contents of the room will be stored
        Returns: ThirdpartyItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.thirdparty_item_request_builder import ThirdpartyItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return ThirdpartyItemRequestBuilder(self.request_adapter, url_tpl_params)
    

