# docspace_api_sdk.UserDataApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_delete_personal_folder_progress**](#get_delete_personal_folder_progress) | **GET** /api/2.0/people/delete/personal/progress | Get the personal folder deletion progress
[**get_reassign_progress**](#get_reassign_progress) | **GET** /api/2.0/people/reassign/progress/{userid} | Get the reassignment progress
[**get_remove_progress**](#get_remove_progress) | **GET** /api/2.0/people/remove/progress/{userid} | Get the deletion progress
[**necessary_reassign**](#necessary_reassign) | **GET** /api/2.0/people/reassign/necessary | Check data for reassignment need
[**send_instructions_to_delete**](#send_instructions_to_delete) | **PUT** /api/2.0/people/self/delete | Send the deletion instructions
[**start_delete_personal_folder**](#start_delete_personal_folder) | **POST** /api/2.0/people/delete/personal/start | Delete the personal folder
[**start_reassign**](#start_reassign) | **POST** /api/2.0/people/reassign/start | Start the data reassignment
[**start_remove**](#start_remove) | **POST** /api/2.0/people/remove/start | Start the data deletion
[**terminate_reassign**](#terminate_reassign) | **PUT** /api/2.0/people/reassign/terminate | Terminate the data reassignment
[**terminate_remove**](#terminate_remove) | **PUT** /api/2.0/people/remove/terminate | Terminate the data deletion


# **get_delete_personal_folder_progress**
> TaskProgressResponseWrapper get_delete_personal_folder_progress()

Returns the current state of the personal folder deletion queued for the authenticated account.
The job must have been queued by `POST api/2.0/people/delete/personal/start` first: when nothing is queued for
the caller the operation answers 200 with an empty body.
It takes no parameters and reports on the caller only, so an administrator cannot watch the folder deletion of
another user through it.
The call is read-only and is the polling operation of this flow - repeat it until `isCompleted` is true, and
read `error` for the message left by a failed job.
A queued personal folder deletion cannot be cancelled, so the only outcome to wait for is its completion.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)

    try:
        # Get the personal folder deletion progress
        api_response = api_instance.get_delete_personal_folder_progress()
        print("The response of UserDataApi->get_delete_personal_folder_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->get_delete_personal_folder_progress: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued personal folder deletion, or an empty body when nothing is queued for the caller |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reassign_progress**
> TaskProgressResponseWrapper get_reassign_progress(userid)

Returns the current state of the data reassignment queued for the user with the ID specified in the request.
A reassignment must have been queued by `POST api/2.0/people/reassign/start` first: when nothing is queued for
that user the operation answers 200 with an empty body.
The caller needs the permission to edit users, and only the portal owner may track a reassignment whose source
user is a DocSpace administrator.
The call is read-only and is the polling operation of the reassignment flow - repeat it until `isCompleted` is
true, reading `percentage` for the 0 to 100 progress and `error` for the message left by a failed job.
Use `PUT api/2.0/people/reassign/terminate` to cancel a job that is still running.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The ID of the user the operation applies to, taken from the route. For a progress operation it has to be the  same ID that was passed when the job was started. | 

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the user the operation applies to, taken from the route. For a progress operation it has to be the  same ID that was passed when the job was started.

    try:
        # Get the reassignment progress
        api_response = api_instance.get_reassign_progress(userid)
        print("The response of UserDataApi->get_reassign_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->get_reassign_progress: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued reassignment, or an empty body when nothing is queued for the user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_remove_progress**
> TaskProgressResponseWrapper get_remove_progress(userid)

Returns the current state of the data deletion queued for the user with the ID specified in the request.
A deletion must have been queued by `POST api/2.0/people/remove/start` first: when nothing is queued for that
user the operation answers 200 with an empty body.
The caller needs the permission to edit users.
The call is read-only and is the polling operation of the deletion flow - repeat it until `isCompleted` is
true, reading `percentage` for the 0 to 100 progress and `error` for the message left by a failed job.
Use `PUT api/2.0/people/remove/terminate` to cancel a job that is still running.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The ID of the user the operation applies to, taken from the route. For a progress operation it has to be the  same ID that was passed when the job was started. | 

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the user the operation applies to, taken from the route. For a progress operation it has to be the  same ID that was passed when the job was started.

    try:
        # Get the deletion progress
        api_response = api_instance.get_remove_progress(userid)
        print("The response of UserDataApi->get_remove_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->get_remove_progress: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued deletion, or an empty body when nothing is queued for the user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **necessary_reassign**
> BooleanWrapper necessary_reassign(user_id=user_id, type=type)

Reports whether the rooms and the shared files of a user have to be reassigned before that user can be removed
or changed to the type passed in `type`.
Call it before `DELETE api/2.0/people/{userid}` or before a type change to find out whether
`POST api/2.0/people/reassign/start` has to run first.
The caller needs the permission to add and remove users of the requested type, and must be the portal owner
when the checked user is a DocSpace administrator.
The call is read-only and answers true when the user owns at least one room, or - when `type` is `Guest` -
when the user still has shared files.
A false answer means the user can be removed or converted without a reassignment.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **UUID**| The ID of the user whose rooms and shared files are checked. | [optional] 
 **type** | [**EmployeeType**](.md)| The type the user is about to be changed to, which decides what counts as data that has to be reassigned:  `RoomAdmin`, `DocSpaceAdmin` and `User` are checked for owned rooms only, while `Guest` is also checked for  files that are still shared. The default is `All`, which checks owned rooms only. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.employee_type import EmployeeType
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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    user_id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the user whose rooms and shared files are checked. (optional)
    type = docspace_api_sdk.EmployeeType() # EmployeeType | The type the user is about to be changed to, which decides what counts as data that has to be reassigned:  `RoomAdmin`, `DocSpaceAdmin` and `User` are checked for owned rooms only, while `Guest` is also checked for  files that are still shared. The default is `All`, which checks owned rooms only. (optional)

    try:
        # Check data for reassignment need
        api_response = api_instance.necessary_reassign(user_id=user_id, type=type)
        print("The response of UserDataApi->necessary_reassign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->necessary_reassign: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the data of the user has to be reassigned before the removal or the type change |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_instructions_to_delete**
> StringWrapper send_instructions_to_delete()

Emails the caller a confirmation link that lets them delete their own profile, and is the first step of the
self-service profile removal.
It acts on the authenticated account only and takes no parameters, so it cannot be used to remove somebody
else - an administrator removes another user through `DELETE api/2.0/people/{userid}`.
The caller has to be a regular portal account: the portal owner and an account imported from LDAP are
rejected, because neither can delete itself.
The call sends mail and does not change the profile; the deletion happens later, when the caller follows the
emailed link and the client calls `DELETE api/2.0/people/@self` with the confirmation token from it.
The answer is a ready-to-display message naming the address the link was sent to, and the address is wrapped
in bold HTML markup, so strip the markup before showing it outside a web page.
Repeated calls are throttled, and each one sends a new link.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)

    try:
        # Send the deletion instructions
        api_response = api_instance.send_instructions_to_delete()
        print("The response of UserDataApi->send_instructions_to_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->send_instructions_to_delete: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message stating which address the confirmation link was sent to |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 15-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is the portal owner or an LDAP account and cannot delete their own profile |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (5 req / 15 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_delete_personal_folder**
> TaskProgressResponseWrapper start_delete_personal_folder()

Queues an asynchronous job that empties the personal folder of the authenticated account.
The operation takes no parameters and always acts on the caller, so it cannot be used to empty the folder of
another user.
Only an account whose type is `Guest` may call it; every other type is rejected, because only a guest has a
personal folder that can be emptied this way.
The job does not finish within this call: poll `GET api/2.0/people/delete/personal/progress` until
`isCompleted` is true.
The job deletes the files permanently and cannot be undone or cancelled - there is no terminate operation for
this flow, unlike the user data deletion.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)

    try:
        # Delete the personal folder
        api_response = api_instance.start_delete_personal_folder()
        print("The response of UserDataApi->start_delete_personal_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->start_delete_personal_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued personal folder deletion |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a guest, so there is no personal folder to empty |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_reassign**
> TaskProgressResponseWrapper start_reassign(start_reassign_request_dto=start_reassign_request_dto)

Queues an asynchronous job that transfers the rooms and the shared files owned by one portal user to another.
The source user must already have the `Terminated` status - disable the account through
`PUT api/2.0/people/status/{status}` before calling this - and the destination user must be an active room
admin or DocSpace admin, so a guest, a system account or a disabled account is rejected.
The caller needs the permission to edit users, cannot reassign their own data, and must be the portal owner to
reassign the data of another DocSpace administrator or of a People module administrator.
The transfer does not finish within this call: poll `GET api/2.0/people/reassign/progress/{userid}` with the
source user ID until `isCompleted` is true, and cancel it through `PUT api/2.0/people/reassign/terminate`.
Pass `deleteProfile` as true to delete the source profile once the transfer succeeds, otherwise the emptied
profile is kept.
Use `GET api/2.0/people/reassign/necessary` first to find out whether the user owns anything that has to be
reassigned at all.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_reassign_request_dto** | [**StartReassignRequestDto**](StartReassignRequestDto.md)|  | [optional] 

### Return type

[**TaskProgressResponseWrapper**](TaskProgressResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.start_reassign_request_dto import StartReassignRequestDto
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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    start_reassign_request_dto = docspace_api_sdk.StartReassignRequestDto() # StartReassignRequestDto |  (optional)

    try:
        # Start the data reassignment
        api_response = api_instance.start_reassign(start_reassign_request_dto=start_reassign_request_dto)
        print("The response of UserDataApi->start_reassign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->start_reassign: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued reassignment |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The destination user is not an active room or DocSpace admin, or the source user is a system account, the portal owner, the caller, or is not disabled |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_remove**
> TaskProgressResponseWrapper start_remove(terminate_request_dto=terminate_request_dto)

Queues an asynchronous job that erases the data of the user with the ID specified in the request.
The account must already have the `Terminated` status - disable it through
`PUT api/2.0/people/status/{status}` first - and it cannot be the portal owner or the caller.
The caller needs the permission to edit users, has to be a DocSpace admin to erase the data of a room admin,
and has to be the portal owner to erase the data of another DocSpace admin.
The erasure does not finish within this call: poll `GET api/2.0/people/remove/progress/{userid}` with the same
user ID until `isCompleted` is true, and cancel it through `PUT api/2.0/people/remove/terminate`.
This operation destroys the data and cannot be undone; to keep the rooms and the shared files of the account
instead, transfer them first through `POST api/2.0/people/reassign/start`.
An unknown ID and a rejected precondition both answer 400 and name the ID they rejected.

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    terminate_request_dto = docspace_api_sdk.TerminateRequestDto() # TerminateRequestDto |  (optional)

    try:
        # Start the data deletion
        api_response = api_instance.start_remove(terminate_request_dto=terminate_request_dto)
        print("The response of UserDataApi->start_remove:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->start_remove: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued deletion |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | No user has the specified ID, or the account is the portal owner, the caller, or is not disabled |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_reassign**
> TaskProgressResponseWrapper terminate_reassign(terminate_request_dto=terminate_request_dto)

Cancels the data reassignment queued for the user with the ID specified in the request.
The caller needs the permission to edit users, and only the portal owner may cancel a reassignment whose
source user is a DocSpace administrator.
The operation is idempotent: when nothing is queued for that user it answers 200 with an empty body, and
repeating it on an already cancelled job changes nothing.
Cancelling removes the job from the queue and does not undo the transfers it has already made, and a cancelled
job cannot be resumed - start a new one through `POST api/2.0/people/reassign/start`.
The returned progress reports `status` as `Canceled` and `isCompleted` as true.

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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    terminate_request_dto = docspace_api_sdk.TerminateRequestDto() # TerminateRequestDto |  (optional)

    try:
        # Terminate the data reassignment
        api_response = api_instance.terminate_reassign(terminate_request_dto=terminate_request_dto)
        print("The response of UserDataApi->terminate_reassign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserDataApi->terminate_reassign: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the cancelled reassignment, or an empty body when nothing was queued for the user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_remove**
> terminate_remove(terminate_request_dto=terminate_request_dto)

Cancels the data deletion queued for the user with the ID specified in the request.
The caller needs the permission to edit users.
The operation is idempotent and returns no body: it drops the job from the queue, and doing so when nothing is
queued, or when the job has already finished, changes nothing and still answers 200.
Cancelling does not restore the data the job has already erased, and a cancelled job cannot be resumed - start
a new one through `POST api/2.0/people/remove/start`.
To find out whether the job is still running, read
`GET api/2.0/people/remove/progress/{userid}` before and after this call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **terminate_request_dto** | [**TerminateRequestDto**](TerminateRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.UserDataApi(api_client)
    terminate_request_dto = docspace_api_sdk.TerminateRequestDto() # TerminateRequestDto |  (optional)

    try:
        # Terminate the data deletion
        api_instance.terminate_remove(terminate_request_dto=terminate_request_dto)
    except Exception as e:
        print("Exception when calling UserDataApi->terminate_remove: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queued deletion is cancelled, or there was nothing to cancel. No content is returned |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

