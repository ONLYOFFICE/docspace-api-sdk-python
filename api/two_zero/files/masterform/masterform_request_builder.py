from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .item.with_file_item_request_builder import WithFileItemRequestBuilder

class MasterformRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/masterform
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MasterformRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/masterform", path_parameters)
    
    def by_file_id(self,file_id: int) -> WithFileItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.files.masterform.item collection
        param file_id: File ID
        Returns: WithFileItemRequestBuilder
        """
        if file_id is None:
            raise TypeError("file_id cannot be null.")
        from .item.with_file_item_request_builder import WithFileItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["fileId"] = file_id
        return WithFileItemRequestBuilder(self.request_adapter, url_tpl_params)
    

