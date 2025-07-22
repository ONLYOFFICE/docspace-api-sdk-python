# docspace-api-sdk.SettingsRebrandingApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_additional_white_label_settings**](#delete_additional_white_label_settings) | **DELETE** /api/2.0/settings/rebranding/additional | Delete the additional white label settings
[**delete_company_white_label_settings**](#delete_company_white_label_settings) | **DELETE** /api/2.0/settings/rebranding/company | Delete the company white label settings
[**get_additional_white_label_settings**](#get_additional_white_label_settings) | **GET** /api/2.0/settings/rebranding/additional | Get the additional white label settings
[**get_company_white_label_settings**](#get_company_white_label_settings) | **GET** /api/2.0/settings/rebranding/company | Get the company white label settings
[**get_enable_whitelabel**](#get_enable_whitelabel) | **GET** /api/2.0/settings/enablewhitelabel | Check the white label availability
[**get_is_default_white_label_logo_text**](#get_is_default_white_label_logo_text) | **GET** /api/2.0/settings/whitelabel/logotext/isdefault | Check the default white label logo text
[**get_is_default_white_label_logos**](#get_is_default_white_label_logos) | **GET** /api/2.0/settings/whitelabel/logos/isdefault | Check the default white label logos
[**get_licensor_data**](#get_licensor_data) | **GET** /api/2.0/settings/companywhitelabel | Get the licensor data
[**get_white_label_logo_text**](#get_white_label_logo_text) | **GET** /api/2.0/settings/whitelabel/logotext | Get the white label logo text
[**get_white_label_logos**](#get_white_label_logos) | **GET** /api/2.0/settings/whitelabel/logos | Get the white label logos
[**restore_white_label_logo_text**](#restore_white_label_logo_text) | **PUT** /api/2.0/settings/whitelabel/logotext/restore | Restore the white label logo text
[**restore_white_label_logos**](#restore_white_label_logos) | **PUT** /api/2.0/settings/whitelabel/logos/restore | Restore the white label logos
[**save_additional_white_label_settings**](#save_additional_white_label_settings) | **POST** /api/2.0/settings/rebranding/additional | Save the additional white label settings
[**save_company_white_label_settings**](#save_company_white_label_settings) | **POST** /api/2.0/settings/rebranding/company | Save the company white label settings
[**save_white_label_logo_text**](#save_white_label_logo_text) | **POST** /api/2.0/settings/whitelabel/logotext/save | Save the white label logo text settings
[**save_white_label_settings**](#save_white_label_settings) | **POST** /api/2.0/settings/whitelabel/logos/save | Save the white label logos
[**save_white_label_settings_from_files**](#save_white_label_settings_from_files) | **POST** /api/2.0/settings/whitelabel/logos/savefromfiles | Save the white label logos from files


# **delete_additional_white_label_settings**
> AdditionalWhiteLabelSettingsWrapper delete_additional_white_label_settings()

Deletes the additional white label settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AdditionalWhiteLabelSettingsWrapper**](AdditionalWhiteLabelSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)

    try:
        # Delete the additional white label settings
        api_response = api_instance.delete_additional_white_label_settings()
        print("The response of SettingsRebrandingApi->delete_additional_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->delete_additional_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default additional white label settings |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_company_white_label_settings**
> CompanyWhiteLabelSettingsWrapper delete_company_white_label_settings()

Deletes the company white label settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyWhiteLabelSettingsWrapper**](CompanyWhiteLabelSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.company_white_label_settings_wrapper import CompanyWhiteLabelSettingsWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)

    try:
        # Delete the company white label settings
        api_response = api_instance.delete_company_white_label_settings()
        print("The response of SettingsRebrandingApi->delete_company_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->delete_company_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Default company white label settings |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_additional_white_label_settings**
> AdditionalWhiteLabelSettingsWrapper get_additional_white_label_settings()

Returns the additional white label settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AdditionalWhiteLabelSettingsWrapper**](AdditionalWhiteLabelSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)

    try:
        # Get the additional white label settings
        api_response = api_instance.get_additional_white_label_settings()
        print("The response of SettingsRebrandingApi->get_additional_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_additional_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Additional white label settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_white_label_settings**
> CompanyWhiteLabelSettingsWrapper get_company_white_label_settings()

Returns the company white label settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyWhiteLabelSettingsWrapper**](CompanyWhiteLabelSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.company_white_label_settings_wrapper import CompanyWhiteLabelSettingsWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)

    try:
        # Get the company white label settings
        api_response = api_instance.get_company_white_label_settings()
        print("The response of SettingsRebrandingApi->get_company_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_company_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Company white label settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enable_whitelabel**
> BooleanWrapper get_enable_whitelabel()

Checks if the white label is enabled or not.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)

    try:
        # Check the white label availability
        api_response = api_instance.get_enable_whitelabel()
        print("The response of SettingsRebrandingApi->get_enable_whitelabel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_enable_whitelabel: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the white label is enabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_default_white_label_logo_text**
> IsDefaultWhiteLabelLogosWrapper get_is_default_white_label_logo_text(is_dark=is_dark, is_default=is_default)

Specifies if the white label logo text are default or not.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**IsDefaultWhiteLabelLogosWrapper**](IsDefaultWhiteLabelLogosWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.is_default_white_label_logos_wrapper import IsDefaultWhiteLabelLogosWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Check the default white label logo text
        api_response = api_instance.get_is_default_white_label_logo_text(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->get_is_default_white_label_logo_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_is_default_white_label_logo_text: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request properties of white label logos |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_default_white_label_logos**
> IsDefaultWhiteLabelLogosArrayWrapper get_is_default_white_label_logos(is_dark=is_dark, is_default=is_default)

Specifies if the white label logos are default or not.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**IsDefaultWhiteLabelLogosArrayWrapper**](IsDefaultWhiteLabelLogosArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.is_default_white_label_logos_array_wrapper import IsDefaultWhiteLabelLogosArrayWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Check the default white label logos
        api_response = api_instance.get_is_default_white_label_logos(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->get_is_default_white_label_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_is_default_white_label_logos: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request properties of white label logos |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_licensor_data**
> CompanyWhiteLabelSettingsArrayWrapper get_licensor_data()

Returns the licensor data.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CompanyWhiteLabelSettingsArrayWrapper**](CompanyWhiteLabelSettingsArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.company_white_label_settings_array_wrapper import CompanyWhiteLabelSettingsArrayWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)

    try:
        # Get the licensor data
        api_response = api_instance.get_licensor_data()
        print("The response of SettingsRebrandingApi->get_licensor_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_licensor_data: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of company white label settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_white_label_logo_text**
> StringWrapper get_white_label_logo_text(is_dark=is_dark, is_default=is_default)

Returns the white label logo text.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.string_wrapper import StringWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Get the white label logo text
        api_response = api_instance.get_white_label_logo_text(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->get_white_label_logo_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_white_label_logo_text: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Logo text |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_white_label_logos**
> WhiteLabelItemArrayWrapper get_white_label_logos(is_dark=is_dark, is_default=is_default)

Returns the white label logos.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**WhiteLabelItemArrayWrapper**](WhiteLabelItemArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.white_label_item_array_wrapper import WhiteLabelItemArrayWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Get the white label logos
        api_response = api_instance.get_white_label_logos(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->get_white_label_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->get_white_label_logos: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | White label logos |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_white_label_logo_text**
> BooleanWrapper restore_white_label_logo_text(is_dark=is_dark, is_default=is_default)

Restores the white label logo text.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Restore the white label logo text
        api_response = api_instance.restore_white_label_logo_text(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->restore_white_label_logo_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->restore_white_label_logo_text: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restore_white_label_logos**
> BooleanWrapper restore_white_label_logos(is_dark=is_dark, is_default=is_default)

Restores the white label logos.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Restore the white label logos
        api_response = api_instance.restore_white_label_logos(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->restore_white_label_logos:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->restore_white_label_logos: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_additional_white_label_settings**
> BooleanWrapper save_additional_white_label_settings(additional_white_label_settings_wrapper=additional_white_label_settings_wrapper)

Saves the additional white label settings specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **additional_white_label_settings_wrapper** | [**AdditionalWhiteLabelSettingsWrapper**](AdditionalWhiteLabelSettingsWrapper.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.additional_white_label_settings_wrapper import AdditionalWhiteLabelSettingsWrapper
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    additional_white_label_settings_wrapper = docspace-api-sdk.AdditionalWhiteLabelSettingsWrapper() # AdditionalWhiteLabelSettingsWrapper |  (optional)

    try:
        # Save the additional white label settings
        api_response = api_instance.save_additional_white_label_settings(additional_white_label_settings_wrapper=additional_white_label_settings_wrapper)
        print("The response of SettingsRebrandingApi->save_additional_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->save_additional_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**400** | Settings is empty |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_company_white_label_settings**
> BooleanWrapper save_company_white_label_settings(company_white_label_settings_wrapper=company_white_label_settings_wrapper)

Saves the company white label settings specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **company_white_label_settings_wrapper** | [**CompanyWhiteLabelSettingsWrapper**](CompanyWhiteLabelSettingsWrapper.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.company_white_label_settings_wrapper import CompanyWhiteLabelSettingsWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    company_white_label_settings_wrapper = docspace-api-sdk.CompanyWhiteLabelSettingsWrapper() # CompanyWhiteLabelSettingsWrapper |  (optional)

    try:
        # Save the company white label settings
        api_response = api_instance.save_company_white_label_settings(company_white_label_settings_wrapper=company_white_label_settings_wrapper)
        print("The response of SettingsRebrandingApi->save_company_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->save_company_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**400** | Argument is empty or invalid |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_white_label_logo_text**
> BooleanWrapper save_white_label_logo_text(is_dark=is_dark, is_default=is_default, white_label_requests_dto=white_label_requests_dto)

Saves the white label logo text specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 
 **white_label_requests_dto** | [**WhiteLabelRequestsDto**](WhiteLabelRequestsDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.white_label_requests_dto import WhiteLabelRequestsDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)
    white_label_requests_dto = docspace-api-sdk.WhiteLabelRequestsDto() # WhiteLabelRequestsDto |  (optional)

    try:
        # Save the white label logo text settings
        api_response = api_instance.save_white_label_logo_text(is_dark=is_dark, is_default=is_default, white_label_requests_dto=white_label_requests_dto)
        print("The response of SettingsRebrandingApi->save_white_label_logo_text:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->save_white_label_logo_text: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is sucessful |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_white_label_settings**
> BooleanWrapper save_white_label_settings(is_dark=is_dark, is_default=is_default, white_label_requests_dto=white_label_requests_dto)

Saves the white label logos specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 
 **white_label_requests_dto** | [**WhiteLabelRequestsDto**](WhiteLabelRequestsDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.models.white_label_requests_dto import WhiteLabelRequestsDto
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)
    white_label_requests_dto = docspace-api-sdk.WhiteLabelRequestsDto() # WhiteLabelRequestsDto |  (optional)

    try:
        # Save the white label logos
        api_response = api_instance.save_white_label_settings(is_dark=is_dark, is_default=is_default, white_label_requests_dto=white_label_requests_dto)
        print("The response of SettingsRebrandingApi->save_white_label_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->save_white_label_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is sucessful |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_white_label_settings_from_files**
> BooleanWrapper save_white_label_settings_from_files(is_dark=is_dark, is_default=is_default)

Saves the white label logos from files.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **is_dark** | **bool**| Specifies if the white label logo is for the dark theme or not. | [optional] 
 **is_default** | **bool**| Specifies if the logo is for a default tenant or not. | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-sdk
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper
from docspace-api-sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-sdk.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-sdk.Configuration(
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
configuration = docspace-api-sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-sdk.SettingsRebrandingApi(api_client)
    is_dark = true # bool | Specifies if the white label logo is for the dark theme or not. (optional)
    is_default = true # bool | Specifies if the logo is for a default tenant or not. (optional)

    try:
        # Save the white label logos from files
        api_response = api_instance.save_white_label_settings_from_files(is_dark=is_dark, is_default=is_default)
        print("The response of SettingsRebrandingApi->save_white_label_settings_from_files:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsRebrandingApi->save_white_label_settings_from_files: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is sucessful |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**409** | No input files |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

