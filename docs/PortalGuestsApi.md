# docspace_api_sdk.GuestsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_guest_sharing_link**](#get_guest_sharing_link) | **GET** /api/2.0/people/guests/{userid}/share | Get a guest sharing link


# **get_guest_sharing_link**
> StringWrapper get_guest_sharing_link(userid)

Builds a link that lets another member of the portal take over the caller's guest, so that the guest becomes
visible to them as well.
The account in the route has to exist and be a guest - any other type is rejected with 400 - and the caller
has to be able to see it and must not be a guest itself.
The call is read-only: it only mints the link and changes nothing, and it can be repeated as often as needed.
The answer is a shortened confirmation URL as plain text; hand it to the person who should get the guest, and
their client completes the hand-over with `POST api/2.0/people/guests/share/approve`.
The link carries a confirmation token and therefore expires, so mint it when it is about to be used rather
than storing it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The ID of the guest to be handed over, taken from the route. The account has to exist, has to be a guest, and  has to be one the caller can see. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.GuestsApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the guest to be handed over, taken from the route. The account has to exist, has to be a guest, and  has to be one the caller can see.

    try:
        # Get a guest sharing link
        api_response = api_instance.get_guest_sharing_link(userid)
        print("The response of GuestsApi->get_guest_sharing_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestsApi->get_guest_sharing_link: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The shortened confirmation link, as plain text |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The account is not a guest |  -  |
**403** | The caller is a guest, or is not allowed to see that account |  -  |
**404** | No account has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

