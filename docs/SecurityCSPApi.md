# docspace_api_sdk.CSPApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**configure_csp**](#configure_csp) | **POST** /api/2.0/security/csp | Configure CSP settings
[**get_csp_settings**](#get_csp_settings) | **GET** /api/2.0/security/csp | Get CSP settings


# **configure_csp**
> CspWrapper configure_csp(csp_requests_dto=csp_requests_dto)

Replaces the list of external domains the portal's Content Security Policy trusts and returns the policy
header the portal serves to browsers from that moment on. The list in `domains` replaces the stored one, so an
omitted or empty list falls back to the portal's built-in policy, and every entry that is sent becomes an
allowed source for scripts, styles, images, fonts, frames, media and connections at once. An entry may be a
host, a host with a scheme, or a wildcard host such as `*.example.com`; it has to form a valid absolute
address and may contain ASCII characters only, and an entry that does not is refused with 400 before anything
is saved. The caller needs the portal-settings right of a DocSpace administrator, and the request is also
refused with 403 when the header built from the list grows past the size configured for the installation, 15
KB by default. The change applies to the whole portal at once and is idempotent. Read the current state with
`GET api/2.0/security/csp`.

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
**200** | The stored domains and the policy header the portal now serves |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | An entry of `domains` is not a valid address or holds non-ASCII characters |  -  |
**403** | The caller does not have the portal-settings right of a DocSpace administrator, or the built policy header exceeds the size allowed for the installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_csp_settings**
> CspWrapper get_csp_settings()

Returns the Content Security Policy this portal serves: `domains`, the external hosts an administrator has
allowed, and `header`, the whole policy value built from them together with the portal's own defaults and the
integrations it has switched on. The operation is anonymous and reachable cross-origin - no token is needed -
because the login and editor front-ends read it before anyone has signed in. It is read-only for the caller,
but it does repair the portal's cached policy when the cache has lost it, so a call can rebuild the header
instead of only reading it. The answer honours `If-Modified-Since`: send back the `Last-Modified` value of an
earlier answer and an unchanged policy comes back as an empty not-modified response rather than a body.
`domains` is an empty list on a portal nobody has configured, while `header` is filled from the defaults even
then. Change the allowed domains with `POST api/2.0/security/csp`, which does need a DocSpace administrator.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CspWrapper**](CspWrapper.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
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
**200** | The allowed domains and the full policy header the portal serves |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

