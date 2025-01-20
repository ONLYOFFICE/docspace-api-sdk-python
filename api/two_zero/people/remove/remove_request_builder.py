from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .progress.progress_request_builder import ProgressRequestBuilder
    from .start.start_request_builder import StartRequestBuilder
    from .terminate.terminate_request_builder import TerminateRequestBuilder

class RemoveRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/remove
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RemoveRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/remove", path_parameters)
    
    @property
    def progress(self) -> ProgressRequestBuilder:
        """
        The progress property
        """
        from .progress.progress_request_builder import ProgressRequestBuilder

        return ProgressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def start(self) -> StartRequestBuilder:
        """
        The start property
        """
        from .start.start_request_builder import StartRequestBuilder

        return StartRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def terminate(self) -> TerminateRequestBuilder:
        """
        The terminate property
        """
        from .terminate.terminate_request_builder import TerminateRequestBuilder

        return TerminateRequestBuilder(self.request_adapter, self.path_parameters)
    

