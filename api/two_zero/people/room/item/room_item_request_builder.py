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
    from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

class RoomItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/room/{id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new RoomItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/room/{id}{?activationStatus*,area*,employeeStatus*,excludeShared*,invitedByMe*,inviterId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[RoomItemRequestBuilderGetQueryParameters]] = None) -> Optional[SuccessApiResponseOfAnonymous]:
        """
        Gets users with shared in room ID specified in request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SuccessApiResponseOfAnonymous]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

        return await self.request_adapter.send_async(request_info, SuccessApiResponseOfAnonymous, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[RoomItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets users with shared in room ID specified in request
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> RoomItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: RoomItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return RoomItemRequestBuilder(self.request_adapter, raw_url)
    
    from uuid import UUID

    @dataclass
    class RoomItemRequestBuilderGetQueryParameters():
        from uuid import UUID

        """
        Gets users with shared in room ID specified in request
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "activation_status":
                return "activationStatus"
            if original_name == "employee_status":
                return "employeeStatus"
            if original_name == "exclude_shared":
                return "excludeShared"
            if original_name == "invited_by_me":
                return "invitedByMe"
            if original_name == "inviter_id":
                return "inviterId"
            if original_name == "area":
                return "area"
            return original_name
        
        # Activation status
        activation_status: Optional[int] = None

        # Area
        area: Optional[int] = None

        # Employee status
        employee_status: Optional[int] = None

        # Exclude shared
        exclude_shared: Optional[bool] = None

        # Invited by me
        invited_by_me: Optional[bool] = None

        # Inviter Id
        inviter_id: Optional[UUID] = None

    
    @dataclass
    class RoomItemRequestBuilderGetRequestConfiguration(RequestConfiguration[RoomItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

