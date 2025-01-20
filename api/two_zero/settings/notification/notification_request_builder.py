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
    from .....models.a_s_c.web.api.api_models.requests_dto.notification_settings_requests_dto import NotificationSettingsRequestsDto
    from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.notification_settings_dto import NotificationSettingsDto
    from .item.with_type_item_request_builder import WithTypeItemRequestBuilder
    from .rooms.rooms_request_builder import RoomsRequestBuilder

class NotificationRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/notification
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new NotificationRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/notification", path_parameters)
    
    def by_type(self,type: int) -> WithTypeItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.settings.notification.item collection
        param type: Notification type (Badges, RoomsActivity, DailyFeed, UsefullTips)
        Returns: WithTypeItemRequestBuilder
        """
        if type is None:
            raise TypeError("type cannot be null.")
        from .item.with_type_item_request_builder import WithTypeItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["type"] = type
        return WithTypeItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def post(self,body: NotificationSettingsRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[NotificationSettingsDto]:
        """
        Enables the notification type specified in the request.
        param body: Notification settings request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[NotificationSettingsDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.notification_settings_dto import NotificationSettingsDto

        return await self.request_adapter.send_async(request_info, NotificationSettingsDto, None)
    
    def to_post_request_information(self,body: NotificationSettingsRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Enables the notification type specified in the request.
        param body: Notification settings request parameters
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
    
    def with_url(self,raw_url: str) -> NotificationRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: NotificationRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return NotificationRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def rooms(self) -> RoomsRequestBuilder:
        """
        The rooms property
        """
        from .rooms.rooms_request_builder import RoomsRequestBuilder

        return RoomsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class NotificationRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

