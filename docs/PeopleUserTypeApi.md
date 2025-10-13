# docspace_api_sdk.UserTypeApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_type_update_progress**](#get_user_type_update_progress) | **GET** /api/2.0/people/type/progress/{userid} | Get the progress of updating user type
[**star_user_typet_update**](#star_user_typet_update) | **POST** /api/2.0/people/type | Update user type
[**terminate_user_type_update**](#terminate_user_type_update) | **PUT** /api/2.0/people/type/terminate | Terminate update user type
[**update_user_type**](#update_user_type) | **PUT** /api/2.0/people/type/{type} | Change a user type


# **get_user_type_update_progress**
> TaskProgressResponseWrapper get_user_type_update_progress(userid)

Returns the progress of updating the user type.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 

### Return type

[**TaskProgressResponseWrapper**](TaskProgressResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.task_progress_response_wrapper import TaskProgressResponseWrapper
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
    api_instance = docspace_api_sdk.UserTypeApi(api_client)
    userid = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The user ID.

    try:
        # Get the progress of updating user type
        api_response = api_instance.get_user_type_update_progress(userid)
        print("The response of UserTypeApi->get_user_type_update_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->get_user_type_update_progress: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update type progress |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **star_user_typet_update**
> TaskProgressResponseWrapper star_user_typet_update(start_update_user_type_dto=start_update_user_type_dto)

Starts updating the type of the user or guest when reassigning rooms and shared files.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_update_user_type_dto** | [**StartUpdateUserTypeDto**](StartUpdateUserTypeDto.md)|  | [optional] 

### Return type

[**TaskProgressResponseWrapper**](TaskProgressResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.start_update_user_type_dto import StartUpdateUserTypeDto
from docspace_api_sdk.models.task_progress_response_wrapper import TaskProgressResponseWrapper
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
    api_instance = docspace_api_sdk.UserTypeApi(api_client)
    start_update_user_type_dto = docspace_api_sdk.StartUpdateUserTypeDto() # StartUpdateUserTypeDto |  (optional)

    try:
        # Update user type
        api_response = api_instance.star_user_typet_update(start_update_user_type_dto=start_update_user_type_dto)
        print("The response of UserTypeApi->star_user_typet_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->star_user_typet_update: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update type progress |  -  |
**400** | Can not update user type |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_user_type_update**
> TaskProgressResponseWrapper terminate_user_type_update(terminate_request_dto=terminate_request_dto)

Terminates the process of updating the type of the user or guest.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminate_request_dto** | [**TerminateRequestDto**](TerminateRequestDto.md)|  | [optional] 

### Return type

[**TaskProgressResponseWrapper**](TaskProgressResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.task_progress_response_wrapper import TaskProgressResponseWrapper
from docspace_api_sdk.models.terminate_request_dto import TerminateRequestDto
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
    api_instance = docspace_api_sdk.UserTypeApi(api_client)
    terminate_request_dto = docspace_api_sdk.TerminateRequestDto() # TerminateRequestDto |  (optional)

    try:
        # Terminate update user type
        api_response = api_instance.terminate_user_type_update(terminate_request_dto=terminate_request_dto)
        print("The response of UserTypeApi->terminate_user_type_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->terminate_user_type_update: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Update type progress |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_type**
> EmployeeFullArrayWrapper update_user_type(type, update_members_request_dto)

Changes a type of the users with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**EmployeeType**](.md)| The new user type. | 
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)| The request parameters for updating the user information. | 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.UserTypeApi(api_client)
    type = docspace_api_sdk.EmployeeType() # EmployeeType | The new user type.
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto | The request parameters for updating the user information.

    try:
        # Change a user type
        api_response = api_instance.update_user_type(type, update_members_request_dto)
        print("The response of UserTypeApi->update_user_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->update_user_type: %s\n" % e)
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

