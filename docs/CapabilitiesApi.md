# docspace_api_sdk.CapabilitiesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portal_capabilities**](#get_portal_capabilities) | **GET** /api/2.0/capabilities | Get portal capabilities


# **get_portal_capabilities**
> CapabilitiesWrapper get_portal_capabilities()

Returns the sign-in methods this portal offers, which a login client needs before anyone has signed in: LDAP
authentication and its domain, the external identity providers to show, the SAML single sign-on URL and its
label, and whether the built-in identity server is available. No token is needed and nothing has to be called
first - the operation is open to unauthenticated callers, answers even while the portal's payment has lapsed,
and is read-only and idempotent. `providers` holds provider keys such as `google` or `facebook`, ordered for
the country detected from the caller's IP address and reduced to the ones this installation has configured;
pass one of them as `provider` to `POST api/2.0/authentication`. An empty `providers` means external sign-in
is off and an empty `ssoUrl` means single sign-on is off; a capability whose settings cannot be read is
reported as disabled rather than failing the call, so a false flag means the method is not offered, not that
it is unknown. The answer describes the portal and never a user, and carries none of the configuration behind
these methods: an administrator reads that from `GET api/2.0/settings/ssov2` and
`GET api/2.0/settings/authservice`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CapabilitiesWrapper**](CapabilitiesWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.capabilities_wrapper import CapabilitiesWrapper
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
    api_instance = docspace_api_sdk.CapabilitiesApi(api_client)

    try:
        # Get portal capabilities
        api_response = api_instance.get_portal_capabilities()
        print("The response of CapabilitiesApi->get_portal_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CapabilitiesApi->get_portal_capabilities: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The sign-in methods the portal offers: LDAP, the external identity providers, single sign-on and the identity server, each with the state it has for this portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

