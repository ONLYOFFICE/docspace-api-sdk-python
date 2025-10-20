# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reset_users_quota**](#reset_users_quota) | **PUT** /api/2.0/people/resetquota | Reset a user quota limit
[**update_user_quota**](#update_user_quota) | **PUT** /api/2.0/people/userquota | Change a user quota limit


# **reset_users_quota**
> EmployeeFullArrayWrapper reset_users_quota(update_members_quota_request_dto=update_members_quota_request_dto)

Resets a quota limit of users with the IDs specified in the request.

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
**200** | User detailed information |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | The invitation link is invalid or its validity has expired |  -  |
**409** | Conflict - system user quota cannot be reset |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_quota**
> EmployeeFullArrayWrapper update_user_quota(update_members_quota_request_dto=update_members_quota_request_dto)

Changes a quota limit for the users with the IDs specified in the request.

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
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |
**402** | Failed to set quota per user. The entered value is greater than the total DocSpace storage |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

