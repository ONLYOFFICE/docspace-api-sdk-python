# docspace_api_sdk.WebSearchApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_web_search_clear**](#ai_web_search_clear) | **DELETE** /api/2.0/ai/web-search/clear | Clear the web-search configuration
[**ai_web_search_configure**](#ai_web_search_configure) | **PUT** /api/2.0/ai/web-search/configure | Configure and verify web search
[**ai_web_search_get_active_config**](#ai_web_search_get_active_config) | **GET** /api/2.0/ai/web-search/get-active-config | Get active config
[**ai_web_search_is_configured**](#ai_web_search_is_configured) | **GET** /api/2.0/ai/web-search/is-configured | Is configured
[**ai_web_search_passthrough_contents**](#ai_web_search_passthrough_contents) | **POST** /api/2.0/ai/websearch/v1/contents | Web page contents passthrough
[**ai_web_search_passthrough_search**](#ai_web_search_passthrough_search) | **POST** /api/2.0/ai/websearch/v1/search | Web search passthrough
[**ai_web_search_set_active_config**](#ai_web_search_set_active_config) | **PUT** /api/2.0/ai/web-search/set-active-config | Set active config
[**ai_web_search_test_connection**](#ai_web_search_test_connection) | **POST** /api/2.0/ai/web-search/test-connection | Test a web-search provider


# **ai_web_search_clear**
> AiSuccessResponse ai_web_search_clear(body)

Removes the portal's web-search configuration, after which web search is unavailable everywhere it was not configured separately. This is not scoped: it takes no `entityId` and any body sent with it is ignored, so it cannot be used to clear one room's configuration. Clearing an already-unconfigured portal is not an error and the call answers success either way. The stored provider key is destroyed with the configuration and has to be entered again.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**| Ignored. The operation always clears the portal-wide configuration, so send an empty body; a value here does not scope it to a room. | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    body = 'body_example' # str | Ignored. The operation always clears the portal-wide configuration, so send an empty body; a value here does not scope it to a room.

    try:
        # Clear the web-search configuration
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
**200** | Confirms the portal has no web-search configuration any more. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_configure**
> AiWebSearchMutationResult ai_web_search_configure(ai_web_search_configure_request)

Validates a web-search configuration against the live provider and stores it only if the provider answers, which makes it the safe way to save a form in one step. `entityId` scopes the configuration to a room and has to name one the caller can open; omitting it configures the portal. A `baseUrl` pointing at a private network address is refused. Use `PUT api/2.0/ai/web-search/set-active-config` when the configuration should be stored without a provider round trip.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_web_search_configure_request** | [**AiWebSearchConfigureRequest**](AiWebSearchConfigureRequest.md)|  | 

### Return type

[**AiWebSearchMutationResult**](AiWebSearchMutationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    ai_web_search_configure_request = docspace_api_sdk.AiWebSearchConfigureRequest() # AiWebSearchConfigureRequest | 

    try:
        # Configure and verify web search
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
**200** | Whether the configuration was stored, after the provider answered. |  -  |
**400** | The configuration is missing or malformed, or the provider URL points at a private network address. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | The referenced object does not exist, or the caller cannot access it - the two are deliberately indistinguishable, so a room the caller may not open answers 404 rather than 403. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_get_active_config**
> AiWebSearchConfig ai_web_search_get_active_config(entity_id=entity_id)

Returns the web-search configuration in force for a scope - the provider, its endpoint and its settings. `entityId` picks a room and has to name one the caller can open; omitting it reads the portal-wide configuration, and a room with none of its own falls back to that. An unconfigured scope answers an empty result rather than 404. The provider key is not part of the answer, so a client cannot read it back after storing it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

[**AiWebSearchConfig**](AiWebSearchConfig.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_web_search_config import AiWebSearchConfig
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get active config
        api_response = api_instance.ai_web_search_get_active_config(entity_id=entity_id)
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
**200** | The configuration in force for the scope, without the provider key, or an empty result when web search is not configured. |  -  |
**400** | `entityId` is not a string. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | The referenced object does not exist, or the caller cannot access it - the two are deliberately indistinguishable, so a room the caller may not open answers 404 rather than 403. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_is_configured**
> bool ai_web_search_is_configured(entity_id=entity_id)

Tells whether web search is available in a scope, as a bare boolean, which is the cheap check for hiding or showing the feature. `entityId` picks a room and has to name one the caller can open. It reports the same state as `GET api/2.0/ai/web-search/get-active-config` without transferring the configuration itself. A true answer means a provider is stored, not that the provider is currently reachable - probe that with `POST api/2.0/ai/web-search/test-connection`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**bool**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Is configured
        api_response = api_instance.ai_web_search_is_configured(entity_id=entity_id)
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
**200** | Whether a web-search provider is stored for the scope. |  -  |
**400** | `entityId` is not a string. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | The referenced object does not exist, or the caller cannot access it - the two are deliberately indistinguishable, so a room the caller may not open answers 404 rather than 403. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_passthrough_contents**
> Dict[str, object] ai_web_search_passthrough_contents(request_body)

Fetches the contents of web pages on behalf of the document editor's AI plugin, against the portal's active web-search provider, exactly as the search passthrough does — including the `entityId` / `entityKind` billing attribution. The portal-wide configuration is used and a portal without one answers 404. The provider's status, body and content type are relayed verbatim, so its 429 and its failures surface unchanged. This is the follow-up to `POST api/2.0/ai/websearch/v1/search`, which returns the results whose contents this operation retrieves.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, Optional[object]]**](object.md)| A page-contents request in the shape the portal's active web-search provider expects, forwarded to it unchanged. The endpoint and the key come from the stored configuration. | 

### Return type

**Dict[str, object]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    request_body = None # Dict[str, Optional[object]] | A page-contents request in the shape the portal's active web-search provider expects, forwarded to it unchanged. The endpoint and the key come from the stored configuration.

    try:
        # Web page contents passthrough
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
**200** | The provider's own response, relayed verbatim with its status and content type. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | Web search is not configured for this portal. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**429** | Relayed verbatim from the AI provider, which is rate-limiting this portal's key. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The AI provider could not be reached, or answered with a failure of its own. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_passthrough_search**
> Dict[str, object] ai_web_search_passthrough_search(request_body)

Runs a web search on behalf of the document editor's AI plugin, which holds only a placeholder configuration - the portal's active provider and its key are resolved here, so neither ever reaches the browser. The portal-wide configuration is used, and a portal without one answers 404. The `entityId` and `entityKind` query parameters name the document the search is billed to; with the ONLYOFFICE provider the entry is resolved under the caller's credentials and sent to the gateway as the request `metadata` (`source_id` / `source_type` / `source_title`), and an entry the caller cannot open sends none. The provider's own status, body and content type are relayed as they stand, so a provider that rate-limits answers 429 and one that is unreachable answers 502. Closing the connection aborts the upstream request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, Optional[object]]**](object.md)| A search request in the shape the portal's active web-search provider expects, forwarded to it unchanged. The endpoint and the key come from the stored configuration and must not be sent here. | 

### Return type

**Dict[str, object]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    request_body = None # Dict[str, Optional[object]] | A search request in the shape the portal's active web-search provider expects, forwarded to it unchanged. The endpoint and the key come from the stored configuration and must not be sent here.

    try:
        # Web search passthrough
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
**200** | The provider's own response, relayed verbatim with its status and content type. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | Web search is not configured for this portal. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**429** | Relayed verbatim from the AI provider, which is rate-limiting this portal's key. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |
**502** | The AI provider could not be reached, or answered with a failure of its own. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_set_active_config**
> AiSuccessResponse ai_web_search_set_active_config(ai_web_search_configure_request)

Stores a web-search configuration without contacting the provider first, for a form that has already validated its input or for restoring a known-good configuration. `entityId` scopes it to a room and has to name one the caller can open. A `baseUrl` pointing at a private network address is still refused, because that check is local. Nothing guarantees the stored provider works: follow up with `POST api/2.0/ai/web-search/test-connection`, or use `PUT api/2.0/ai/web-search/configure` to have the store gated on a live probe.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_web_search_configure_request** | [**AiWebSearchConfigureRequest**](AiWebSearchConfigureRequest.md)|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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
**200** | Confirms the configuration was stored, unverified. |  -  |
**400** | The configuration is missing or malformed, or the provider URL points at a private network address. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | The referenced object does not exist, or the caller cannot access it - the two are deliberately indistinguishable, so a room the caller may not open answers 404 rather than 403. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_web_search_test_connection**
> AiProfilesTestConnection200Response ai_web_search_test_connection(ai_web_search_config)

Probes a web-search configuration against the live provider and reports the outcome, storing nothing - this is what a Test button calls so that a failure commits no state. The configuration is taken from the request rather than from storage, so credentials that were never saved can be checked. A `baseUrl` pointing at a private network address is refused before any request leaves the portal. The verdict is carried in the body rather than in the status, so a failed probe still answers 200 and the caller has to read the payload.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_web_search_config** | [**AiWebSearchConfig**](AiWebSearchConfig.md)|  | 

### Return type

[**AiProfilesTestConnection200Response**](AiProfilesTestConnection200Response.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.WebSearchApi(api_client)
    ai_web_search_config = docspace_api_sdk.AiWebSearchConfig() # AiWebSearchConfig | 

    try:
        # Test a web-search provider
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
**200** | The outcome of the probe. A failed probe is reported here, not as a status. |  -  |
**400** | The configuration is missing or malformed, or the provider URL points at a private network address. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

