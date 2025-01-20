from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .logos.logos_request_builder import LogosRequestBuilder
    from .logotext.logotext_request_builder import LogotextRequestBuilder
    from .restore.restore_request_builder import RestoreRequestBuilder
    from .save.save_request_builder import SaveRequestBuilder
    from .savefromfiles.savefromfiles_request_builder import SavefromfilesRequestBuilder

class WhitelabelRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/whitelabel
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WhitelabelRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/whitelabel", path_parameters)
    
    @property
    def logos(self) -> LogosRequestBuilder:
        """
        The logos property
        """
        from .logos.logos_request_builder import LogosRequestBuilder

        return LogosRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logotext(self) -> LogotextRequestBuilder:
        """
        The logotext property
        """
        from .logotext.logotext_request_builder import LogotextRequestBuilder

        return LogotextRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def restore(self) -> RestoreRequestBuilder:
        """
        The restore property
        """
        from .restore.restore_request_builder import RestoreRequestBuilder

        return RestoreRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def save(self) -> SaveRequestBuilder:
        """
        The save property
        """
        from .save.save_request_builder import SaveRequestBuilder

        return SaveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def savefromfiles(self) -> SavefromfilesRequestBuilder:
        """
        The savefromfiles property
        """
        from .savefromfiles.savefromfiles_request_builder import SavefromfilesRequestBuilder

        return SavefromfilesRequestBuilder(self.request_adapter, self.path_parameters)
    

