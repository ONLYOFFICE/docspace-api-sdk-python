from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fillresult.fillresult_request_builder import FillresultRequestBuilder
    from .item.file_item_request_builder import FileItemRequestBuilder
    from .referencedata.referencedata_request_builder import ReferencedataRequestBuilder

class FileRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/files/file
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FileRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/files/file", path_parameters)
    
    def by_file_id(self,file_id: int) -> FileItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.files.file.item collection
        param file_id: File ID
        Returns: FileItemRequestBuilder
        """
        if file_id is None:
            raise TypeError("file_id cannot be null.")
        from .item.file_item_request_builder import FileItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["file%2Did"] = file_id
        return FileItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    @property
    def fillresult(self) -> FillresultRequestBuilder:
        """
        The fillresult property
        """
        from .fillresult.fillresult_request_builder import FillresultRequestBuilder

        return FillresultRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def referencedata(self) -> ReferencedataRequestBuilder:
        """
        The referencedata property
        """
        from .referencedata.referencedata_request_builder import ReferencedataRequestBuilder

        return ReferencedataRequestBuilder(self.request_adapter, self.path_parameters)
    

