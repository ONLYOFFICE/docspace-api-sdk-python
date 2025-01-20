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
    from ......models.a_s_c.people.api_models.request_dto.members_request import MembersRequest
    from ......models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto
    from .item.with_to_item_request_builder import WithToItemRequestBuilder

class MembersRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/group/{from-id}/members
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new MembersRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/group/{from%2Did}/members", path_parameters)
    
    def by_to_id(self,to_id: UUID) -> WithToItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.group.item.members.item collection
        param to_id: Group ID to move to
        Returns: WithToItemRequestBuilder
        """
        if to_id is None:
            raise TypeError("to_id cannot be null.")
        from .item.with_to_item_request_builder import WithToItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["toId"] = to_id
        return WithToItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def delete(self,body: MembersRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupDto]:
        """
        Removes the group members specified in the request from the selected group.
        param body: Group request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[GroupDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_delete_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    async def post(self,body: MembersRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupDto]:
        """
        Replaces the group members with those specified in the request.
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
        from ......models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    async def put(self,body: MembersRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[GroupDto]:
        """
        Adds new group members to the group with the ID specified in the request.
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
        from ......models.success_api_response_of_a_s_c.people.api_models.response_dto.group_dto import GroupDto

        return await self.request_adapter.send_async(request_info, GroupDto, None)
    
    def to_delete_request_information(self,body: MembersRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Removes the group members specified in the request from the selected group.
        param body: Group request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = RequestInformation(Method.DELETE, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    def to_post_request_information(self,body: MembersRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Replaces the group members with those specified in the request.
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
    
    def to_put_request_information(self,body: MembersRequest, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds new group members to the group with the ID specified in the request.
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
    
    def with_url(self,raw_url: str) -> MembersRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: MembersRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return MembersRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class MembersRequestBuilderDeleteRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MembersRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class MembersRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

