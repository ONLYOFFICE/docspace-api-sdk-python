# docspace_api_sdk.AuthenticationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_me**](#authenticate_me) | **POST** /api/2.0/authentication | Authenticate a user
[**authenticate_me_from_body_with_code**](#authenticate_me_from_body_with_code) | **POST** /api/2.0/authentication/{code} | Authenticate a user by code
[**check_confirm**](#check_confirm) | **POST** /api/2.0/authentication/confirm | Open confirmation email URL
[**get_is_authentificated**](#get_is_authentificated) | **GET** /api/2.0/authentication | Check authentication
[**logout**](#logout) | **POST** /api/2.0/authentication/logout | Log out
[**save_mobile_phone**](#save_mobile_phone) | **POST** /api/2.0/authentication/setphone | Set a mobile phone
[**send_sms_code**](#send_sms_code) | **POST** /api/2.0/authentication/sendsms | Send SMS code


# **authenticate_me**
> AuthenticationTokenWrapper authenticate_me(auth_requests_dto=auth_requests_dto)

Authenticates the current user by SMS, authenticator app, or without two-factor authentication.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auth_requests_dto import AuthRequestsDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    auth_requests_dto = docspace_api_sdk.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Authenticate a user
        api_response = api_instance.authenticate_me(auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->authenticate_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_me: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication data |  -  |
**400** | userName, password or passworHash is empty |  -  |
**401** | User authentication failed |  -  |
**404** | The user could not be found |  -  |
**429** | Too many login attempts. Please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **authenticate_me_from_body_with_code**
> AuthenticationTokenWrapper authenticate_me_from_body_with_code(code, auth_requests_dto=auth_requests_dto)

Authenticates the current user by SMS or two-factor authentication code.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auth_requests_dto import AuthRequestsDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    code = 'code_example' # str | 
    auth_requests_dto = docspace_api_sdk.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Authenticate a user by code
        api_response = api_instance.authenticate_me_from_body_with_code(code, auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->authenticate_me_from_body_with_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_me_from_body_with_code: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication data |  -  |
**400** | userName, password or passworHash is empty |  -  |
**401** | User authentication failed |  -  |
**403** | Auth code is not available |  -  |
**429** | Too many login attempts. Please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **check_confirm**
> ConfirmWrapper check_confirm(email_validation_key_model=email_validation_key_model)

Opens a confirmation email URL to validate a certain action (employee invitation, portal removal, phone activation, etc.).

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_validation_key_model** | [**EmailValidationKeyModel**](EmailValidationKeyModel.md)|  | [optional] 

### Return type

[**ConfirmWrapper**](ConfirmWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.confirm_wrapper import ConfirmWrapper
from docspace_api_sdk.models.email_validation_key_model import EmailValidationKeyModel
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    email_validation_key_model = docspace_api_sdk.EmailValidationKeyModel() # EmailValidationKeyModel |  (optional)

    try:
        # Open confirmation email URL
        api_response = api_instance.check_confirm(email_validation_key_model=email_validation_key_model)
        print("The response of AuthenticationApi->check_confirm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->check_confirm: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Validation result: Ok, Invalid, or Expired |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_authentificated**
> BooleanWrapper get_is_authentificated()

Checks if the current user is authenticated or not.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)

    try:
        # Check authentication
        api_response = api_instance.get_is_authentificated()
        print("The response of AuthenticationApi->get_is_authentificated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_is_authentificated: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the current user is authenticated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> StringWrapper logout()

Logs out of the current user account.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)

    try:
        # Log out
        api_response = api_instance.logout()
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_mobile_phone**
> AuthenticationTokenWrapper save_mobile_phone(mobile_requests_dto=mobile_requests_dto)

Sets a mobile phone for the current user.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_requests_dto** | [**MobileRequestsDto**](MobileRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
from docspace_api_sdk.models.mobile_requests_dto import MobileRequestsDto
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
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    mobile_requests_dto = docspace_api_sdk.MobileRequestsDto() # MobileRequestsDto |  (optional)

    try:
        # Set a mobile phone
        api_response = api_instance.save_mobile_phone(mobile_requests_dto=mobile_requests_dto)
        print("The response of AuthenticationApi->save_mobile_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->save_mobile_phone: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication data |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_sms_code**
> AuthenticationTokenWrapper send_sms_code(auth_requests_dto=auth_requests_dto)

Sends SMS with an authentication code.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.auth_requests_dto import AuthRequestsDto
from docspace_api_sdk.models.authentication_token_wrapper import AuthenticationTokenWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AuthenticationApi(api_client)
    auth_requests_dto = docspace_api_sdk.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Send SMS code
        api_response = api_instance.send_sms_code(auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->send_sms_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->send_sms_code: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Authentication data |  -  |
**400** | userName, password or passworHash is empty |  -  |
**429** | Too many login attempts. Please try again later |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

