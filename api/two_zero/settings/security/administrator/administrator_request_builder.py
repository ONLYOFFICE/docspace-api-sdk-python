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
    from ......models.a_s_c.web.api.api_model.requests_dto.security_requests_dto import SecurityRequestsDto
    from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous
    from .item.with_product_item_request_builder import WithProductItemRequestBuilder

class AdministratorRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /api/2.0/settings/security/administrator
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, Dict[str, Any]]) -> None:
        """
        Instantiates a new AdministratorRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/api/2.0/settings/security/administrator{?productid*,userid*}", path_parameters)
    
    def by_productid(self,productid: UUID) -> WithProductItemRequestBuilder:
        """
        Gets an item from the client.api.TwoZero.settings.security.administrator.item collection
        param productid: Product ID
        Returns: WithProductItemRequestBuilder
        """
        if productid is None:
            raise TypeError("productid cannot be null.")
        from .item.with_product_item_request_builder import WithProductItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["productid"] = productid
        return WithProductItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[AdministratorRequestBuilderGetQueryParameters]] = None) -> Optional[SuccessApiResponseOfAnonymous]:
        """
        Checks if the selected user is a product administrator with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SuccessApiResponseOfAnonymous]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

        return await self.request_adapter.send_async(request_info, SuccessApiResponseOfAnonymous, None)
    
    async def put(self,body: SecurityRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[SuccessApiResponseOfAnonymous]:
        """
        Sets the selected user as a product administrator with the ID specified in the request.
        param body: Security request parameters
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SuccessApiResponseOfAnonymous]
        """
        if body is None:
            raise TypeError("body cannot be null.")
        request_info = self.to_put_request_information(
            body, request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.success_api_response_of_anonymous import SuccessApiResponseOfAnonymous

        return await self.request_adapter.send_async(request_info, SuccessApiResponseOfAnonymous, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[AdministratorRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Checks if the selected user is a product administrator with the ID specified in the request.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json, text/plain;q=0.9")
        return request_info
    
    def to_put_request_information(self,body: SecurityRequestsDto, request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Sets the selected user as a product administrator with the ID specified in the request.
        param body: Security request parameters
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
    
    def with_url(self,raw_url: str) -> AdministratorRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: AdministratorRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return AdministratorRequestBuilder(self.request_adapter, raw_url)
    
    from uuid import UUID

    @dataclass
    class AdministratorRequestBuilderGetQueryParameters():
        from uuid import UUID

        """
        Checks if the selected user is a product administrator with the ID specified in the request.
        """
        # Product ID
        productid: Optional[UUID] = None

        # User ID
        userid: Optional[UUID] = None

    
    @dataclass
    class AdministratorRequestBuilderGetRequestConfiguration(RequestConfiguration[AdministratorRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    
    @dataclass
    class AdministratorRequestBuilderPutRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

