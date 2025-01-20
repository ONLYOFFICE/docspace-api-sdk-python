from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from uuid import UUID

if TYPE_CHECKING:
    from .item.deletebackup_item_request_builder import DeletebackupItemRequestBuilder

class DeletebackupRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/backup/deletebackup
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new DeletebackupRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/backup/deletebackup", path_parameters)
    
    def by_id(self,id: UUID) -> DeletebackupItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.backup.deletebackup.item collection
        param id: Backup Id
        Returns: DeletebackupItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.deletebackup_item_request_builder import DeletebackupItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return DeletebackupItemRequestBuilder(self.request_adapter, url_tpl_params)
    

