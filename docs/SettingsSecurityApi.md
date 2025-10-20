# docspace_api_sdk.SecurityApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_enabled_modules**](#get_enabled_modules) | **GET** /api/2.0/settings/security/modules | Get the enabled modules
[**get_is_product_administrator**](#get_is_product_administrator) | **GET** /api/2.0/settings/security/administrator | Check a product administrator
[**get_password_settings**](#get_password_settings) | **GET** /api/2.0/settings/security/password | Get the password settings
[**get_product_administrators**](#get_product_administrators) | **GET** /api/2.0/settings/security/administrator/{productid} | Get the product administrators
[**get_web_item_security_info**](#get_web_item_security_info) | **GET** /api/2.0/settings/security/{id} | Get the module availability
[**get_web_item_settings_security_info**](#get_web_item_settings_security_info) | **GET** /api/2.0/settings/security | Get the security settings
[**set_access_to_web_items**](#set_access_to_web_items) | **PUT** /api/2.0/settings/security/access | Set the security settings to modules
[**set_product_administrator**](#set_product_administrator) | **PUT** /api/2.0/settings/security/administrator | Set a product administrator
[**set_web_item_security**](#set_web_item_security) | **PUT** /api/2.0/settings/security | Set the module security settings
[**update_password_settings**](#update_password_settings) | **PUT** /api/2.0/settings/security/password | Set the password settings


# **get_enabled_modules**
> ObjectWrapper get_enabled_modules()

Returns a list of all the enabled modules.

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
    api_instance = docspace_api_sdk.SecurityApi(api_client)

    try:
        # Get the enabled modules
        api_response = api_instance.get_enabled_modules()
        print("The response of SecurityApi->get_enabled_modules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_enabled_modules: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of enabled modules |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_is_product_administrator**
> ProductAdministratorWrapper get_is_product_administrator(productid, userid)

Checks if the selected user is an administrator of a product with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productid** | **str**| The ID of the product extracted from the query parameters. | 
 **userid** | **str**| The user ID extracted from the query parameters. | 

### Return type

[**ProductAdministratorWrapper**](ProductAdministratorWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.product_administrator_wrapper import ProductAdministratorWrapper
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    productid = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The ID of the product extracted from the query parameters.
    userid = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The user ID extracted from the query parameters.

    try:
        # Check a product administrator
        api_response = api_instance.get_is_product_administrator(productid, userid)
        print("The response of SecurityApi->get_is_product_administrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_is_product_administrator: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object with the user security information: product ID, user ID, administrator or not |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_password_settings**
> PasswordSettingsWrapper get_password_settings()

Returns the portal password settings.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**PasswordSettingsWrapper**](PasswordSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.password_settings_wrapper import PasswordSettingsWrapper
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)

    try:
        # Get the password settings
        api_response = api_instance.get_password_settings()
        print("The response of SecurityApi->get_password_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_password_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product_administrators**
> EmployeeArrayWrapper get_product_administrators(productid)

Returns a list of all the administrators of a product with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **productid** | **str**| The ID of the product extracted from the route parameters. | 

### Return type

[**EmployeeArrayWrapper**](EmployeeArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.employee_array_wrapper import EmployeeArrayWrapper
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    productid = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The ID of the product extracted from the route parameters.

    try:
        # Get the product administrators
        api_response = api_instance.get_product_administrators(productid)
        print("The response of SecurityApi->get_product_administrators:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_product_administrators: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of product administrators with the following parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_item_security_info**
> BooleanWrapper get_web_item_security_info(id)

Returns the availability of the module with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The ID extracted from the route parameters. | 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | The ID extracted from the route parameters.

    try:
        # Get the module availability
        api_response = api_instance.get_web_item_security_info(id)
        print("The response of SecurityApi->get_web_item_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_web_item_security_info: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true - module is enabled, false - module is disabled |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_item_settings_security_info**
> SecurityArrayWrapper get_web_item_settings_security_info(ids=ids)

Returns the security settings for the modules specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ids** | [**List[str]**](str.md)| The list of module identifiers for which to retrieve the security settings. | [optional] 

### Return type

[**SecurityArrayWrapper**](SecurityArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.security_array_wrapper import SecurityArrayWrapper
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    ids = ['[\"some text\"]'] # List[str] | The list of module identifiers for which to retrieve the security settings. (optional)

    try:
        # Get the security settings
        api_response = api_instance.get_web_item_settings_security_info(ids=ids)
        print("The response of SecurityApi->get_web_item_settings_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->get_web_item_settings_security_info: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_access_to_web_items**
> SecurityArrayWrapper set_access_to_web_items(web_items_security_requests_dto=web_items_security_requests_dto)

Sets the security settings to the modules with the IDs specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_items_security_requests_dto** | [**WebItemsSecurityRequestsDto**](WebItemsSecurityRequestsDto.md)|  | [optional] 

### Return type

[**SecurityArrayWrapper**](SecurityArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.security_array_wrapper import SecurityArrayWrapper
from docspace_api_sdk.models.web_items_security_requests_dto import WebItemsSecurityRequestsDto
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    web_items_security_requests_dto = docspace_api_sdk.WebItemsSecurityRequestsDto() # WebItemsSecurityRequestsDto |  (optional)

    try:
        # Set the security settings to modules
        api_response = api_instance.set_access_to_web_items(web_items_security_requests_dto=web_items_security_requests_dto)
        print("The response of SecurityApi->set_access_to_web_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->set_access_to_web_items: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security settings |  -  |
**401** | Unauthorized |  -  |
**403** | Security settings are disabled for an open portal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_product_administrator**
> ProductAdministratorWrapper set_product_administrator(security_requests_dto=security_requests_dto)

Sets the selected user as an administrator of a product with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **security_requests_dto** | [**SecurityRequestsDto**](SecurityRequestsDto.md)|  | [optional] 

### Return type

[**ProductAdministratorWrapper**](ProductAdministratorWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.product_administrator_wrapper import ProductAdministratorWrapper
from docspace_api_sdk.models.security_requests_dto import SecurityRequestsDto
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    security_requests_dto = docspace_api_sdk.SecurityRequestsDto() # SecurityRequestsDto |  (optional)

    try:
        # Set a product administrator
        api_response = api_instance.set_product_administrator(security_requests_dto=security_requests_dto)
        print("The response of SecurityApi->set_product_administrator:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->set_product_administrator: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object with the user security information: product ID, user ID, administrator or not |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | Only portal owner can set user as administrator |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_web_item_security**
> SecurityArrayWrapper set_web_item_security(web_item_security_requests_dto=web_item_security_requests_dto)

Sets the security settings to the module with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_item_security_requests_dto** | [**WebItemSecurityRequestsDto**](WebItemSecurityRequestsDto.md)|  | [optional] 

### Return type

[**SecurityArrayWrapper**](SecurityArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.security_array_wrapper import SecurityArrayWrapper
from docspace_api_sdk.models.web_item_security_requests_dto import WebItemSecurityRequestsDto
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    web_item_security_requests_dto = docspace_api_sdk.WebItemSecurityRequestsDto() # WebItemSecurityRequestsDto |  (optional)

    try:
        # Set the module security settings
        api_response = api_instance.set_web_item_security(web_item_security_requests_dto=web_item_security_requests_dto)
        print("The response of SecurityApi->set_web_item_security:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->set_web_item_security: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Security settings |  -  |
**401** | Unauthorized |  -  |
**403** | Security settings are disabled for an open portal |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_password_settings**
> PasswordSettingsWrapper update_password_settings(password_settings_requests_dto=password_settings_requests_dto)

Sets the portal password settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **password_settings_requests_dto** | [**PasswordSettingsRequestsDto**](PasswordSettingsRequestsDto.md)|  | [optional] 

### Return type

[**PasswordSettingsWrapper**](PasswordSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.password_settings_requests_dto import PasswordSettingsRequestsDto
from docspace_api_sdk.models.password_settings_wrapper import PasswordSettingsWrapper
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
    api_instance = docspace_api_sdk.SecurityApi(api_client)
    password_settings_requests_dto = docspace_api_sdk.PasswordSettingsRequestsDto() # PasswordSettingsRequestsDto |  (optional)

    try:
        # Set the password settings
        api_response = api_instance.update_password_settings(password_settings_requests_dto=password_settings_requests_dto)
        print("The response of SecurityApi->update_password_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SecurityApi->update_password_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Password settings |  -  |
**400** | MinLength |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

