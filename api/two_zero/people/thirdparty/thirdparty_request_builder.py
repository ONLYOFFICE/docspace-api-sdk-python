from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .linkaccount.linkaccount_request_builder import LinkaccountRequestBuilder
    from .providers.providers_request_builder import ProvidersRequestBuilder
    from .signup.signup_request_builder import SignupRequestBuilder
    from .unlinkaccount.unlinkaccount_request_builder import UnlinkaccountRequestBuilder

class ThirdpartyRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/thirdparty
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new ThirdpartyRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/thirdparty", path_parameters)
    
    @property
    def linkaccount(self) -> LinkaccountRequestBuilder:
        """
        The linkaccount property
        """
        from .linkaccount.linkaccount_request_builder import LinkaccountRequestBuilder

        return LinkaccountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def providers(self) -> ProvidersRequestBuilder:
        """
        The providers property
        """
        from .providers.providers_request_builder import ProvidersRequestBuilder

        return ProvidersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def signup(self) -> SignupRequestBuilder:
        """
        The signup property
        """
        from .signup.signup_request_builder import SignupRequestBuilder

        return SignupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def unlinkaccount(self) -> UnlinkaccountRequestBuilder:
        """
        The unlinkaccount property
        """
        from .unlinkaccount.unlinkaccount_request_builder import UnlinkaccountRequestBuilder

        return UnlinkaccountRequestBuilder(self.request_adapter, self.path_parameters)
    

