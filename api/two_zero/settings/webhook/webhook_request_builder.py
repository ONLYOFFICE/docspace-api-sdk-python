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
    from .....models.a_s_c.web.api.api_models.requests_dto.webhooks_config_requests_dto import WebhooksConfigRequestsDto
    from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_config_dto import WebhooksConfigDto
    from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_config_with_status_dto import WebhooksConfigWithStatusDto
    from .item.webhook_item_request_builder import WebhookItemRequestBuilder
    from .retry.retry_request_builder import RetryRequestBuilder

class WebhookRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/webhook
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new WebhookRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/webhook", path_parameters)
    
    def by_id(self,id: int) -> WebhookItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.settings.webhook.item collection
        param id: Id
        Returns: WebhookItemRequestBuilder
        """
        if id is None:
            raise TypeError("id cannot be null.")
        from .item.webhook_item_request_builder import WebhookItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["id"] = id
        return WebhookItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WebhooksConfigWithStatusDto]:
        """
        Returns a list of the tenant webhooks.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WebhooksConfigWithStatusDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_config_with_status_dto import WebhooksConfigWithStatusDto

        return await self.request_adapter.send_async(request_info, WebhooksConfigWithStatusDto, None)
    
    async def post(self,body: WebhooksConfigRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WebhooksConfigDto]:
        """
        Creates a new tenant webhook with the parameters specified in the request.
        param body: Webhook request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WebhooksConfigDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_config_dto import WebhooksConfigDto

        return await self.request_adapter.send_async(request_info, WebhooksConfigDto, None)
    
    async def put(self,body: WebhooksConfigRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[WebhooksConfigDto]:
        """
        Updates the tenant webhook with the parameters specified in the request.
        param body: Webhook request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WebhooksConfigDto]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_config_dto import WebhooksConfigDto

        return await self.request_adapter.send_async(request_info, WebhooksConfigDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Returns a list of the tenant webhooks.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_post_request_information(self,body: WebhooksConfigRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Creates a new tenant webhook with the parameters specified in the request.
        param body: Webhook request parameters
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
    
    def to_put_request_information(self,body: WebhooksConfigRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Updates the tenant webhook with the parameters specified in the request.
        param body: Webhook request parameters
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
    
    def with_url(self,raw_url: str) -> WebhookRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WebhookRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WebhookRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def retry(self) -> RetryRequestBuilder:
        """
        The retry property
        """
        from .retry.retry_request_builder import RetryRequestBuilder

        return RetryRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class WebhookRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WebhookRequestBuilderPostRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class WebhookRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

