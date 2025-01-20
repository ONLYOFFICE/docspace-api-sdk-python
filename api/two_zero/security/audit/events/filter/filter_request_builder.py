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
    from .......models.success_api_response_of_a_s_c.web.api.api_model.response_dto.audit_event_dto import AuditEventDto

class FilterRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/security/audit/events/filter
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FilterRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/security/audit/events/filter{?action*,actionType*,entryType*,from*,moduleType*,productType*,target*,to*,userId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FilterRequestBuilderGetQueryParameters]] = None) -> Optional[AuditEventDto]:
        """
        Returns a list of the audit events by the parameters specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[AuditEventDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.success_api_response_of_a_s_c.web.api.api_model.response_dto.audit_event_dto import AuditEventDto

        return await self.request_adapter.send_async(request_info, AuditEventDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FilterRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of the audit events by the parameters specified in the request.
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
        Returns a list of the audit events by the parameters specified in the request.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "action_type":
                return "actionType"
            if original_name == "entry_type":
                return "entryType"
            if original_name == "module_type":
                return "moduleType"
            if original_name == "product_type":
                return "productType"
            if original_name == "user_id":
                return "userId"
            if original_name == "action":
                return "action"
            if original_name == "from_":
                return "from_"
            if original_name == "target":
                return "target"
            if original_name == "to":
                return "to"
            return original_name
        
        # Action
        action: Optional[int] = None

        # Action type
        action_type: Optional[int] = None

        # Entry
        entry_type: Optional[int] = None

        # Start date
        from_: Optional[str] = None

        # Module
        module_type: Optional[int] = None

        # Product
        product_type: Optional[int] = None

        # Target
        target: Optional[str] = None

        # End date
        to: Optional[str] = None

        # User ID
        user_id: Optional[UUID] = None

    
    @dataclass
    class FilterRequestBuilderGetRequestConfiguration(RequestConfiguration[FilterRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

