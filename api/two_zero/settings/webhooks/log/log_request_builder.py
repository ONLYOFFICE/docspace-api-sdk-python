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
    from ......models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_log_dto import WebhooksLogDto

class LogRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/webhooks/log
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new LogRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/webhooks/log{?configId*,deliveryFrom*,deliveryTo*,eventId*,groupStatus*,hookUri*,webhookId*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[LogRequestBuilderGetQueryParameters]] = None) -> Optional[WebhooksLogDto]:
        """
        Returns the logs of the webhook activities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[WebhooksLogDto]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_a_s_c.web.api.api_models.response_dto.webhooks_log_dto import WebhooksLogDto

        return await self.request_adapter.send_async(request_info, WebhooksLogDto, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[LogRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Returns the logs of the webhook activities.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def with_url(self,raw_url: str) -> LogRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: LogRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return LogRequestBuilder(self.request_adapter, raw_url)
    
    import datetime

    @dataclass
    class LogRequestBuilderGetQueryParameters():
        import datetime

        """
        Returns the logs of the webhook activities.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "config_id":
                return "configId"
            if original_name == "delivery_from":
                return "deliveryFrom"
            if original_name == "delivery_to":
                return "deliveryTo"
            if original_name == "event_id":
                return "eventId"
            if original_name == "group_status":
                return "groupStatus"
            if original_name == "hook_uri":
                return "hookUri"
            if original_name == "webhook_id":
                return "webhookId"
            return original_name
        
        # Config ID
        config_id: Optional[int] = None

        # Delivey start time
        delivery_from: Optional[datetime.datetime] = None

        # Delivey end time
        delivery_to: Optional[datetime.datetime] = None

        # Event ID
        event_id: Optional[int] = None

        # Webhook group status
        group_status: Optional[int] = None

        # Hook URI
        hook_uri: Optional[str] = None

        # Webhook ID
        webhook_id: Optional[int] = None

    
    @dataclass
    class LogRequestBuilderGetRequestConfiguration(RequestConfiguration[LogRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

