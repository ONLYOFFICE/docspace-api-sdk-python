# docspace-api-python.PeopleQuotaApi

All URIs are relative to *http://localhost:8092*

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
import docspace-api-python
from docspace-api-python.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace-api-python.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.PeopleQuotaApi(api_client)
    update_members_quota_request_dto = docspace-api-python.UpdateMembersQuotaRequestDto() # UpdateMembersQuotaRequestDto |  (optional)

    try:
        # Reset a user quota limit
        api_response = api_instance.reset_users_quota(update_members_quota_request_dto=update_members_quota_request_dto)
        print("The response of PeopleQuotaApi->reset_users_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleQuotaApi->reset_users_quota: %s\n" % e)
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
import docspace-api-python
from docspace-api-python.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace-api-python.models.update_members_quota_request_dto import UpdateMembersQuotaRequestDto
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.PeopleQuotaApi(api_client)
    update_members_quota_request_dto = docspace-api-python.UpdateMembersQuotaRequestDto() # UpdateMembersQuotaRequestDto |  (optional)

    try:
        # Change a user quota limit
        api_response = api_instance.update_user_quota(update_members_quota_request_dto=update_members_quota_request_dto)
        print("The response of PeopleQuotaApi->update_user_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleQuotaApi->update_user_quota: %s\n" % e)
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

