# docspace.AuthenticationApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_me**](AuthenticationApi.md#authenticate_me) | **POST** /api/2.0/authentication | Authenticate a user
[**authenticate_me_from_body_with_code**](AuthenticationApi.md#authenticate_me_from_body_with_code) | **POST** /api/2.0/authentication/{code} | Authenticate a user by code
[**check_confirm**](AuthenticationApi.md#check_confirm) | **POST** /api/2.0/authentication/confirm | Open confirmation email URL
[**get_is_authentificated**](AuthenticationApi.md#get_is_authentificated) | **GET** /api/2.0/authentication | Check authentication
[**logout**](AuthenticationApi.md#logout) | **POST** /api/2.0/authentication/logout | Log out
[**save_mobile_phone**](AuthenticationApi.md#save_mobile_phone) | **POST** /api/2.0/authentication/setphone | Set a mobile phone
[**send_sms_code**](AuthenticationApi.md#send_sms_code) | **POST** /api/2.0/authentication/sendsms | Send SMS code


# **authenticate_me**
> AuthenticationTokenWrapper authenticate_me(auth_requests_dto=auth_requests_dto)

Authenticate a user

Authenticates the current user by SMS, authenticator app, or without two-factor authentication.

### Example


```python
import docspace
from docspace.models.auth_requests_dto import AuthRequestsDto
from docspace.models.authentication_token_wrapper import AuthenticationTokenWrapper
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
    api_instance = docspace.AuthenticationApi(api_client)
    auth_requests_dto = docspace.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Authenticate a user
        api_response = api_instance.authenticate_me(auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->authenticate_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_me: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

No authorization required

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

Authenticate a user by code

Authenticates the current user by SMS or two-factor authentication code.

### Example


```python
import docspace
from docspace.models.auth_requests_dto import AuthRequestsDto
from docspace.models.authentication_token_wrapper import AuthenticationTokenWrapper
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
    api_instance = docspace.AuthenticationApi(api_client)
    code = 'code_example' # str | 
    auth_requests_dto = docspace.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Authenticate a user by code
        api_response = api_instance.authenticate_me_from_body_with_code(code, auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->authenticate_me_from_body_with_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->authenticate_me_from_body_with_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**|  | 
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

No authorization required

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

Open confirmation email URL

Opens a confirmation email URL to validate a certain action (employee invitation, portal removal, phone activation, etc.).

### Example


```python
import docspace
from docspace.models.confirm_wrapper import ConfirmWrapper
from docspace.models.email_validation_key_model import EmailValidationKeyModel
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
    api_instance = docspace.AuthenticationApi(api_client)
    email_validation_key_model = docspace.EmailValidationKeyModel() # EmailValidationKeyModel |  (optional)

    try:
        # Open confirmation email URL
        api_response = api_instance.check_confirm(email_validation_key_model=email_validation_key_model)
        print("The response of AuthenticationApi->check_confirm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->check_confirm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_validation_key_model** | [**EmailValidationKeyModel**](EmailValidationKeyModel.md)|  | [optional] 

### Return type

[**ConfirmWrapper**](ConfirmWrapper.md)

### Authorization

No authorization required

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

Check authentication

Checks if the current user is authenticated or not.

### Example


```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace.AuthenticationApi(api_client)

    try:
        # Check authentication
        api_response = api_instance.get_is_authentificated()
        print("The response of AuthenticationApi->get_is_authentificated:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->get_is_authentificated: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

No authorization required

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

Log out

Logs out of the current user account.

### Example


```python
import docspace
from docspace.models.string_wrapper import StringWrapper
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
    api_instance = docspace.AuthenticationApi(api_client)

    try:
        # Log out
        api_response = api_instance.logout()
        print("The response of AuthenticationApi->logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->logout: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

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

Set a mobile phone

Sets a mobile phone for the current user.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.authentication_token_wrapper import AuthenticationTokenWrapper
from docspace.models.mobile_requests_dto import MobileRequestsDto
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

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.AuthenticationApi(api_client)
    mobile_requests_dto = docspace.MobileRequestsDto() # MobileRequestsDto |  (optional)

    try:
        # Set a mobile phone
        api_response = api_instance.save_mobile_phone(mobile_requests_dto=mobile_requests_dto)
        print("The response of AuthenticationApi->save_mobile_phone:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->save_mobile_phone: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mobile_requests_dto** | [**MobileRequestsDto**](MobileRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Send SMS code

Sends SMS with an authentication code.

### Example


```python
import docspace
from docspace.models.auth_requests_dto import AuthRequestsDto
from docspace.models.authentication_token_wrapper import AuthenticationTokenWrapper
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
    api_instance = docspace.AuthenticationApi(api_client)
    auth_requests_dto = docspace.AuthRequestsDto() # AuthRequestsDto |  (optional)

    try:
        # Send SMS code
        api_response = api_instance.send_sms_code(auth_requests_dto=auth_requests_dto)
        print("The response of AuthenticationApi->send_sms_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthenticationApi->send_sms_code: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **auth_requests_dto** | [**AuthRequestsDto**](AuthRequestsDto.md)|  | [optional] 

### Return type

[**AuthenticationTokenWrapper**](AuthenticationTokenWrapper.md)

### Authorization

No authorization required

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

