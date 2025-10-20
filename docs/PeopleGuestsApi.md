# docspace_api_sdk.GuestsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_guest_share_link**](#approve_guest_share_link) | **POST** /api/2.0/people/guests/share/approve | Approve a guest sharing link
[**delete_guests**](#delete_guests) | **DELETE** /api/2.0/people/guests | Delete guests


# **approve_guest_share_link**
> EmployeeFullWrapper approve_guest_share_link(email_member_request_dto=email_member_request_dto)

Approves a guest sharing link and returns the detailed information about a guest.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_member_request_dto** | [**EmailMemberRequestDto**](EmailMemberRequestDto.md)|  | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.email_member_request_dto import EmailMemberRequestDto
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
    api_instance = docspace_api_sdk.GuestsApi(api_client)
    email_member_request_dto = docspace_api_sdk.EmailMemberRequestDto() # EmailMemberRequestDto |  (optional)

    try:
        # Approve a guest sharing link
        api_response = api_instance.approve_guest_share_link(email_member_request_dto=email_member_request_dto)
        print("The response of GuestsApi->approve_guest_share_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GuestsApi->approve_guest_share_link: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed profile information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guests**
> delete_guests(update_members_request_dto=update_members_request_dto)

Deletes guests from the list and excludes them from rooms to which they were invited.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.GuestsApi(api_client)
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto |  (optional)

    try:
        # Delete guests
        api_instance.delete_guests(update_members_request_dto=update_members_request_dto)
    except Exception as e:
        print("Exception when calling GuestsApi->delete_guests: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request parameters for deleting guests |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

