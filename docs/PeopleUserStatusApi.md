# docspace_api_sdk.UserStatusApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_by_status**](#get_by_status) | **GET** /api/2.0/people/status/{status} | Get profiles by status
[**update_user_activation_status**](#update_user_activation_status) | **PUT** /api/2.0/people/activationstatus/{activationstatus} | Set an activation status to the users
[**update_user_status**](#update_user_status) | **PUT** /api/2.0/people/status/{status} | Change a user status


# **get_by_status**
> EmployeeFullArrayWrapper get_by_status(status, filter_by=filter_by, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)

Returns a list of profiles filtered by the user status.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**EmployeeStatus**](.md)| The user status. | 
 **filter_by** | **str**| Specifies the criteria used to filter the profiles in the request. | [optional] 
 **count** | **int**| The maximum number of user profiles to retrieve. | [optional] 
 **start_index** | **int**| The starting index for retrieving data in a paginated request. | [optional] 
 **sort_by** | **str**| Specifies the property or field name by which the results should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_separator** | **str**| Represents the separator used to split multiple filter criteria in a query string. | [optional] 
 **filter_value** | **str**| A string value representing additional filter criteria used in query parameters. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.sort_order import SortOrder
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
    api_instance = docspace_api_sdk.UserStatusApi(api_client)
    status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | The user status.
    filter_by = 'some text' # str | Specifies the criteria used to filter the profiles in the request. (optional)
    count = 1234 # int | The maximum number of user profiles to retrieve. (optional)
    start_index = 1234 # int | The starting index for retrieving data in a paginated request. (optional)
    sort_by = 'some text' # str | Specifies the property or field name by which the results should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_separator = 'some text' # str | Represents the separator used to split multiple filter criteria in a query string. (optional)
    filter_value = 'some text' # str | A string value representing additional filter criteria used in query parameters. (optional)

    try:
        # Get profiles by status
        api_response = api_instance.get_by_status(status, filter_by=filter_by, count=count, start_index=start_index, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of UserStatusApi->get_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserStatusApi->get_by_status: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_activation_status**
> EmployeeFullArrayWrapper update_user_activation_status(activationstatus, update_members_request_dto=update_members_request_dto)

Sets the required activation status to the list of users with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **activationstatus** | [**EmployeeActivationStatus**](.md)| The new user activation status. | 
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)| The request parameters for updating the user information. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_activation_status import EmployeeActivationStatus
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.update_members_request_dto import UpdateMembersRequestDto
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
    api_instance = docspace_api_sdk.UserStatusApi(api_client)
    activationstatus = docspace_api_sdk.EmployeeActivationStatus() # EmployeeActivationStatus | The new user activation status.
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto | The request parameters for updating the user information. (optional)

    try:
        # Set an activation status to the users
        api_response = api_instance.update_user_activation_status(activationstatus, update_members_request_dto=update_members_request_dto)
        print("The response of UserStatusApi->update_user_activation_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserStatusApi->update_user_activation_status: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_status**
> EmployeeFullArrayWrapper update_user_status(status, update_members_request_dto=update_members_request_dto)

Changes a status of the users with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | [**EmployeeStatus**](.md)| The new user status. | 
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)| The request parameters for updating the user information. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_status import EmployeeStatus
from docspace_api_sdk.models.update_members_request_dto import UpdateMembersRequestDto
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
    api_instance = docspace_api_sdk.UserStatusApi(api_client)
    status = docspace_api_sdk.EmployeeStatus() # EmployeeStatus | The new user status.
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto | The request parameters for updating the user information. (optional)

    try:
        # Change a user status
        api_response = api_instance.update_user_status(status, update_members_request_dto=update_members_request_dto)
        print("The response of UserStatusApi->update_user_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserStatusApi->update_user_status: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

