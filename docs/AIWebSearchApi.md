# docspace_api_sdk.WebSearchApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_web_search_clear**](#ai_web_search_clear) | **DELETE** /api/2.0/ai/web-search/clear | Clear
[**ai_web_search_configure**](#ai_web_search_configure) | **PUT** /api/2.0/ai/web-search/configure | Configure
[**ai_web_search_get_active_config**](#ai_web_search_get_active_config) | **GET** /api/2.0/ai/web-search/get-active-config | Get active config
[**ai_web_search_is_configured**](#ai_web_search_is_configured) | **GET** /api/2.0/ai/web-search/is-configured | Is configured
[**ai_web_search_passthrough_contents**](#ai_web_search_passthrough_contents) | **POST** /api/2.0/ai/websearch/v1/contents | Web page contents proxied to the portal's active web-search provider
[**ai_web_search_passthrough_search**](#ai_web_search_passthrough_search) | **POST** /api/2.0/ai/websearch/v1/search | Web search proxied to the portal's active web-search provider
[**ai_web_search_set_active_config**](#ai_web_search_set_active_config) | **PUT** /api/2.0/ai/web-search/set-active-config | Set active config
[**ai_web_search_test_connection**](#ai_web_search_test_connection) | **POST** /api/2.0/ai/web-search/test-connection | Test connection


# **ai_web_search_clear**
> AiSuccessResponse ai_web_search_clear(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    body = 'body_example' # str | 

    try:
        # Clear
        api_response = api_instance.ai_web_search_clear(body)
        print("The response of WebSearchApi->ai_web_search_clear:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_clear: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_configure**
> AiWebSearchMutationResult ai_web_search_configure(ai_web_search_configure_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_web_search_configure_request** | [**AiWebSearchConfigureRequest**](AiWebSearchConfigureRequest.md)|  | 

### Return type

[**AiWebSearchMutationResult**](AiWebSearchMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_web_search_configure_request import AiWebSearchConfigureRequest
from docspace_api_sdk.models.ai_web_search_mutation_result import AiWebSearchMutationResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    ai_web_search_configure_request = docspace_api_sdk.AiWebSearchConfigureRequest() # AiWebSearchConfigureRequest | 

    try:
        # Configure
        api_response = api_instance.ai_web_search_configure(ai_web_search_configure_request)
        print("The response of WebSearchApi->ai_web_search_configure:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_configure: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_get_active_config**
> AiWebSearchConfig ai_web_search_get_active_config(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

[**AiWebSearchConfig**](AiWebSearchConfig.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_web_search_config import AiWebSearchConfig
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # Get active config
        api_response = api_instance.ai_web_search_get_active_config(entity_id)
        print("The response of WebSearchApi->ai_web_search_get_active_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_get_active_config: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_is_configured**
> bool ai_web_search_is_configured(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**bool**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # Is configured
        api_response = api_instance.ai_web_search_is_configured(entity_id)
        print("The response of WebSearchApi->ai_web_search_is_configured:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_is_configured: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_passthrough_contents**
> AiSuccessResponse ai_web_search_passthrough_contents(request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Web page contents proxied to the portal's active web-search provider
        api_response = api_instance.ai_web_search_passthrough_contents(request_body)
        print("The response of WebSearchApi->ai_web_search_passthrough_contents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_passthrough_contents: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_passthrough_search**
> AiSuccessResponse ai_web_search_passthrough_search(request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, object]**](object.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    request_body = None # Dict[str, object] | 

    try:
        # Web search proxied to the portal's active web-search provider
        api_response = api_instance.ai_web_search_passthrough_search(request_body)
        print("The response of WebSearchApi->ai_web_search_passthrough_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_passthrough_search: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_set_active_config**
> AiSuccessResponse ai_web_search_set_active_config(ai_web_search_configure_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_web_search_configure_request** | [**AiWebSearchConfigureRequest**](AiWebSearchConfigureRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.models.ai_web_search_configure_request import AiWebSearchConfigureRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    ai_web_search_configure_request = docspace_api_sdk.AiWebSearchConfigureRequest() # AiWebSearchConfigureRequest | 

    try:
        # Set active config
        api_response = api_instance.ai_web_search_set_active_config(ai_web_search_configure_request)
        print("The response of WebSearchApi->ai_web_search_set_active_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_set_active_config: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_test_connection**
> AiProfilesTestConnection200Response ai_web_search_test_connection(ai_web_search_config)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_web_search_config** | [**AiWebSearchConfig**](AiWebSearchConfig.md)|  | 

### Return type

[**AiProfilesTestConnection200Response**](AiProfilesTestConnection200Response.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_profiles_test_connection200_response import AiProfilesTestConnection200Response
from docspace_api_sdk.models.ai_web_search_config import AiWebSearchConfig
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    ai_web_search_config = docspace_api_sdk.AiWebSearchConfig() # AiWebSearchConfig | 

    try:
        # Test connection
        api_response = api_instance.ai_web_search_test_connection(ai_web_search_config)
        print("The response of WebSearchApi->ai_web_search_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WebSearchApi->ai_web_search_test_connection: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

