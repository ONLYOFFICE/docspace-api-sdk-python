# docspace_api_sdk.UserTypeApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_type_update_progress**](#get_user_type_update_progress) | **GET** /api/2.0/people/type/progress/{userid} | Get the user type change progress
[**start_user_type_update**](#start_user_type_update) | **POST** /api/2.0/people/type | Start updating user type
[**terminate_user_type_update**](#terminate_user_type_update) | **PUT** /api/2.0/people/type/terminate | Terminate updating user type
[**update_user_type**](#update_user_type) | **PUT** /api/2.0/people/type/{type} | Change a user type


# **get_user_type_update_progress**
> TaskProgressResponseWrapper get_user_type_update_progress(userid)

Returns the current state of the user type change queued for the user with the ID specified in the request.
A conversion must have been queued by `POST api/2.0/people/type` first: when nothing is queued for that user
the operation answers 200 with an empty body.
The caller needs the permission to add and remove users.
The call is read-only and is the polling operation of this flow - repeat it until `isCompleted` is true,
reading `percentage` for the 0 to 100 progress and `error` for the message left by a failed job.
Use `PUT api/2.0/people/type/terminate` to cancel a conversion that is still running.

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
    api_instance = docspace_api_sdk.UserTypeApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The ID of the user the operation applies to, taken from the route. For a progress operation it has to be the  same ID that was passed when the job was started.

    try:
        # Get the user type change progress
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
**200** | The state of the queued user type change, or an empty body when nothing is queued for the user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_user_type_update**
> TaskProgressResponseWrapper start_user_type_update(start_update_user_type_dto=start_update_user_type_dto)

Queues an asynchronous job that converts one account to `Guest` or `User` and, in the same job, hands the
rooms and the shared files of that account over to another administrator.
Only `Guest` and `User` are accepted here, because they are the types that cannot own rooms; for any other
type use `PUT api/2.0/people/type/{type}`, which converts immediately and transfers nothing.
The caller needs the permission to add and remove users of the requested type, has to be the portal owner to
convert a DocSpace administrator, and converting to `Guest` also requires the portal to allow inviting guests.
The account being converted has to be active and cannot be the caller, and the recipient - `reassignUserId`,
or the caller when it is omitted - has to be an active room admin or DocSpace admin other than that account.
The conversion does not finish within this call: poll `GET api/2.0/people/type/progress/{userid}` with the
converted user ID until `isCompleted` is true, and cancel it through `PUT api/2.0/people/type/terminate`.
A failure inside the running job is reported in the `error` field of the progress, not as a status code here.

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
        # Start updating user type
        api_response = api_instance.start_user_type_update(start_update_user_type_dto=start_update_user_type_dto)
        print("The response of UserTypeApi->start_user_type_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserTypeApi->start_user_type_update: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the queued user type change |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The requested type is neither Guest nor User, the account is a system account, disabled or the caller, the recipient is the same account or is not an active admin, or a non-owner tried to convert a DocSpace admin |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_user_type_update**
> TaskProgressResponseWrapper terminate_user_type_update(terminate_request_dto=terminate_request_dto)

Cancels the user type change queued for the user with the ID specified in the request.
The caller needs the permission to add and remove users.
The operation is idempotent: when nothing is queued for that user it answers 200 with an empty body, and
repeating it on an already cancelled job changes nothing.
Cancelling removes the job from the queue and does not undo the type change or the transfers it has already
made, and a cancelled job cannot be resumed - start a new one through `POST api/2.0/people/type`.
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
    api_instance = docspace_api_sdk.UserTypeApi(api_client)
    terminate_request_dto = docspace_api_sdk.TerminateRequestDto() # TerminateRequestDto |  (optional)

    try:
        # Terminate updating user type
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
**200** | The state of the cancelled user type change, or an empty body when nothing was queued for the user |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_type**
> EmployeeFullArrayWrapper update_user_type(type, update_members_request_dto)

Changes the type of the existing portal users listed in `userIds` to the type given in the route, in one call.
The caller needs the permission to add and remove users of the requested type, cannot change their own type or
the type of the portal owner, and cannot use this operation at all while being a guest; changing somebody to
`Guest` additionally requires the portal to allow inviting guests.
Every listed account has to be visible to the caller and must not be disabled.
The change is applied immediately: each converted user gets a notification email and raises a `UserUpdated`
webhook, and the accounts are processed one by one, so a rejection in the middle leaves the users before it
already converted - re-read them before retrying.
The answer streams the converted users with their detailed information, in the order they were processed.
Converting somebody to a paid type takes a paid seat, so the operation answers 402 when the tariff or the
paid-user quota does not allow one more.
This operation only moves the type and leaves the rooms and the shared files of the account where they are -
to hand them over to another admin in the same step, use `POST api/2.0/people/type` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**EmployeeType**](.md)| The type to convert the listed accounts to, taken from the route: `User`, `Guest`, `RoomAdmin` or  `DocSpaceAdmin`. `RoomAdmin` and `DocSpaceAdmin` take a paid seat. | 
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)| The accounts to convert. Only `userIds` is read by this operation; `resendAll` belongs to the invitation  operations and is ignored here. | 

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
    type = docspace_api_sdk.EmployeeType() # EmployeeType | The type to convert the listed accounts to, taken from the route: `User`, `Guest`, `RoomAdmin` or  `DocSpaceAdmin`. `RoomAdmin` and `DocSpaceAdmin` take a paid seat.
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto | The accounts to convert. Only `userIds` is read by this operation; `resendAll` belongs to the invitation  operations and is ignored here.

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
**200** | The converted users with their detailed information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The tariff or the paid-user quota does not allow one more paid user |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

