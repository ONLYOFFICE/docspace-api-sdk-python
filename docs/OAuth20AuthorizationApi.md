# docspace.OAuth20AuthorizationApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth2_authorize_get**](OAuth20AuthorizationApi.md#oauth2_authorize_get) | **GET** /oauth2/authorize | OAuth2 authorization endpoint
[**oauth2_authorize_post**](OAuth20AuthorizationApi.md#oauth2_authorize_post) | **POST** /oauth2/authorize | OAuth2 consent endpoint
[**oauth2_token_post**](OAuth20AuthorizationApi.md#oauth2_token_post) | **POST** /oauth2/token | OAuth2 token endpoint


# **oauth2_authorize_get**
> oauth2_authorize_get(response_type, client_id, redirect_uri, scope)

OAuth2 authorization endpoint

Initiates the OAuth2 authorization flow.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.OAuth20AuthorizationApi(api_client)
    response_type = 'code' # str | The OAuth 2.0 response type, must be 'code' for authorization code flow.
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The client identifier issued to the client during registration.
    redirect_uri = 'https://example.com' # str | The URL to redirect to after authorization is complete.
    scope = 'files:read' # str | The space-separated list of requested scope permissions.

    try:
        # OAuth2 authorization endpoint
        api_instance.oauth2_authorize_get(response_type, client_id, redirect_uri, scope)
    except Exception as e:
        print("Exception when calling OAuth20AuthorizationApi->oauth2_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**| The OAuth 2.0 response type, must be &#39;code&#39; for authorization code flow. | 
 **client_id** | **str**| The client identifier issued to the client during registration. | 
 **redirect_uri** | **str**| The URL to redirect to after authorization is complete. | 
 **scope** | **str**| The space-separated list of requested scope permissions. | 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization page |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_authorize_post**
> oauth2_authorize_post(client_id=client_id, state=state, scope=scope)

OAuth2 consent endpoint

Sends a consent request with the specified parameters.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.OAuth20AuthorizationApi(api_client)
    client_id = 'client_id_example' # str | The client identifier issued to the client during registration. (optional)
    state = 'state_example' # str | The random string used to solve the CSRF vulnerability problem. (optional)
    scope = 'scope_example' # str | The space-separated list of requested scope permissions. (optional)

    try:
        # OAuth2 consent endpoint
        api_instance.oauth2_authorize_post(client_id=client_id, state=state, scope=scope)
    except Exception as e:
        print("Exception when calling OAuth20AuthorizationApi->oauth2_authorize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client identifier issued to the client during registration. | [optional] 
 **state** | **str**| The random string used to solve the CSRF vulnerability problem. | [optional] 
 **scope** | **str**| The space-separated list of requested scope permissions. | [optional] 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the client&#39;s redirect URI with authorization code |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth2_token_post**
> Oauth2TokenPost200Response oauth2_token_post(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)

OAuth2 token endpoint

Exchanges an authorization code specified in the request for the access token.

### Example


```python
import docspace
from docspace.models.oauth2_token_post200_response import Oauth2TokenPost200Response
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.OAuth20AuthorizationApi(api_client)
    grant_type = 'grant_type_example' # str | The OAuth2 grant type, must be 'authorization_code' for the authorization code flow. (optional)
    code = 'code_example' # str | A temporary authorization code that is sent to the client to be exchanged for a token. (optional)
    redirect_uri = 'redirect_uri_example' # str | The URL where the user will be redirected after successful or unsuccessful authentication. (optional)
    client_id = 'client_id_example' # str | The client identifier issued to the client during registration. (optional)
    client_secret = 'client_secret_example' # str | The client secret issued to the client during registration. (optional)

    try:
        # OAuth2 token endpoint
        api_response = api_instance.oauth2_token_post(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)
        print("The response of OAuth20AuthorizationApi->oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20AuthorizationApi->oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The OAuth2 grant type, must be &#39;authorization_code&#39; for the authorization code flow. | [optional] 
 **code** | **str**| A temporary authorization code that is sent to the client to be exchanged for a token. | [optional] 
 **redirect_uri** | **str**| The URL where the user will be redirected after successful or unsuccessful authentication. | [optional] 
 **client_id** | **str**| The client identifier issued to the client during registration. | [optional] 
 **client_secret** | **str**| The client secret issued to the client during registration. | [optional] 

### Return type

[**Oauth2TokenPost200Response**](Oauth2TokenPost200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authorization code was successfully exchanged for the access token |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

