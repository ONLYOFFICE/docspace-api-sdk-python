# docspace.PeoplePasswordApi

All URIs are relative to *http://http:*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_user_password**](PeoplePasswordApi.md#change_user_password) | **PUT** /api/2.0/people/{userid}/password | Change a user password
[**send_user_password**](PeoplePasswordApi.md#send_user_password) | **POST** /api/2.0/people/password | Remind a user password


# **change_user_password**
> EmployeeFullWrapper change_user_password(userid, member_base_request_dto=member_base_request_dto)

Change a user password

Sets a new password to the user with the ID specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.employee_full_wrapper import EmployeeFullWrapper
from docspace.models.member_base_request_dto import MemberBaseRequestDto
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.PeoplePasswordApi(api_client)
    userid = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The user ID.
    member_base_request_dto = docspace.MemberBaseRequestDto() # MemberBaseRequestDto | The request parameters for the user generic information. (optional)

    try:
        # Change a user password
        api_response = api_instance.change_user_password(userid, member_base_request_dto=member_base_request_dto)
        print("The response of PeoplePasswordApi->change_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePasswordApi->change_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 
 **member_base_request_dto** | [**MemberBaseRequestDto**](MemberBaseRequestDto.md)| The request parameters for the user generic information. | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed user information |  -  |
**400** | Incorrect email |  -  |
**401** | Unauthorized |  -  |
**403** | The invitation link is invalid or its validity has expired |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_user_password**
> StringWrapper send_user_password(email_member_request_dto=email_member_request_dto)

Remind a user password

Reminds a password to the user using the email address specified in the request.

### Example


```python
import docspace
from docspace.models.email_member_request_dto import EmailMemberRequestDto
from docspace.models.string_wrapper import StringWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.PeoplePasswordApi(api_client)
    email_member_request_dto = docspace.EmailMemberRequestDto() # EmailMemberRequestDto |  (optional)

    try:
        # Remind a user password
        api_response = api_instance.send_user_password(email_member_request_dto=email_member_request_dto)
        print("The response of PeoplePasswordApi->send_user_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePasswordApi->send_user_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_member_request_dto** | [**EmailMemberRequestDto**](EmailMemberRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Email with the password |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

