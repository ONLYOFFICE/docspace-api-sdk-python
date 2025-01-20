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
from uuid import UUID
from warnings import warn

if TYPE_CHECKING:
    from ....models.a_s_c.people.api_models.request_dto.group_request_dto import GroupRequestDto
    from ....models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto
    from .item.from_item_request_builder import FromItemRequestBuilder
    from .room.room_request_builder import RoomRequestBuilder
    from .user.user_request_builder import UserRequestBuilder

class GroupRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/group
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new GroupRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/group{?manager*,userId*}", path_parameters)
    
    def by_from_id(self,from_id: UUID) -> FromItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.group.item collection
        param from_id: Group ID
        Returns: FromItemRequestBuilder
        """
        if from_id is None:
            raise TypeError("from_id cannot be null.")
        from .item.from_item_request_builder import FromItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["from%2Did"] = from_id
        return FromItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[GroupRequestBuilderGetQueryParameters]] = None) -> Optional[GroupDto]:
        """
        This method returns partial group information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    async def post(self,body: GroupRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupDto]:
        """
        Adds a new group with the group manager, name, and members specified in the request.
        param body: Group request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[GroupRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        This method returns partial group information.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: GroupRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds a new group with the group manager, name, and members specified in the request.
        param body: Group request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.POST, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def with_url(self,raw_url: str) -> GroupRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: GroupRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return GroupRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def room(self) -> RoomRequestBuilder:
        """
        The room property
        """
        from .room.room_request_builder import RoomRequestBuilder

        return RoomRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def user(self) -> UserRequestBuilder:
        """
        The user property
        """
        from .user.user_request_builder import UserRequestBuilder

        return UserRequestBuilder(self.request_adapter, self.path_parameters)
    
    from uuid import UUID

    @dataclass
    class GroupRequestBuilderGetQueryParameters():
        from uuid import UUID

        """
        This method returns partial group information.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "user_id":
                return "userId"
            if original_name == "manager":
                return "manager"
            return original_name
        
        # Specifies if the user is a manager or not
        manager: Optional[bool] = None

        # User ID
        user_id: Optional[UUID] = None

    
    @dataclass
    class GroupRequestBuilderGetRequestConfiguration(RequestConfiguration[GroupRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class GroupRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

