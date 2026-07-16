# docspace_api_sdk.ProfilesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_member**](#add_member) | **POST** /api/2.0/people | Add a user
[**check_user_exists_by_email**](#check_user_exists_by_email) | **GET** /api/2.0/people/exists | Check if a user exists by email
[**delete_member**](#delete_member) | **DELETE** /api/2.0/people/{userid} | Delete a user
[**delete_profile**](#delete_profile) | **DELETE** /api/2.0/people/@self | Delete my profile
[**get_all_profiles**](#get_all_profiles) | **GET** /api/2.0/people | Get profiles
[**get_claims**](#get_claims) | **GET** /api/2.0/people/tokendiagnostics | Get user claims
[**get_profile_by_email**](#get_profile_by_email) | **GET** /api/2.0/people/email | Get a profile by user email
[**get_profile_by_user_id**](#get_profile_by_user_id) | **GET** /api/2.0/people/{userid} | Get a profile by user ID
[**get_self_profile**](#get_self_profile) | **GET** /api/2.0/people/@self | Get my profile
[**invite_users**](#invite_users) | **POST** /api/2.0/people/invite | Invite users
[**remove_users**](#remove_users) | **PUT** /api/2.0/people/delete | Delete users
[**resend_user_invites**](#resend_user_invites) | **PUT** /api/2.0/people/invite | Resend activation emails
[**update_member**](#update_member) | **PUT** /api/2.0/people/{userid} | Update a user
[**update_member_culture**](#update_member_culture) | **PUT** /api/2.0/people/{userid}/culture | Update a user culture


# **add_member**
> EmployeeFullWrapper add_member(member_request_dto=member_request_dto)

Adds a new portal user with the first name, last name, email address, and several optional parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_request_dto** | [**MemberRequestDto**](MemberRequestDto.md)|  | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_wrapper import EmployeeFullWrapper
from docspace_api_sdk.models.member_request_dto import MemberRequestDto
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    member_request_dto = docspace_api_sdk.MemberRequestDto() # MemberRequestDto |  (optional)

    try:
        # Add a user
        api_response = api_instance.add_member(member_request_dto=member_request_dto)
        print("The response of ProfilesApi->add_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->add_member: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Newly added user with the detailed information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | The invitation link is invalid or its validity has expired |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_user_exists_by_email**
> UserExistsResponseWrapper check_user_exists_by_email(email=email, encemail=encemail, culture=culture)

Returns data indicating whether a user with the specified email exists on the portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The user email address. | [optional] 
 **encemail** | **str**| The user encrypted email address. | [optional] 
 **culture** | **str**| Culture | [optional] 

### Return type

[**UserExistsResponseWrapper**](UserExistsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.user_exists_response_wrapper import UserExistsResponseWrapper
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    email = 'john.doe@example.com' # str | The user email address. (optional)
    encemail = 'encrypted_email_string' # str | The user encrypted email address. (optional)
    culture = 'en-US' # str | Culture (optional)

    try:
        # Check if a user exists by email
        api_response = api_instance.check_user_exists_by_email(email=email, encemail=encemail, culture=culture)
        print("The response of ProfilesApi->check_user_exists_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->check_user_exists_by_email: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User existence result |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Incorrect email |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member**
> EmployeeFullWrapper delete_member(userid)

Deletes a user with the ID specified in the request from the portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    userid = '00000000-0000-0000-0000-000000000000' # str | The user ID.

    try:
        # Delete a user
        api_response = api_instance.delete_member(userid)
        print("The response of ProfilesApi->delete_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->delete_member: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted user detailed information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation or user is not suspended |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_profile**
> EmployeeFullWrapper delete_profile()

Deletes the current user profile.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)

    try:
        # Delete my profile
        api_response = api_instance.delete_profile()
        print("The response of ProfilesApi->delete_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->delete_profile: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed information about my profile |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_profiles**
> EmployeeFullArrayWrapper get_all_profiles(count=count, start_index=start_index, filter_by=filter_by, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)

Returns a list of profiles for all the portal users.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**| The maximum number of items to be retrieved in the response. | [optional] 
 **start_index** | **int**| The zero-based index of the first item to be retrieved in a filtered result set. | [optional] 
 **filter_by** | **str**| Specifies the filter criteria for user-related queries. | [optional] 
 **sort_by** | **str**| Specifies the property or field name by which the results should be sorted. | [optional] 
 **sort_order** | [**SortOrder**](.md)| The order in which the results are sorted. | [optional] 
 **filter_separator** | **str**| The character or string used to separate multiple filter values in a filtering query. | [optional] 
 **filter_value** | **str**| The text value used as an additional filter criterion for profiles retrieval. | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    count = 25 # int | The maximum number of items to be retrieved in the response. (optional)
    start_index = 0 # int | The zero-based index of the first item to be retrieved in a filtered result set. (optional)
    filter_by = 'displayName' # str | Specifies the filter criteria for user-related queries. (optional)
    sort_by = 'displayName' # str | Specifies the property or field name by which the results should be sorted. (optional)
    sort_order = docspace_api_sdk.SortOrder() # SortOrder | The order in which the results are sorted. (optional)
    filter_separator = ',' # str | The character or string used to separate multiple filter values in a filtering query. (optional)
    filter_value = 'John' # str | The text value used as an additional filter criterion for profiles retrieval. (optional)

    try:
        # Get profiles
        api_response = api_instance.get_all_profiles(count=count, start_index=start_index, filter_by=filter_by, sort_by=sort_by, sort_order=sort_order, filter_separator=filter_separator, filter_value=filter_value)
        print("The response of ProfilesApi->get_all_profiles:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_all_profiles: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_claims**
> ObjectWrapper get_claims()

Returns the user claims.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectWrapper**](ObjectWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_wrapper import ObjectWrapper
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)

    try:
        # Get user claims
        api_response = api_instance.get_claims()
        print("The response of ProfilesApi->get_claims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_claims: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Claims |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_email**
> EmployeeFullWrapper get_profile_by_email(email=email, encemail=encemail, culture=culture)

Returns the detailed information about a profile of the user with the email specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| The user email address. | [optional] 
 **encemail** | **str**| The user encrypted email address. | [optional] 
 **culture** | **str**| Culture | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    email = 'john.doe@example.com' # str | The user email address. (optional)
    encemail = 'encrypted_email_string' # str | The user encrypted email address. (optional)
    culture = 'en-US' # str | Culture (optional)

    try:
        # Get a profile by user email
        api_response = api_instance.get_profile_by_email(email=email, encemail=encemail, culture=culture)
        print("The response of ProfilesApi->get_profile_by_email:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_by_email: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed profile information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Incorrect email |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_by_user_id**
> EmployeeFullWrapper get_profile_by_user_id(userid)

Returns the detailed information about a profile of the user with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    userid = '00000000-0000-0000-0000-000000000000' # str | The user ID.

    try:
        # Get a profile by user ID
        api_response = api_instance.get_profile_by_user_id(userid)
        print("The response of ProfilesApi->get_profile_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_profile_by_user_id: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed profile information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Incorrect UserId |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_self_profile**
> EmployeeFullWrapper get_self_profile()

Returns the detailed information about the current user profile.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)

    try:
        # Get my profile
        api_response = api_instance.get_self_profile()
        print("The response of ProfilesApi->get_self_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->get_self_profile: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed information about my profile |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_users**
> EmployeeArrayWrapper invite_users(invite_users_request_dto=invite_users_request_dto)

Invites users specified in the request to the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_users_request_dto** | [**InviteUsersRequestDto**](InviteUsersRequestDto.md)|  | [optional] 

### Return type

[**EmployeeArrayWrapper**](EmployeeArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_array_wrapper import EmployeeArrayWrapper
from docspace_api_sdk.models.invite_users_request_dto import InviteUsersRequestDto
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    invite_users_request_dto = docspace_api_sdk.InviteUsersRequestDto() # InviteUsersRequestDto |  (optional)

    try:
        # Invite users
        api_response = api_instance.invite_users(invite_users_request_dto=invite_users_request_dto)
        print("The response of ProfilesApi->invite_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->invite_users: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users |  -  |
**400** | Incorrect email or User disabled |  -  |
**402** | The number of admins exceeds the limit |  -  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_users**
> EmployeeFullArrayWrapper remove_users(update_members_request_dto=update_members_request_dto)

Deletes a list of the users with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)|  | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto |  (optional)

    try:
        # Delete users
        api_response = api_instance.remove_users(update_members_request_dto=update_members_request_dto)
        print("The response of ProfilesApi->remove_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->remove_users: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Incorrect UserIds |  -  |
**403** | No permissions to perform this action or users are not suspended |  -  |
**409** | Data reassign process is not complete |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **resend_user_invites**
> EmployeeFullArrayWrapper resend_user_invites(update_members_request_dto=update_members_request_dto)

Resends emails to the users who have not activated their emails.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)|  | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    update_members_request_dto = docspace_api_sdk.UpdateMembersRequestDto() # UpdateMembersRequestDto |  (optional)

    try:
        # Resend activation emails
        api_response = api_instance.resend_user_invites(update_members_request_dto=update_members_request_dto)
        print("The response of ProfilesApi->resend_user_invites:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->resend_user_invites: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  * X-RateLimit-Limit - Rate limit: 5 requests per 15 minutes per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member**
> EmployeeFullWrapper update_member(userid, update_member_request_dto)

Updates the data for the selected portal user with the first name, last name, email address, and/or optional parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 
 **update_member_request_dto** | [**UpdateMemberRequestDto**](UpdateMemberRequestDto.md)| The request parameters for updating the user information. | 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_full_wrapper import EmployeeFullWrapper
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    userid = '00000000-0000-0000-0000-000000000000' # str | The user ID.
    update_member_request_dto = docspace_api_sdk.UpdateMemberRequestDto() # UpdateMemberRequestDto | The request parameters for updating the user information.

    try:
        # Update a user
        api_response = api_instance.update_member(userid, update_member_request_dto)
        print("The response of ProfilesApi->update_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_member: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user with the detailed information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | Incorrect user name |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_culture**
> EmployeeFullWrapper update_member_culture(userid, culture=culture)

Updates the user culture with the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 
 **culture** | [**Culture**](Culture.md)| The culture name parameters. | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.culture import Culture
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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    userid = '00000000-0000-0000-0000-000000000000' # str | The user ID.
    culture = docspace_api_sdk.Culture() # Culture | The culture name parameters. (optional)

    try:
        # Update a user culture
        api_response = api_instance.update_member_culture(userid, culture=culture)
        print("The response of ProfilesApi->update_member_culture:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->update_member_culture: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Detailed user information |  * X-RateLimit-Limit - Sliding window rate limit: 1500 requests per minute per user/IP. <br>  * X-RateLimit-Remaining - Number of requests remaining in the current sliding window (1500 req/min). Concurrent limits also apply: 50 parallel GET requests, 15 parallel POST/PUT requests. <br>  * X-RateLimit-Reset - Unix timestamp (seconds) when the current sliding window rate limit resets. <br>  |
**400** | The specified culture is not in the list of available ones |  -  |
**403** | You don't have enough permission to perform the operation |  -  |
**404** | User not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying. Up to 60s for the sliding window (1500 req/min), up to 86400s for the daily POST/PUT limit (10000/day). <br>  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

