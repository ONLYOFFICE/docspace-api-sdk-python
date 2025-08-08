# docspace_api_sdk.TFASettingsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tfa_app_codes**](#get_tfa_app_codes) | **GET** /api/2.0/settings/tfaappcodes | Get the TFA codes
[**get_tfa_confirm_url**](#get_tfa_confirm_url) | **GET** /api/2.0/settings/tfaapp/confirm | Get confirmation email
[**get_tfa_settings**](#get_tfa_settings) | **GET** /api/2.0/settings/tfaapp | Get the TFA settings
[**tfa_app_generate_setup_code**](#tfa_app_generate_setup_code) | **GET** /api/2.0/settings/tfaapp/setup | Generate setup code
[**tfa_validate_auth_code**](#tfa_validate_auth_code) | **POST** /api/2.0/settings/tfaapp/validate | Validate the TFA code
[**unlink_tfa_app**](#unlink_tfa_app) | **PUT** /api/2.0/settings/tfaappnewapp | Unlink the TFA application
[**update_tfa_app_codes**](#update_tfa_app_codes) | **PUT** /api/2.0/settings/tfaappnewcodes | Update the TFA codes
[**update_tfa_settings**](#update_tfa_settings) | **PUT** /api/2.0/settings/tfaapp | Update the TFA settings
[**update_tfa_settings_link**](#update_tfa_settings_link) | **PUT** /api/2.0/settings/tfaappwithlink | Get a confirmation email for updating TFA settings


# **get_tfa_app_codes**
> ObjectArrayWrapper get_tfa_app_codes()

Returns the two-factor authentication application codes.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_array_wrapper import ObjectArrayWrapper
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)

    try:
        # Get the TFA codes
        api_response = api_instance.get_tfa_app_codes()
        print("The response of TFASettingsApi->get_tfa_app_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->get_tfa_app_codes: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TFA application codes |  -  |
**401** | Unauthorized |  -  |
**405** | TFA application settings are not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tfa_confirm_url**
> StringWrapper get_tfa_confirm_url()

Returns the confirmation email URL for authorization via SMS or TFA application.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)

    try:
        # Get confirmation email
        api_response = api_instance.get_tfa_confirm_url()
        print("The response of TFASettingsApi->get_tfa_confirm_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->get_tfa_confirm_url: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation email URL |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tfa_settings**
> TfaSettingsArrayWrapper get_tfa_settings()

Returns the current two-factor authentication settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TfaSettingsArrayWrapper**](TfaSettingsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tfa_settings_array_wrapper import TfaSettingsArrayWrapper
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)

    try:
        # Get the TFA settings
        api_response = api_instance.get_tfa_settings()
        print("The response of TFASettingsApi->get_tfa_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->get_tfa_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TFA settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfa_app_generate_setup_code**
> SetupCodeWrapper tfa_app_generate_setup_code()

Generates the setup TFA code for the current user.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SetupCodeWrapper**](SetupCodeWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.setup_code_wrapper import SetupCodeWrapper
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)

    try:
        # Generate setup code
        api_response = api_instance.tfa_app_generate_setup_code()
        print("The response of TFASettingsApi->tfa_app_generate_setup_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->tfa_app_generate_setup_code: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Setup code |  -  |
**401** | Unauthorized |  -  |
**405** | TFA application settings are not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **tfa_validate_auth_code**
> BooleanWrapper tfa_validate_auth_code(tfa_validate_requests_dto=tfa_validate_requests_dto)

Validates the two-factor authentication code specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tfa_validate_requests_dto** | [**TfaValidateRequestsDto**](TfaValidateRequestsDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.tfa_validate_requests_dto import TfaValidateRequestsDto
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)
    tfa_validate_requests_dto = docspace_api_sdk.TfaValidateRequestsDto() # TfaValidateRequestsDto |  (optional)

    try:
        # Validate the TFA code
        api_response = api_instance.tfa_validate_auth_code(tfa_validate_requests_dto=tfa_validate_requests_dto)
        print("The response of TFASettingsApi->tfa_validate_auth_code:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->tfa_validate_auth_code: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the code is valid |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **unlink_tfa_app**
> StringWrapper unlink_tfa_app(tfa_requests_dto=tfa_requests_dto)

Unlinks the current two-factor authentication application from the user account specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tfa_requests_dto** | [**TfaRequestsDto**](TfaRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.models.tfa_requests_dto import TfaRequestsDto
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)
    tfa_requests_dto = docspace_api_sdk.TfaRequestsDto() # TfaRequestsDto |  (optional)

    try:
        # Unlink the TFA application
        api_response = api_instance.unlink_tfa_app(tfa_requests_dto=tfa_requests_dto)
        print("The response of TFASettingsApi->unlink_tfa_app:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->unlink_tfa_app: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Login URL |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**405** | TFA application settings are not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tfa_app_codes**
> ObjectArrayWrapper update_tfa_app_codes()

Requests the new backup codes for the two-factor authentication application.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ObjectArrayWrapper**](ObjectArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.object_array_wrapper import ObjectArrayWrapper
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)

    try:
        # Update the TFA codes
        api_response = api_instance.update_tfa_app_codes()
        print("The response of TFASettingsApi->update_tfa_app_codes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->update_tfa_app_codes: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | New backup codes |  -  |
**401** | Unauthorized |  -  |
**405** | TFA application settings are not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tfa_settings**
> BooleanWrapper update_tfa_settings(tfa_requests_dto=tfa_requests_dto)

Updates the two-factor authentication settings with the parameters specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tfa_requests_dto** | [**TfaRequestsDto**](TfaRequestsDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.tfa_requests_dto import TfaRequestsDto
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)
    tfa_requests_dto = docspace_api_sdk.TfaRequestsDto() # TfaRequestsDto |  (optional)

    try:
        # Update the TFA settings
        api_response = api_instance.update_tfa_settings(tfa_requests_dto=tfa_requests_dto)
        print("The response of TFASettingsApi->update_tfa_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->update_tfa_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**405** | SMS settings are not available/TFA application settings are not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tfa_settings_link**
> StringWrapper update_tfa_settings_link(tfa_requests_dto=tfa_requests_dto)

Returns the confirmation email URL for updating TFA settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tfa_requests_dto** | [**TfaRequestsDto**](TfaRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.models.tfa_requests_dto import TfaRequestsDto
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
    api_instance = docspace_api_sdk.TFASettingsApi(api_client)
    tfa_requests_dto = docspace_api_sdk.TfaRequestsDto() # TfaRequestsDto |  (optional)

    try:
        # Get a confirmation email for updating TFA settings
        api_response = api_instance.update_tfa_settings_link(tfa_requests_dto=tfa_requests_dto)
        print("The response of TFASettingsApi->update_tfa_settings_link:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TFASettingsApi->update_tfa_settings_link: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Confirmation email URL |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**405** | SMS settings are not available/TFA application settings are not available |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

