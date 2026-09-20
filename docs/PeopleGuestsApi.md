# docspace_api_sdk.GuestsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**approve_guest_share_link**](#approve_guest_share_link) | **POST** /api/2.0/people/guests/share/approve | Approve a guest sharing link
[**delete_guests**](#delete_guests) | **DELETE** /api/2.0/people/guests | Remove guest relations


# **approve_guest_share_link**
> EmployeeFullWrapper approve_guest_share_link(email_member_request_dto=email_member_request_dto)

Accepts a guest that another member shared, which links that guest to the calling account and makes it
visible in the caller's list of guests.
Everything the operation needs comes from the confirmation token of the link produced by
`GET api/2.0/people/guests/{userid}/share`: the request body is not read at all, so there is nothing to fill
in, and an expired or already used token is answered with 401.
The caller has to be a room admin or a DocSpace admin; a member or a guest gets 403.
The account the token names has to exist and still be a guest, otherwise the operation answers 404 or 400.
The call is idempotent: a guest that is already linked to the caller is simply returned again.
The answer is the full profile of the guest.

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
**200** | The full profile of the guest now linked to the caller |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The account named by the token is not a guest |  -  |
**403** | The caller is a member or a guest |  -  |
**404** | The account named by the token no longer exists |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_guests**
> delete_guests(update_members_request_dto=update_members_request_dto)

Removes the listed guests from the caller's own list of guests and withdraws the access the caller had
granted them.
It does not delete the accounts: each guest keeps its profile and any access other members gave it, and only
the link to the caller and the caller's own shares disappear.
The caller has to be a room admin or a DocSpace admin, and every listed account has to exist, be an active
guest and be one of the caller's own guests - a single entry that is not rejects the whole call with 403 and
changes nothing.
The call returns no body; read `GET api/2.0/people/filter` with `area` set to `Guests` to see what is left.
To delete a guest account for good, disable it and then use `DELETE api/2.0/people/{userid}`.

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
        # Remove guest relations
        api_instance.delete_guests(update_members_request_dto=update_members_request_dto)
    except Exception as e:
        print("Exception when calling GuestsApi->delete_guests: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The guests are no longer linked to the caller. No content is returned |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The userIds field is missing |  -  |
**403** | The caller is not an admin, or an entry is not an active guest of the caller |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

