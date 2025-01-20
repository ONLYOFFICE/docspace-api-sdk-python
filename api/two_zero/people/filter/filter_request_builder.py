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
    from .....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto

class FilterRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/filter
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FilterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/filter{?accountLoginType*,activationStatus*,area*,employeeStatus*,employeeType*,employeeTypes,excludeGroup*,groupId*,invitedByMe*,inviterId*,isAdministrator*,payments*,quotaFilter*,withoutGroup*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FilterRequestBuilderGetQueryParameters]] = None) -> Optional[EmployeeFullDto]:
        """
        Returns a list of users with full information about them matching the parameters specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeFullDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto

        return await self.request_adapter.send_async(request_info, EmployeeFullDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FilterRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of users with full information about them matching the parameters specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> FilterRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FilterRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FilterRequestBuilder(self.request_adapter, raw_url)
    
    from uuid import UUID

    @dataclass
    class FilterRequestBuilderGetQueryParameters():
        from uuid import UUID

        """
        Returns a list of users with full information about them matching the parameters specified in the request.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "account_login_type":
                return "accountLoginType"
            if original_name == "activation_status":
                return "activationStatus"
            if original_name == "employee_status":
                return "employeeStatus"
            if original_name == "employee_type":
                return "employeeType"
            if original_name == "employee_types":
                return "employeeTypes"
            if original_name == "exclude_group":
                return "excludeGroup"
            if original_name == "group_id":
                return "groupId"
            if original_name == "invited_by_me":
                return "invitedByMe"
            if original_name == "inviter_id":
                return "inviterId"
            if original_name == "is_administrator":
                return "isAdministrator"
            if original_name == "quota_filter":
                return "quotaFilter"
            if original_name == "without_group":
                return "withoutGroup"
            if original_name == "area":
                return "area"
            if original_name == "payments":
                return "payments"
            return original_name
        
        # Account login type
        account_login_type: Optional[int] = None

        # Activation status
        activation_status: Optional[int] = None

        # Area
        area: Optional[int] = None

        # User status
        employee_status: Optional[int] = None

        # User type
        employee_type: Optional[int] = None

        # List of user types
        employee_types: Optional[List[str]] = None

        # Specifies whether or not the user should be a member of the group with the specified ID
        exclude_group: Optional[bool] = None

        # Group ID
        group_id: Optional[UUID] = None

        # Invited by me
        invited_by_me: Optional[bool] = None

        # Inviter Id
        inviter_id: Optional[UUID] = None

        # Specifies if the user is an administrator or not
        is_administrator: Optional[bool] = None

        # User payment status
        payments: Optional[int] = None

        # Filter by quota (Default - 1, Custom - 2)
        quota_filter: Optional[int] = None

        # Specifies whether the user should be a member of a group or not
        without_group: Optional[bool] = None

    
    @dataclass
    class FilterRequestBuilderGetRequestConfiguration(RequestConfiguration[FilterRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

