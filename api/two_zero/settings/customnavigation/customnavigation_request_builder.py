from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .create.create_request_builder import CreateRequestBuilder
    from .delete.delete_request_builder import DeleteRequestBuilder
    from .get.get_request_builder import GetRequestBuilder
    from .getall.getall_request_builder import GetallRequestBuilder
    from .getsample.getsample_request_builder import GetsampleRequestBuilder

class CustomnavigationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/customnavigation
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new CustomnavigationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/customnavigation", path_parameters)
    
    @property
    def create(self) -> CreateRequestBuilder:
        """
        The create property
        """
        from .create.create_request_builder import CreateRequestBuilder

        return CreateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_path(self) -> DeleteRequestBuilder:
        """
        The deletePath property
        """
        from .delete.delete_request_builder import DeleteRequestBuilder

        return DeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_path(self) -> GetRequestBuilder:
        """
        The getPath property
        """
        from .get.get_request_builder import GetRequestBuilder

        return GetRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def getall(self) -> GetallRequestBuilder:
        """
        The getall property
        """
        from .getall.getall_request_builder import GetallRequestBuilder

        return GetallRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def getsample(self) -> GetsampleRequestBuilder:
        """
        The getsample property
        """
        from .getsample.getsample_request_builder import GetsampleRequestBuilder

        return GetsampleRequestBuilder(self.request_adapter, self.path_parameters)
    

