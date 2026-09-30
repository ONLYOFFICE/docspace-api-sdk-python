# docspace_api_sdk.AuthorizationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authorize_o_auth**](#authorize_o_auth) | **GET** /oauth2/authorize | Start the authorization flow
[**exchange_token**](#exchange_token) | **POST** /oauth2/token | Exchange the authorization code
[**submit_consent**](#submit_consent) | **POST** /oauth2/authorize | Submit the consent decision


# **authorize_o_auth**
> authorize_o_auth(response_type, client_id, redirect_uri, scope)

Starts the OAuth2 authorization code flow for the client named by client_id. The caller has to present the portal signature cookie, and a request without a valid one is not refused with 401 or 403 but redirected to the portal login page, carrying the client ID so the flow can resume after signing in. When the user has not yet consented to the requested scopes the browser is redirected to the consent page; once the consent exists the browser is redirected to the client's redirect URI with the authorization code and, when one was sent, the original state. A caller that cannot follow redirects may send the X-Disable-Redirect header, and then the response is 200 with an empty body and the target URL in the X-Redirect-URI header. The code returned here is exchanged for tokens at the token endpoint.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **response_type** | **str**| The OAuth 2.0 response type. Only code is supported: this server issues an authorization code, never a token, from this endpoint. | 
 **client_id** | **str**| The identifier the client was given when it was registered. It selects both the client shown on the consent screen and the set of redirect URIs the request is checked against. | 
 **redirect_uri** | **str**| Where to send the user once authorization is complete. It has to be one of the redirect URIs registered for the client, otherwise the request is refused. | 
 **scope** | **str**| The permissions being asked for, as a space-separated list. Every scope has to be one the client is registered for, and the consent screen lists exactly these. | 

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

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
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthorizationApi(api_client)
    response_type = 'code' # str | The OAuth 2.0 response type. Only code is supported: this server issues an authorization code, never a token, from this endpoint.
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The identifier the client was given when it was registered. It selects both the client shown on the consent screen and the set of redirect URIs the request is checked against.
    redirect_uri = 'https://example.com' # str | Where to send the user once authorization is complete. It has to be one of the redirect URIs registered for the client, otherwise the request is refused.
    scope = 'files:read' # str | The permissions being asked for, as a space-separated list. Every scope has to be one the client is registered for, and the consent screen lists exactly these.

    try:
        # Start the authorization flow
        api_instance.authorize_o_auth(response_type, client_id, redirect_uri, scope)
    except Exception as e:
        print("Exception when calling AuthorizationApi->authorize_o_auth: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the login page, to the consent page, or back to the client's redirect URI with an authorization code |  -  |
**200** | Returned instead of the redirect when the request carries the X-Disable-Redirect header: the target URL is sent in the X-Redirect-URI response header and the body is empty |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exchange_token**
> ExchangeToken200Response exchange_token(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)

Exchanges an authorization code for an access token. The request is form-encoded and has to carry the grant type, the code, the same redirect URI that was used to obtain the code, and the client credentials: the client authenticates itself here rather than through the portal signature cookie the authorization endpoint uses. The response carries the access token, its type and its lifetime in seconds, plus a refresh token when the client is configured for the refresh token grant. Client authentication that fails is answered with 401, while a malformed, unknown or expired code is answered with 400. The code is single use, so replaying it fails.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | **str**| Which exchange is being performed: authorization_code to redeem a code, refresh_token to renew an access token. | [optional] 
 **code** | **str**| The authorization code returned by the authorization endpoint. It may be redeemed once. | [optional] 
 **redirect_uri** | **str**| The same redirect URI that was used to obtain the code. The exchange fails when it differs. | [optional] 
 **client_id** | **str**| The identifier of the client redeeming the code. | [optional] 
 **client_secret** | **str**| The secret of the client redeeming the code. It is omitted by a public client, which proves itself with a PKCE code verifier instead. | [optional] 

### Return type

[**ExchangeToken200Response**](ExchangeToken200Response.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.exchange_token200_response import ExchangeToken200Response
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthorizationApi(api_client)
    grant_type = 'grant_type_example' # str | Which exchange is being performed: authorization_code to redeem a code, refresh_token to renew an access token. (optional)
    code = 'code_example' # str | The authorization code returned by the authorization endpoint. It may be redeemed once. (optional)
    redirect_uri = 'redirect_uri_example' # str | The same redirect URI that was used to obtain the code. The exchange fails when it differs. (optional)
    client_id = 'client_id_example' # str | The identifier of the client redeeming the code. (optional)
    client_secret = 'client_secret_example' # str | The secret of the client redeeming the code. It is omitted by a public client, which proves itself with a PKCE code verifier instead. (optional)

    try:
        # Exchange the authorization code
        api_response = api_instance.exchange_token(grant_type=grant_type, code=code, redirect_uri=redirect_uri, client_id=client_id, client_secret=client_secret)
        print("The response of AuthorizationApi->exchange_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthorizationApi->exchange_token: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully exchanged authorization code for access token |  -  |
**400** | Invalid request parameters |  -  |
**401** | Client authentication failed: the client ID is unknown or the client secret does not match |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_consent**
> submit_consent(client_id=client_id, state=state, scope=scope)

Submits the user's consent decision for the scopes an authorization request asked for. It is the form post the consent page makes, so it carries the client ID, the state and the agreed scopes as multipart form data, along with the same portal signature cookie the authorization request needed. On success the browser is redirected to the client's redirect URI with an authorization code, or, when the request carries the X-Disable-Redirect header, answered 200 with that URL in the X-Redirect-URI header. The consent is stored per user and client, so a later authorization request for the same scopes no longer stops at the consent page.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client the consent is being given to. It has to be the same client the authorization request named. | [optional] 
 **state** | **str**| The opaque value carried through from the authorization request, returned unchanged on the redirect so the client can match the answer to its request. | [optional] 
 **scope** | **str**| The scopes the user agreed to, as a space-separated list. Anything the user declined is left out, so this may be narrower than what was requested. | [optional] 

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

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
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthorizationApi(api_client)
    client_id = 'client_id_example' # str | The client the consent is being given to. It has to be the same client the authorization request named. (optional)
    state = 'state_example' # str | The opaque value carried through from the authorization request, returned unchanged on the redirect so the client can match the answer to its request. (optional)
    scope = 'scope_example' # str | The scopes the user agreed to, as a space-separated list. Anything the user declined is left out, so this may be narrower than what was requested. (optional)

    try:
        # Submit the consent decision
        api_instance.submit_consent(client_id=client_id, state=state, scope=scope)
    except Exception as e:
        print("Exception when calling AuthorizationApi->submit_consent: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | Redirect to the client's redirect URI with authorization code |  -  |
**200** | Returned instead of the redirect when the request carries the X-Disable-Redirect header: the target URL is sent in the X-Redirect-URI response header and the body is empty |  -  |
**400** | Invalid request parameters |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

