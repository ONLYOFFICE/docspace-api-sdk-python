from __future__ import annotations
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.tenant_dto import TenantDto
    from .continue_.continue_request_builder import ContinueRequestBuilder
    from .delete.delete_request_builder import DeleteRequestBuilder
    from .path.path_request_builder import PathRequestBuilder
    from .present.present_request_builder import PresentRequestBuilder
    from .quota.quota_request_builder import QuotaRequestBuilder
    from .sendcongratulations.sendcongratulations_request_builder import SendcongratulationsRequestBuilder
    from .suspend.suspend_request_builder import SuspendRequestBuilder
    from .tariff.tariff_request_builder import TariffRequestBuilder
    from .usedspace.usedspace_request_builder import UsedspaceRequestBuilder
    from .users.users_request_builder import UsersRequestBuilder
    from .userscount.userscount_request_builder import UserscountRequestBuilder

class PortalRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/portal
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PortalRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/portal", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TenantDto]:
        """
        Returns the current portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TenantDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.tenant_dto import TenantDto

        return await self.request_adapter.send_async(request_info, TenantDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the current portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> PortalRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PortalRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PortalRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def continue_(self) -> ContinueRequestBuilder:
        """
        The continue property
        """
        from .continue_.continue_request_builder import ContinueRequestBuilder

        return ContinueRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_path(self) -> DeleteRequestBuilder:
        """
        The deletePath property
        """
        from .delete.delete_request_builder import DeleteRequestBuilder

        return DeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def path(self) -> PathRequestBuilder:
        """
        The path property
        """
        from .path.path_request_builder import PathRequestBuilder

        return PathRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def present(self) -> PresentRequestBuilder:
        """
        The present property
        """
        from .present.present_request_builder import PresentRequestBuilder

        return PresentRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def quota(self) -> QuotaRequestBuilder:
        """
        The quota property
        """
        from .quota.quota_request_builder import QuotaRequestBuilder

        return QuotaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sendcongratulations(self) -> SendcongratulationsRequestBuilder:
        """
        The sendcongratulations property
        """
        from .sendcongratulations.sendcongratulations_request_builder import SendcongratulationsRequestBuilder

        return SendcongratulationsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def suspend(self) -> SuspendRequestBuilder:
        """
        The suspend property
        """
        from .suspend.suspend_request_builder import SuspendRequestBuilder

        return SuspendRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tariff(self) -> TariffRequestBuilder:
        """
        The tariff property
        """
        from .tariff.tariff_request_builder import TariffRequestBuilder

        return TariffRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def usedspace(self) -> UsedspaceRequestBuilder:
        """
        The usedspace property
        """
        from .usedspace.usedspace_request_builder import UsedspaceRequestBuilder

        return UsedspaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def users(self) -> UsersRequestBuilder:
        """
        The users property
        """
        from .users.users_request_builder import UsersRequestBuilder

        return UsersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def userscount(self) -> UserscountRequestBuilder:
        """
        The userscount property
        """
        from .userscount.userscount_request_builder import UserscountRequestBuilder

        return UserscountRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PortalRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

