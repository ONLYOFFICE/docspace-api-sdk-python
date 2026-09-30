# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_users_quota**](#reset_users_quota) | **PUT** /api/2.0/people/resetquota | Reset a user quota limit
[**update_user_quota**](#update_user_quota) | **PUT** /api/2.0/people/userquota | Change a user quota limit


# **reset_users_quota**
> EmployeeFullArrayWrapper reset_users_quota(update_members_quota_request_dto=update_members_quota_request_dto)

Drops the personal storage limit of the listed accounts, so that each of them follows the portal default
again.
The caller needs the permission to edit the portal settings, which in practice means a DocSpace
administrator or the portal owner.
On a hosted portal the tariff has to include the storage statistics feature, otherwise the operation answers
402; a standalone installation has no such condition.
It takes only `userIds` - the `quota` field of the request body is not read here - and system accounts are
dropped from the list without an error.
The accounts are processed one by one and the answer holds the ones that were reached, each already showing
the portal default as its limit.
Nothing is deleted and no space is freed; only the limit that applies changes.
Use `PUT api/2.0/people/userquota` to give an account its own limit instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_members_quota_request_dto** | [**UpdateMembersQuotaRequestDto**](UpdateMembersQuotaRequestDto.md)|  | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    update_members_quota_request_dto = docspace_api_sdk.UpdateMembersQuotaRequestDto() # UpdateMembersQuotaRequestDto |  (optional)

    try:
        # Reset a user quota limit
        api_response = api_instance.reset_users_quota(update_members_quota_request_dto=update_members_quota_request_dto)
        print("The response of QuotaApi->reset_users_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->reset_users_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The accounts that now follow the portal default limit |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The tariff of a hosted portal does not include the storage statistics feature |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_quota**
> EmployeeFullArrayWrapper update_user_quota(update_members_quota_request_dto=update_members_quota_request_dto)

Gives the listed accounts their own storage limit, replacing the portal default for each of them.
The caller needs the permission to edit the portal settings, which in practice means a DocSpace
administrator or the portal owner.
`quota` is a whole number of bytes: a value of 0 or more becomes the personal limit, while any negative value
switches the personal limit off and hands the account back to the portal default.
The value has to fit the portal: a limit larger than the total storage the tariff allows, or larger than the
portal-wide quota on a standalone installation, is rejected with 400, and so is a value that is not a whole
number.
System accounts are dropped from the list without an error, the accounts are processed one by one, and the
answer holds the ones that were reached.
Setting a limit does not free any space and does not delete anything: an account already over its new limit
simply cannot add more.
Use `PUT api/2.0/people/resetquota` to return accounts to the portal default.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_members_quota_request_dto** | [**UpdateMembersQuotaRequestDto**](UpdateMembersQuotaRequestDto.md)|  | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    update_members_quota_request_dto = docspace_api_sdk.UpdateMembersQuotaRequestDto() # UpdateMembersQuotaRequestDto |  (optional)

    try:
        # Change a user quota limit
        api_response = api_instance.update_user_quota(update_members_quota_request_dto=update_members_quota_request_dto)
        print("The response of QuotaApi->update_user_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->update_user_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The accounts whose limit was changed |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The value is not a whole number of bytes, or it exceeds the storage the portal allows |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

