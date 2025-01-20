from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .createbackupschedule.createbackupschedule_request_builder import CreatebackupscheduleRequestBuilder
    from .deletebackup.deletebackup_request_builder import DeletebackupRequestBuilder
    from .deletebackuphistory.deletebackuphistory_request_builder import DeletebackuphistoryRequestBuilder
    from .deletebackupschedule.deletebackupschedule_request_builder import DeletebackupscheduleRequestBuilder
    from .getbackuphistory.getbackuphistory_request_builder import GetbackuphistoryRequestBuilder
    from .getbackupprogress.getbackupprogress_request_builder import GetbackupprogressRequestBuilder
    from .getbackupschedule.getbackupschedule_request_builder import GetbackupscheduleRequestBuilder
    from .getrestoreprogress.getrestoreprogress_request_builder import GetrestoreprogressRequestBuilder
    from .startbackup.startbackup_request_builder import StartbackupRequestBuilder
    from .startrestore.startrestore_request_builder import StartrestoreRequestBuilder

class BackupRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/backup
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new BackupRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/backup", path_parameters)
    
    @property
    def createbackupschedule(self) -> CreatebackupscheduleRequestBuilder:
        """
        The createbackupschedule property
        """
        from .createbackupschedule.createbackupschedule_request_builder import CreatebackupscheduleRequestBuilder

        return CreatebackupscheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deletebackup(self) -> DeletebackupRequestBuilder:
        """
        The deletebackup property
        """
        from .deletebackup.deletebackup_request_builder import DeletebackupRequestBuilder

        return DeletebackupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deletebackuphistory(self) -> DeletebackuphistoryRequestBuilder:
        """
        The deletebackuphistory property
        """
        from .deletebackuphistory.deletebackuphistory_request_builder import DeletebackuphistoryRequestBuilder

        return DeletebackuphistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def deletebackupschedule(self) -> DeletebackupscheduleRequestBuilder:
        """
        The deletebackupschedule property
        """
        from .deletebackupschedule.deletebackupschedule_request_builder import DeletebackupscheduleRequestBuilder

        return DeletebackupscheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def getbackuphistory(self) -> GetbackuphistoryRequestBuilder:
        """
        The getbackuphistory property
        """
        from .getbackuphistory.getbackuphistory_request_builder import GetbackuphistoryRequestBuilder

        return GetbackuphistoryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def getbackupprogress(self) -> GetbackupprogressRequestBuilder:
        """
        The getbackupprogress property
        """
        from .getbackupprogress.getbackupprogress_request_builder import GetbackupprogressRequestBuilder

        return GetbackupprogressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def getbackupschedule(self) -> GetbackupscheduleRequestBuilder:
        """
        The getbackupschedule property
        """
        from .getbackupschedule.getbackupschedule_request_builder import GetbackupscheduleRequestBuilder

        return GetbackupscheduleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def getrestoreprogress(self) -> GetrestoreprogressRequestBuilder:
        """
        The getrestoreprogress property
        """
        from .getrestoreprogress.getrestoreprogress_request_builder import GetrestoreprogressRequestBuilder

        return GetrestoreprogressRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startbackup(self) -> StartbackupRequestBuilder:
        """
        The startbackup property
        """
        from .startbackup.startbackup_request_builder import StartbackupRequestBuilder

        return StartbackupRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def startrestore(self) -> StartrestoreRequestBuilder:
        """
        The startrestore property
        """
        from .startrestore.startrestore_request_builder import StartrestoreRequestBuilder

        return StartrestoreRequestBuilder(self.request_adapter, self.path_parameters)
    

