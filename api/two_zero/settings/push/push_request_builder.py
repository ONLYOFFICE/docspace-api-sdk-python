from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .docregisterdevice.docregisterdevice_request_builder import DocregisterdeviceRequestBuilder
    from .docsubscribe.docsubscribe_request_builder import DocsubscribeRequestBuilder

class PushRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/push
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PushRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/push", path_parameters)
    
    @property
    def docregisterdevice(self) -> DocregisterdeviceRequestBuilder:
        """
        The docregisterdevice property
        """
        from .docregisterdevice.docregisterdevice_request_builder import DocregisterdeviceRequestBuilder

        return DocregisterdeviceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def docsubscribe(self) -> DocsubscribeRequestBuilder:
        """
        The docsubscribe property
        """
        from .docsubscribe.docsubscribe_request_builder import DocsubscribeRequestBuilder

        return DocsubscribeRequestBuilder(self.request_adapter, self.path_parameters)
    

