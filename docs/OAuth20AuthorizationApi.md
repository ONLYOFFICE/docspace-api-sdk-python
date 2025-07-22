# docspace-api-sdk.OAuth20AuthorizationApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_o_auth**](#authorize_o_auth) | **GET** /oauth2/authorize | OAuth2 authorization endpoint
[**exchange_token**](#exchange_token) | **POST** /oauth2/token | OAuth2 token endpoint
[**submit_consent**](#submit_consent) | **POST** /oauth2/authorize | OAuth2 consent endpoint


# **authorize_o_auth**
> authorize_o_auth(response_type, client_id, redirect_uri, scope)

Initiates the OAuth2 authorization flow.

For more information, see [api.onlyoffice.com]().

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

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
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
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.OAuth20AuthorizationApi(api_client)
    response_type = 'code' # str | The OAuth 2.0 response type, must be 'code' for authorization code flow.
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The client identifier issued to the client during registration.
    redirect_uri = 'https://example.com' # str | The URL to redirect to after authorization is complete.
    scope = 'files:read' # str | The space-separated list of requested scope permissions.

    try:
        # OAuth2 authorization endpoint
        api_instance.authorize_o_auth(response_type, client_id, redirect_uri, scope)
    except Exception as e:
        print("Exception when calling OAuth20AuthorizationApi->authorize_o_auth: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authorization page |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_token**
> ExchangeToken200Response exchange_token(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)

Exchanges an authorization code specified in the request for the access token.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| The OAuth2 grant type, must be &#39;authorization_code&#39; for the authorization code flow. | [optional] 
 **code** | **str**| A temporary authorization code that is sent to the client to be exchanged for a token. | [optional] 
 **redirect_uri** | **str**| The URL where the user will be redirected after successful or unsuccessful authentication. | [optional] 
 **client_id** | **str**| The client identifier issued to the client during registration. | [optional] 
 **client_secret** | **str**| The client secret issued to the client during registration. | [optional] 

### Return type

[**ExchangeToken200Response**](ExchangeToken200Response.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.exchange_token200_response import ExchangeToken200Response
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.OAuth20AuthorizationApi(api_client)
    grant_type = 'grant_type_example' # str | The OAuth2 grant type, must be 'authorization_code' for the authorization code flow. (optional)
    code = 'code_example' # str | A temporary authorization code that is sent to the client to be exchanged for a token. (optional)
    redirect_uri = 'redirect_uri_example' # str | The URL where the user will be redirected after successful or unsuccessful authentication. (optional)
    client_id = 'client_id_example' # str | The client identifier issued to the client during registration. (optional)
    client_secret = 'client_secret_example' # str | The client secret issued to the client during registration. (optional)

    try:
        # OAuth2 token endpoint
        api_response = api_instance.exchange_token(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)
        print("The response of OAuth20AuthorizationApi->exchange_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20AuthorizationApi->exchange_token: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The authorization code was successfully exchanged for the access token |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_consent**
> submit_consent(client_id=client_id, state=state, scope=scope)

Sends a consent request with the specified parameters.

For more information, see [api.onlyoffice.com]().

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

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
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
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.OAuth20AuthorizationApi(api_client)
    client_id = 'client_id_example' # str | The client identifier issued to the client during registration. (optional)
    state = 'state_example' # str | The random string used to solve the CSRF vulnerability problem. (optional)
    scope = 'scope_example' # str | The space-separated list of requested scope permissions. (optional)

    try:
        # OAuth2 consent endpoint
        api_instance.submit_consent(client_id=client_id, state=state, scope=scope)
    except Exception as e:
        print("Exception when calling OAuth20AuthorizationApi->submit_consent: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the client&#39;s redirect URI with authorization code |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

