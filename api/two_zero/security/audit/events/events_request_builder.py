from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .filter.filter_request_builder import FilterRequestBuilder
    from .last.last_request_builder import LastRequestBuilder
    from .report.report_request_builder import ReportRequestBuilder

class EventsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/security/audit/events
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new EventsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/security/audit/events", path_parameters)
    
    @property
    def filter(self) -> FilterRequestBuilder:
        """
        The filter property
        """
        from .filter.filter_request_builder import FilterRequestBuilder

        return FilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def last(self) -> LastRequestBuilder:
        """
        The last property
        """
        from .last.last_request_builder import LastRequestBuilder

        return LastRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def report(self) -> ReportRequestBuilder:
        """
        The report property
        """
        from .report.report_request_builder import ReportRequestBuilder

        return ReportRequestBuilder(self.request_adapter, self.path_parameters)
    

