# docspace.PeopleThirdPartyAccountsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_auth_providers**](PeopleThirdPartyAccountsApi.md#get_auth_providers) | **GET** /api/2.0/people/thirdparty/providers | Get third-party accounts
[**link_account**](PeopleThirdPartyAccountsApi.md#link_account) | **PUT** /api/2.0/people/thirdparty/linkaccount | Link a third-pary account
[**signup_account**](PeopleThirdPartyAccountsApi.md#signup_account) | **POST** /api/2.0/people/thirdparty/signup | Create a third-pary account
[**unlink_account**](PeopleThirdPartyAccountsApi.md#unlink_account) | **DELETE** /api/2.0/people/thirdparty/unlinkaccount | Unlink a third-pary account


# **get_auth_providers**
> AccountInfoArrayWrapper get_auth_providers(invite_view=invite_view, settings_view=settings_view, client_callback=client_callback, from_only=from_only)

Get third-party accounts

Returns a list of the available third-party accounts.

### Example


```python
import docspace
from docspace.models.account_info_array_wrapper import AccountInfoArrayWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.PeopleThirdPartyAccountsApi(api_client)
    invite_view = true # bool | Specifies whether to return providers that are available for invitation links, i.e. the user can login or register through these providers. (optional)
    settings_view = true # bool | Specifies whether to display the provider settings in a pop-up window (true) or redirect them to the desktop application (false). (optional)
    client_callback = 'some text' # str | The method that is called after authentication. (optional)
    from_only = 'some text' # str | The provider name if a response is required only from this provider. (optional)

    try:
        # Get third-party accounts
        api_response = api_instance.get_auth_providers(invite_view=invite_view, settings_view=settings_view, client_callback=client_callback, from_only=from_only)
        print("The response of PeopleThirdPartyAccountsApi->get_auth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleThirdPartyAccountsApi->get_auth_providers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invite_view** | **bool**| Specifies whether to return providers that are available for invitation links, i.e. the user can login or register through these providers. | [optional] 
 **settings_view** | **bool**| Specifies whether to display the provider settings in a pop-up window (true) or redirect them to the desktop application (false). | [optional] 
 **client_callback** | **str**| The method that is called after authentication. | [optional] 
 **from_only** | **str**| The provider name if a response is required only from this provider. | [optional] 

### Return type

[**AccountInfoArrayWrapper**](AccountInfoArrayWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of third-party accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_account**
> link_account(link_account_request_dto=link_account_request_dto)

Link a third-pary account

Links a third-party account specified in the request to the user profile.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.link_account_request_dto import LinkAccountRequestDto
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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
    api_instance = docspace.PeopleThirdPartyAccountsApi(api_client)
    link_account_request_dto = docspace.LinkAccountRequestDto() # LinkAccountRequestDto |  (optional)

    try:
        # Link a third-pary account
        api_instance.link_account(link_account_request_dto=link_account_request_dto)
    except Exception as e:
        print("Exception when calling PeopleThirdPartyAccountsApi->link_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_account_request_dto** | [**LinkAccountRequestDto**](LinkAccountRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**405** | Error not allowed option |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **signup_account**
> signup_account(signup_account_request_dto=signup_account_request_dto)

Create a third-pary account

Creates a third-party account with the parameters specified in the request.

### Example


```python
import docspace
from docspace.models.signup_account_request_dto import SignupAccountRequestDto
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.PeopleThirdPartyAccountsApi(api_client)
    signup_account_request_dto = docspace.SignupAccountRequestDto() # SignupAccountRequestDto |  (optional)

    try:
        # Create a third-pary account
        api_instance.signup_account(signup_account_request_dto=signup_account_request_dto)
    except Exception as e:
        print("Exception when calling PeopleThirdPartyAccountsApi->signup_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_account_request_dto** | [**SignupAccountRequestDto**](SignupAccountRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**400** | Incorrect email |  -  |
**403** | The invitation link is invalid or its validity has expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_account**
> unlink_account(provider=provider)

Unlink a third-pary account

Unlinks a third-party account specified in the request from the user profile.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
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
    api_instance = docspace.PeopleThirdPartyAccountsApi(api_client)
    provider = 'some text' # str | The provider name. (optional)

    try:
        # Unlink a third-pary account
        api_instance.unlink_account(provider=provider)
    except Exception as e:
        print("Exception when calling PeopleThirdPartyAccountsApi->unlink_account: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The provider name. | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

