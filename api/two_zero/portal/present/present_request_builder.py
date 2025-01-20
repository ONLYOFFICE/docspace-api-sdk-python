from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .mark.mark_request_builder import MarkRequestBuilder

class PresentRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/portal/present
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PresentRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/portal/present", path_parameters)
    
    @property
    def mark(self) -> MarkRequestBuilder:
        """
        The mark property
        """
        from .mark.mark_request_builder import MarkRequestBuilder

        return MarkRequestBuilder(self.request_adapter, self.path_parameters)
    

