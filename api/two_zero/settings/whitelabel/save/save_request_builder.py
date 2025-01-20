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
    from ......models.a_s_c.web.api.api_model.requests_dto.white_label_requests_dto import WhiteLabelRequestsDto
    from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

class SaveRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/whitelabel/save
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new SaveRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/whitelabel/save{?IsDark*,IsDefault*}", path_parameters)
    
    async def post(self,body: WhiteLabelRequestsDto, request_configuration: Optional[RequestConfiguration[SaveRequestBuilderPostQueryParameters]] = None) -> Optional[SuccessApiResponseOfAnonymous]:
        """
        Saves the white label settings specified in the request.
        param body: Request parameters for white label settings
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SuccessApiResponseOfAnonymous]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_post_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

        return await self.request_adapter.send_async(request_info, SuccessApiResponseOfAnonymous, None)
    
    def to_post_request_information(self,body: WhiteLabelRequestsDto, request_configuration: Optional[RequestConfiguration[SaveRequestBuilderPostQueryParameters]] = None) -> RequestInformation:
        """
        Saves the white label settings specified in the request.
        param body: Request parameters for white label settings
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
    
    def with_url(self,raw_url: str) -> SaveRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: SaveRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return SaveRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class SaveRequestBuilderPostQueryParameters():
        """
        Saves the white label settings specified in the request.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "is_dark":
                return "IsDark"
            if original_name == "is_default":
                return "IsDefault"
            return original_name
        
        # Specifies if the logo is for a dark theme or not
        is_dark: Optional[bool] = None

        # Specifies if the logo is for a default tenant or not
        is_default: Optional[bool] = None

    
    @dataclass
    class SaveRequestBuilderPostRequestConfiguration(RequestConfiguration[SaveRequestBuilderPostQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

