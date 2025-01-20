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
    from .....models.a_s_c.web.api.api_model.requests_dto.tips_request_dto import TipsRequestDto
    from .....models.success_api_response_of_a_s_c.web.studio.core.tips_settings import TipsSettings
    from .change.change_request_builder import ChangeRequestBuilder
    from .subscription.subscription_request_builder import SubscriptionRequestBuilder

class TipsRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/tips
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new TipsRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/tips", path_parameters)
    
    async def put(self,body: TipsRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[TipsSettings]:
        """
        Updates the tip settings with a parameter specified in the request.
        param body: Settings request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[TipsSettings]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.studio.core.tips_settings import TipsSettings

        return await self.request_adapter.send_async(request_info, TipsSettings, None)
    
    def to_put_request_information(self,body: TipsRequestDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the tip settings with a parameter specified in the request.
        param body: Settings request parameters
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
    
    def with_url(self,raw_url: str) -> TipsRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: TipsRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return TipsRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def change(self) -> ChangeRequestBuilder:
        """
        The change property
        """
        from .change.change_request_builder import ChangeRequestBuilder

        return ChangeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def subscription(self) -> SubscriptionRequestBuilder:
        """
        The subscription property
        """
        from .subscription.subscription_request_builder import SubscriptionRequestBuilder

        return SubscriptionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class TipsRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

