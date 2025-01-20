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
    from ....models.a_s_c.people.api_models.request_dto.member_request_dto import MemberRequestDto
    from ....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto
    from .activationstatus.activationstatus_request_builder import ActivationstatusRequestBuilder
    from .delete.delete_request_builder import DeleteRequestBuilder
    from .email.email_request_builder import EmailRequestBuilder
    from .filter.filter_request_builder import FilterRequestBuilder
    from .guests.guests_request_builder import GuestsRequestBuilder
    from .invite.invite_request_builder import InviteRequestBuilder
    from .item.with_user_item_request_builder import WithUserItemRequestBuilder
    from .password.password_request_builder import PasswordRequestBuilder
    from .reassign.reassign_request_builder import ReassignRequestBuilder
    from .remove.remove_request_builder import RemoveRequestBuilder
    from .resetquota.resetquota_request_builder import ResetquotaRequestBuilder
    from .room.room_request_builder import RoomRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .self.self_request_builder import SelfRequestBuilder
    from .simple.simple_request_builder import SimpleRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .theme.theme_request_builder import ThemeRequestBuilder
    from .thirdparty.thirdparty_request_builder import ThirdpartyRequestBuilder
    from .tokendiagnostics.tokendiagnostics_request_builder import TokendiagnosticsRequestBuilder
    from .type.type_request_builder import TypeRequestBuilder
    from .userquota.userquota_request_builder import UserquotaRequestBuilder

class PeopleRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/people
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new PeopleRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/people", path_parameters)
    
    def by_userid(self,userid: str) -> WithUserItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.people.item collection
        param userid: User ID
        Returns: WithUserItemRequestBuilder
        """
        if userid is None:
            raise TypeError("userid cannot be null.")
        from .item.with_user_item_request_builder import WithUserItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["userid"] = userid
        return WithUserItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeFullDto]:
        """
        Returns a list of profiles for all the portal users.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeFullDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto

        return await self.request_adapter.send_async(request_info, EmployeeFullDto, None)
    
    async def post(self,body: MemberRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[EmployeeFullDto]:
        """
        Adds a new portal user with the first name, last name, email address, and several optional parameters specified in the request.
        param body: Member request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[EmployeeFullDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.success_api_response_of_a_s_c.web.api.models.employee_full_dto import EmployeeFullDto

        return await self.request_adapter.send_async(request_info, EmployeeFullDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of profiles for all the portal users.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: MemberRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Adds a new portal user with the first name, last name, email address, and several optional parameters specified in the request.
        param body: Member request parameters
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
    
    def with_url(self,raw_url: str) -> PeopleRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: PeopleRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return PeopleRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def activationstatus(self) -> ActivationstatusRequestBuilder:
        """
        The activationstatus property
        """
        from .activationstatus.activationstatus_request_builder import ActivationstatusRequestBuilder

        return ActivationstatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def delete_path(self) -> DeleteRequestBuilder:
        """
        The deletePath property
        """
        from .delete.delete_request_builder import DeleteRequestBuilder

        return DeleteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def email(self) -> EmailRequestBuilder:
        """
        The email property
        """
        from .email.email_request_builder import EmailRequestBuilder

        return EmailRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def filter(self) -> FilterRequestBuilder:
        """
        The filter property
        """
        from .filter.filter_request_builder import FilterRequestBuilder

        return FilterRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def guests(self) -> GuestsRequestBuilder:
        """
        The guests property
        """
        from .guests.guests_request_builder import GuestsRequestBuilder

        return GuestsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def invite(self) -> InviteRequestBuilder:
        """
        The invite property
        """
        from .invite.invite_request_builder import InviteRequestBuilder

        return InviteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def password(self) -> PasswordRequestBuilder:
        """
        The password property
        """
        from .password.password_request_builder import PasswordRequestBuilder

        return PasswordRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def reassign(self) -> ReassignRequestBuilder:
        """
        The reassign property
        """
        from .reassign.reassign_request_builder import ReassignRequestBuilder

        return ReassignRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def remove(self) -> RemoveRequestBuilder:
        """
        The remove property
        """
        from .remove.remove_request_builder import RemoveRequestBuilder

        return RemoveRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def resetquota(self) -> ResetquotaRequestBuilder:
        """
        The resetquota property
        """
        from .resetquota.resetquota_request_builder import ResetquotaRequestBuilder

        return ResetquotaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def room(self) -> RoomRequestBuilder:
        """
        The room property
        """
        from .room.room_request_builder import RoomRequestBuilder

        return RoomRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def self(self) -> SelfRequestBuilder:
        """
        The Self property
        """
        from .self.self_request_builder import SelfRequestBuilder

        return SelfRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def simple(self) -> SimpleRequestBuilder:
        """
        The simple property
        """
        from .simple.simple_request_builder import SimpleRequestBuilder

        return SimpleRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def theme(self) -> ThemeRequestBuilder:
        """
        The theme property
        """
        from .theme.theme_request_builder import ThemeRequestBuilder

        return ThemeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def thirdparty(self) -> ThirdpartyRequestBuilder:
        """
        The thirdparty property
        """
        from .thirdparty.thirdparty_request_builder import ThirdpartyRequestBuilder

        return ThirdpartyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def tokendiagnostics(self) -> TokendiagnosticsRequestBuilder:
        """
        The tokendiagnostics property
        """
        from .tokendiagnostics.tokendiagnostics_request_builder import TokendiagnosticsRequestBuilder

        return TokendiagnosticsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        The type property
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def userquota(self) -> UserquotaRequestBuilder:
        """
        The userquota property
        """
        from .userquota.userquota_request_builder import UserquotaRequestBuilder

        return UserquotaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class PeopleRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class PeopleRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

