# docspace_api_sdk.EmailApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_email**](#change_user_email) | **PUT** /api/2.0/people/{userid}/email | Change a user email
[**send_email_change_instructions**](#send_email_change_instructions) | **POST** /api/2.0/people/email | Send instructions to change email


# **change_user_email**
> EmployeeFullWrapper change_user_email(userid, change_email_request)

Sets a new email to the user with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **UUID**| The user ID. | 
 **change_email_request** | [**ChangeEmailRequest**](ChangeEmailRequest.md)| The request parameters for updating a user email. | 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_email_request import ChangeEmailRequest
from docspace_api_sdk.models.employee_full_wrapper import EmployeeFullWrapper
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
    api_instance = docspace_api_sdk.EmailApi(api_client)
    userid = UUID('00000000-0000-0000-0000-000000000000') # UUID | The user ID.
    change_email_request = docspace_api_sdk.ChangeEmailRequest() # ChangeEmailRequest | The request parameters for updating a user email.

    try:
        # Change a user email
        api_response = api_instance.change_user_email(userid, change_email_request)
        print("The response of EmailApi->change_user_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->change_user_email: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed user information |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Incorrect userId or email |  -  |
**403** | The link is invalid or no permissions to perform this action |  -  |
**404** | The user could not be found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_email_change_instructions**
> StringWrapper send_email_change_instructions(update_member_request_dto=update_member_request_dto)

Sends a message to the user email with the instructions to change the email address connected to the portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_member_request_dto** | [**UpdateMemberRequestDto**](UpdateMemberRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.models.update_member_request_dto import UpdateMemberRequestDto
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
    api_instance = docspace_api_sdk.EmailApi(api_client)
    update_member_request_dto = docspace_api_sdk.UpdateMemberRequestDto() # UpdateMemberRequestDto |  (optional)

    try:
        # Send instructions to change email
        api_response = api_instance.send_email_change_instructions(update_member_request_dto=update_member_request_dto)
        print("The response of EmailApi->send_email_change_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailApi->send_email_change_instructions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message text |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | Incorrect userId or email |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

