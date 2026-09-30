# docspace_api_sdk.IPRestrictionsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_ip_restrictions**](#get_ip_restrictions) | **GET** /api/2.0/settings/iprestrictions | Get IP restrictions
[**read_ip_restrictions_settings**](#read_ip_restrictions_settings) | **GET** /api/2.0/settings/iprestrictions/settings | Get IP restriction settings
[**save_ip_restrictions**](#save_ip_restrictions) | **PUT** /api/2.0/settings/iprestrictions | Save IP restrictions
[**update_ip_restrictions_settings**](#update_ip_restrictions_settings) | **PUT** /api/2.0/settings/iprestrictions/settings | Update IP restriction settings


# **get_ip_restrictions**
> IPRestrictionArrayWrapper get_ip_restrictions()

Returns the IP restriction list of the current portal - the addresses allowed to reach it, each with its `id`
and the `forAdmin` flag that narrows the entry to DocSpace administrators. The caller needs the
portal-settings right of a DocSpace administrator, otherwise the call is refused. The call is read-only and
honours `If-None-Match`: send back the `ETag` of an earlier answer and an unchanged list comes back as an
empty not-modified response rather than a body. The list has no defined order and is empty on a portal where
nobody has configured restrictions - and an empty list blocks nobody, whatever the enforcement flag says.
Whether the restrictions are enforced at all is not part of this answer: read that flag with
`GET api/2.0/settings/iprestrictions/settings`. The entries listed here apply to every user of the portal
except its owner. Replace the whole list with `PUT api/2.0/settings/iprestrictions`; single entries cannot be
added or deleted, and that update takes plain addresses rather than the IDs returned here.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**IPRestrictionArrayWrapper**](IPRestrictionArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restriction_array_wrapper import IPRestrictionArrayWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)

    try:
        # Get IP restrictions
        api_response = api_instance.get_ip_restrictions()
        print("The response of IPRestrictionsApi->get_ip_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->get_ip_restrictions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The IP addresses allowed to reach the portal, each with its ID and administrators-only flag; an empty list when the portal has no restrictions |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **read_ip_restrictions_settings**
> IPRestrictionsSettingsWrapper read_ip_restrictions_settings()

Reports whether the IP restrictions of the current portal are enforced, as the `enable` flag together with the
`lastModified` stamp of the setting. The caller needs the portal-settings right of a DocSpace administrator,
otherwise the call is refused. The call is read-only and honours `If-Modified-Since`: send back the
`Last-Modified` value of an earlier answer and an unchanged setting comes back as an empty not-modified
response rather than a body. The flag is `false` on a portal nobody has configured. A `true` flag on its own
blocks nothing: enforcement also needs at least one stored address, which this answer does not carry - read
the addresses with `GET api/2.0/settings/iprestrictions` - and it is skipped entirely on an installation whose
configuration hides the IP security section. Even when enforced, the portal owner and the installation's own
networks are let through. Change the flag with `PUT api/2.0/settings/iprestrictions/settings`, which replaces
the address list in the same call, so resend the addresses in force when all that changes is the flag.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**IPRestrictionsSettingsWrapper**](IPRestrictionsSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restrictions_settings_wrapper import IPRestrictionsSettingsWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)

    try:
        # Get IP restriction settings
        api_response = api_instance.read_ip_restrictions_settings()
        print("The response of IPRestrictionsApi->read_ip_restrictions_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->read_ip_restrictions_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The enforcement flag of the IP restrictions and the date the setting was last modified |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_ip_restrictions**
> IpRestrictionsWrapper save_ip_restrictions(ip_restrictions_dto=ip_restrictions_dto)

Replaces the whole IP restriction list of the current portal with the addresses from the request and stores
the enforcement flag in the same call. The caller needs the portal-settings right of a DocSpace administrator,
otherwise the call is refused. Every entry must be a single IPv4 or IPv6 address: `from-to` ranges and CIDR
blocks are matched by the portal but cannot be stored here and are rejected as an invalid request, as is
`enable: true` with an empty list. An omitted `enable` follows the list - on when addresses are sent, off when
the list is empty. The replacement is written in one transaction, applies to new requests without a restart
and is recorded in the audit trail; entries not repeated in the body are deleted, and sending the same body
twice leaves the portal as it is. Enforcement spares the portal owner and the installation's own networks
only, so a list without the caller's own address locks the remaining administrators out. The answer echoes the
request rather than the stored rows - no entry IDs, and `enable` exactly as sent, empty when it was omitted -
so read the result with `GET api/2.0/settings/iprestrictions`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_restrictions_dto** | [**IpRestrictionsDto**](IpRestrictionsDto.md)|  | [optional] 

### Return type

[**IpRestrictionsWrapper**](IpRestrictionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restrictions_dto import IpRestrictionsDto
from docspace_api_sdk.models.ip_restrictions_wrapper import IpRestrictionsWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)
    ip_restrictions_dto = docspace_api_sdk.IpRestrictionsDto() # IpRestrictionsDto |  (optional)

    try:
        # Save IP restrictions
        api_response = api_instance.save_ip_restrictions(ip_restrictions_dto=ip_restrictions_dto)
        print("The response of IPRestrictionsApi->save_ip_restrictions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->save_ip_restrictions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The saved addresses and enforcement flag echoed back exactly as sent, without the IDs of the stored entries |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_ip_restrictions_settings**
> IpRestrictionsWrapper update_ip_restrictions_settings(ip_restrictions_dto=ip_restrictions_dto)

Stores the enforcement flag of the IP restrictions of the current portal together with the whole address list,
replacing the addresses saved before; this operation and `PUT api/2.0/settings/iprestrictions` are two routes
to the same handler and behave identically. The caller needs the portal-settings right of a DocSpace
administrator, otherwise the call is refused. Every entry must be a single IPv4 or IPv6 address: `from-to`
ranges and CIDR blocks are matched by the portal but cannot be stored here and are rejected as an invalid
request, as is `enable: true` with an empty list. An omitted `enable` follows the list - on when addresses are
sent, off when the list is empty - so the flag cannot be moved without resending the addresses that stay in
force. The new state applies to new requests without a restart, is recorded in the audit trail, and sending
the same body twice changes nothing further. Enforcement spares the portal owner and the installation's own
networks only, so a list without the caller's own address locks the remaining administrators out. The answer
echoes the request, so read the stored entries and their IDs with `GET api/2.0/settings/iprestrictions`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip_restrictions_dto** | [**IpRestrictionsDto**](IpRestrictionsDto.md)|  | [optional] 

### Return type

[**IpRestrictionsWrapper**](IpRestrictionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ip_restrictions_dto import IpRestrictionsDto
from docspace_api_sdk.models.ip_restrictions_wrapper import IpRestrictionsWrapper
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
    api_instance = docspace_api_sdk.IPRestrictionsApi(api_client)
    ip_restrictions_dto = docspace_api_sdk.IpRestrictionsDto() # IpRestrictionsDto |  (optional)

    try:
        # Update IP restriction settings
        api_response = api_instance.update_ip_restrictions_settings(ip_restrictions_dto=ip_restrictions_dto)
        print("The response of IPRestrictionsApi->update_ip_restrictions_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPRestrictionsApi->update_ip_restrictions_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stored enforcement flag and addresses echoed back exactly as sent, without the IDs of the stored entries |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

