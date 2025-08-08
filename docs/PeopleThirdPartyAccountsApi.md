# docspace_api_sdk.ThirdPartyAccountsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_third_party_auth_providers**](#get_third_party_auth_providers) | **GET** /api/2.0/people/thirdparty/providers | Get third-party accounts
[**link_third_party_account**](#link_third_party_account) | **PUT** /api/2.0/people/thirdparty/linkaccount | Link a third-pary account
[**signup_third_party_account**](#signup_third_party_account) | **POST** /api/2.0/people/thirdparty/signup | Create a third-pary account
[**unlink_third_party_account**](#unlink_third_party_account) | **DELETE** /api/2.0/people/thirdparty/unlinkaccount | Unlink a third-pary account


# **get_third_party_auth_providers**
> AccountInfoArrayWrapper get_third_party_auth_providers(invite_view=invite_view, settings_view=settings_view, client_callback=client_callback, from_only=from_only)

Returns a list of the available third-party accounts.

For more information, see [api.onlyoffice.com]().

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

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.account_info_array_wrapper import AccountInfoArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    invite_view = true # bool | Specifies whether to return providers that are available for invitation links, i.e. the user can login or register through these providers. (optional)
    settings_view = true # bool | Specifies whether to display the provider settings in a pop-up window (true) or redirect them to the desktop application (false). (optional)
    client_callback = 'some text' # str | The method that is called after authentication. (optional)
    from_only = 'some text' # str | The provider name if a response is required only from this provider. (optional)

    try:
        # Get third-party accounts
        api_response = api_instance.get_third_party_auth_providers(invite_view=invite_view, settings_view=settings_view, client_callback=client_callback, from_only=from_only)
        print("The response of ThirdPartyAccountsApi->get_third_party_auth_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->get_third_party_auth_providers: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of third-party accounts |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **link_third_party_account**
> link_third_party_account(link_account_request_dto=link_account_request_dto)

Links a third-party account specified in the request to the user profile.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **link_account_request_dto** | [**LinkAccountRequestDto**](LinkAccountRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.link_account_request_dto import LinkAccountRequestDto
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
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    link_account_request_dto = docspace_api_sdk.LinkAccountRequestDto() # LinkAccountRequestDto |  (optional)

    try:
        # Link a third-pary account
        api_instance.link_third_party_account(link_account_request_dto=link_account_request_dto)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->link_third_party_account: %s\n" % e)
```



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

# **signup_third_party_account**
> signup_third_party_account(signup_account_request_dto=signup_account_request_dto)

Creates a third-party account with the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **signup_account_request_dto** | [**SignupAccountRequestDto**](SignupAccountRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.signup_account_request_dto import SignupAccountRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    signup_account_request_dto = docspace_api_sdk.SignupAccountRequestDto() # SignupAccountRequestDto |  (optional)

    try:
        # Create a third-pary account
        api_instance.signup_third_party_account(signup_account_request_dto=signup_account_request_dto)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->signup_third_party_account: %s\n" % e)
```



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

# **unlink_third_party_account**
> unlink_third_party_account(provider=provider)

Unlinks a third-party account specified in the request from the user profile.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | **str**| The provider name. | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
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
    api_instance = docspace_api_sdk.ThirdPartyAccountsApi(api_client)
    provider = 'some text' # str | The provider name. (optional)

    try:
        # Unlink a third-pary account
        api_instance.unlink_third_party_account(provider=provider)
    except Exception as e:
        print("Exception when calling ThirdPartyAccountsApi->unlink_third_party_account: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

