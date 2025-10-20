# docspace_api_sdk.CSPApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_csp**](#configure_csp) | **POST** /api/2.0/security/csp | Configure CSP settings
[**get_csp_settings**](#get_csp_settings) | **GET** /api/2.0/security/csp | Get CSP settings


# **configure_csp**
> CspWrapper configure_csp(csp_requests_dto=csp_requests_dto)

Configures the CSP (Content Security Policy) settings for the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **csp_requests_dto** | [**CspRequestsDto**](CspRequestsDto.md)|  | [optional] 

### Return type

[**CspWrapper**](CspWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.csp_requests_dto import CspRequestsDto
from docspace_api_sdk.models.csp_wrapper import CspWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.CSPApi(api_client)
    csp_requests_dto = docspace_api_sdk.CspRequestsDto() # CspRequestsDto |  (optional)

    try:
        # Configure CSP settings
        api_response = api_instance.configure_csp(csp_requests_dto=csp_requests_dto)
        print("The response of CSPApi->configure_csp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSPApi->configure_csp: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Exception in Domains |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csp_settings**
> CspWrapper get_csp_settings()

Returns the CSP (Content Security Policy) settings for the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CspWrapper**](CspWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.csp_wrapper import CspWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.CSPApi(api_client)

    try:
        # Get CSP settings
        api_response = api_instance.get_csp_settings()
        print("The response of CSPApi->get_csp_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CSPApi->get_csp_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

