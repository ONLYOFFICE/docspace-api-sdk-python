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
    from .....models.a_s_c.people.api_models.request_dto.update_member_request_dto import UpdateMemberRequestDto
    from .....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto
    from .contacts.contacts_request_builder import ContactsRequestBuilder
    from .culture.culture_request_builder import CultureRequestBuilder
    from .password.password_request_builder import PasswordRequestBuilder
    from .photo.photo_request_builder import PhotoRequestBuilder

class WithUserItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people/{userid}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WithUserItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people/{userid}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeFullDto]:
        """
        Deletes a user with the ID specified in the request from the portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeFullDto]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto

        return await self.request_adapter.send_async(request_info, EmployeeFullDto, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeFullDto]:
        """
        Returns the detailed information about a profile of the user with the name specified in the request.
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
    
    async def put(self,body: UpdateMemberRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeFullDto]:
        """
        Updates the data for the selected portal user with the first name, last name, email address, and/or optional parameters specified in the request.
        param body: Request parameters for updating user information
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeFullDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto

        return await self.request_adapter.send_async(request_info, EmployeeFullDto, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a user with the ID specified in the request from the portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns the detailed information about a profile of the user with the name specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: UpdateMemberRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the data for the selected portal user with the first name, last name, email address, and/or optional parameters specified in the request.
        param body: Request parameters for updating user information
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.PUT, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> WithUserItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithUserItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithUserItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def contacts(self) -> ContactsRequestBuilder:
        """
        The contacts property
        """
        from .contacts.contacts_request_builder import ContactsRequestBuilder

        return ContactsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def culture(self) -> CultureRequestBuilder:
        """
        The culture property
        """
        from .culture.culture_request_builder import CultureRequestBuilder

        return CultureRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password(self) -> PasswordRequestBuilder:
        """
        The password property
        """
        from .password.password_request_builder import PasswordRequestBuilder

        return PasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def photo(self) -> PhotoRequestBuilder:
        """
        The photo property
        """
        from .photo.photo_request_builder import PhotoRequestBuilder

        return PhotoRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WithUserItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithUserItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WithUserItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

