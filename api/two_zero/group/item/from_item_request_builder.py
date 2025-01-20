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
    from .....models.a_s_c.people.api_models.request_dto.update_group_request import UpdateGroupRequest
    from .....models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto
    from .....models.success_api_response_of_microsoft.asp_net_core.mvc.no_content_result import NoContentResult
    from .manager.manager_request_builder import ManagerRequestBuilder
    from .members.members_request_builder import MembersRequestBuilder

class FromItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/group/{from-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new FromItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/group/{from%2Did}{?includeMembers*}", path_parameters)
    
    async def delete(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NoContentResult]:
        """
        Deletes a group with the ID specified in the request from the list of groups on the portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NoContentResult]
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_microsoft.asp_net_core.mvc.no_content_result import NoContentResult

        return await self.request_adapter.send_async(request_info, NoContentResult, None)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[FromItemRequestBuilderGetQueryParameters]] = None) -> Optional[GroupDto]:
        """
        This method returns full group information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    async def put(self,body: UpdateGroupRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupDto]:
        """
        Updates the existing group changing the group manager, name, and/or members.
        param body: Group request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    def to_delete_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Deletes a group with the ID specified in the request from the list of groups on the portal.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[FromItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This method returns full group information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: UpdateGroupRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the existing group changing the group manager, name, and/or members.
        param body: Group request parameters
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
    
    def with_url(self,raw_url: str) -> FromItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: FromItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return FromItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def manager(self) -> ManagerRequestBuilder:
        """
        The manager property
        """
        from .manager.manager_request_builder import ManagerRequestBuilder

        return ManagerRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def members(self) -> MembersRequestBuilder:
        """
        The members property
        """
        from .members.members_request_builder import MembersRequestBuilder

        return MembersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class FromItemRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FromItemRequestBuilderGetQueryParameters():
        """
        This method returns full group information.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_members":
                return "includeMembers"
            return original_name
        
        # Include members
        include_members: Optional[bool] = None

    
    @dataclass
    class FromItemRequestBuilderGetRequestConfiguration(RequestConfiguration[FromItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class FromItemRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

