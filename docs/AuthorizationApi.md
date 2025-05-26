# docspace.AuthorizationApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth2_authorize_get**](AuthorizationApi.md#oauth2_authorize_get) | **GET** /oauth2/authorize | OAuth2 Authorization Endpoint
[**oauth2_authorize_post**](AuthorizationApi.md#oauth2_authorize_post) | **POST** /oauth2/authorize | OAuth2 Consent Endpoint
[**oauth2_token_post**](AuthorizationApi.md#oauth2_token_post) | **POST** /oauth2/token | OAuth2 Token Endpoint


# **oauth2_authorize_get**
> oauth2_authorize_get(response_type, client_id, redirect_uri, scope)

OAuth2 Authorization Endpoint

Initiates the OAuth2 authorization flow

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
    api_instance = docspace.AuthorizationApi(api_client)
    response_type = 'code' # str | 
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | 
    redirect_uri = 'https://example.com' # str | 
    scope = 'files:read' # str | 

    try:
        # OAuth2 Authorization Endpoint
        api_instance.oauth2_authorize_get(response_type, client_id, redirect_uri, scope)
    except Exception as e:
        print("Exception when calling AuthorizationApi->oauth2_authorize_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**|  | 
 **client_id** | **str**|  | 
 **redirect_uri** | **str**|  | 
 **scope** | **str**|  | 

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

OAuth2 Consent Endpoint

Sends consent approval

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
    api_instance = docspace.AuthorizationApi(api_client)
    client_id = 'client_id_example' # str |  (optional)
    state = 'state_example' # str |  (optional)
    scope = 'scope_example' # str |  (optional)

    try:
        # OAuth2 Consent Endpoint
        api_instance.oauth2_authorize_post(client_id=client_id, state=state, scope=scope)
    except Exception as e:
        print("Exception when calling AuthorizationApi->oauth2_authorize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 
 **state** | **str**|  | [optional] 
 **scope** | **str**|  | [optional] 

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

OAuth2 Token Endpoint

Exchange authorization code for access token

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
    api_instance = docspace.AuthorizationApi(api_client)
    grant_type = 'grant_type_example' # str |  (optional)
    code = 'code_example' # str |  (optional)
    redirect_uri = 'redirect_uri_example' # str |  (optional)
    client_id = 'client_id_example' # str |  (optional)
    client_secret = 'client_secret_example' # str |  (optional)

    try:
        # OAuth2 Token Endpoint
        api_response = api_instance.oauth2_token_post(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)
        print("The response of AuthorizationApi->oauth2_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->oauth2_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**|  | [optional] 
 **code** | **str**|  | [optional] 
 **redirect_uri** | **str**|  | [optional] 
 **client_id** | **str**|  | [optional] 
 **client_secret** | **str**|  | [optional] 

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
**200** | Successfully exchanged authorization code for access token |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

