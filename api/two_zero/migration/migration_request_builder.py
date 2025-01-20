from __future__ import annotations
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .cancel.cancel_request_builder import CancelRequestBuilder
    from .clear.clear_request_builder import ClearRequestBuilder
    from .finish.finish_request_builder import FinishRequestBuilder
    from .init.init_request_builder import InitRequestBuilder
    from .list_.list_request_builder import ListRequestBuilder
    from .logs.logs_request_builder import LogsRequestBuilder
    from .migrate.migrate_request_builder import MigrateRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder

class MigrationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/migration
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MigrationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/migration", path_parameters)
    
    @property
    def cancel(self) -> CancelRequestBuilder:
        """
        The cancel property
        """
        from .cancel.cancel_request_builder import CancelRequestBuilder

        return CancelRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def clear(self) -> ClearRequestBuilder:
        """
        The clear property
        """
        from .clear.clear_request_builder import ClearRequestBuilder

        return ClearRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def finish(self) -> FinishRequestBuilder:
        """
        The finish property
        """
        from .finish.finish_request_builder import FinishRequestBuilder

        return FinishRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def init(self) -> InitRequestBuilder:
        """
        The init property
        """
        from .init.init_request_builder import InitRequestBuilder

        return InitRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def list_(self) -> ListRequestBuilder:
        """
        The list property
        """
        from .list_.list_request_builder import ListRequestBuilder

        return ListRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def logs(self) -> LogsRequestBuilder:
        """
        The logs property
        """
        from .logs.logs_request_builder import LogsRequestBuilder

        return LogsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def migrate(self) -> MigrateRequestBuilder:
        """
        The migrate property
        """
        from .migrate.migrate_request_builder import MigrateRequestBuilder

        return MigrateRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    

