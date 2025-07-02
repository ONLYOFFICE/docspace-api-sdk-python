# docspace-api-python.PeopleThemeApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_portal_theme**](#change_portal_theme) | **PUT** /api/2.0/people/theme | Change the portal theme
[**get_portal_theme**](#get_portal_theme) | **GET** /api/2.0/people/theme | Get the portal theme


# **change_portal_theme**
> DarkThemeSettingsWrapper change_portal_theme(dark_theme_settings_request_dto=dark_theme_settings_request_dto)

Changes the current portal theme.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dark_theme_settings_request_dto** | [**DarkThemeSettingsRequestDto**](DarkThemeSettingsRequestDto.md)|  | [optional] 

### Return type

[**DarkThemeSettingsWrapper**](DarkThemeSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.dark_theme_settings_request_dto import DarkThemeSettingsRequestDto
from docspace-api-python.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
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
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.PeopleThemeApi(api_client)
    dark_theme_settings_request_dto = docspace-api-python.DarkThemeSettingsRequestDto() # DarkThemeSettingsRequestDto |  (optional)

    try:
        # Change the portal theme
        api_response = api_instance.change_portal_theme(dark_theme_settings_request_dto=dark_theme_settings_request_dto)
        print("The response of PeopleThemeApi->change_portal_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleThemeApi->change_portal_theme: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_theme**
> DarkThemeSettingsWrapper get_portal_theme()

Returns a theme which is set to the current portal.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DarkThemeSettingsWrapper**](DarkThemeSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
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
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.PeopleThemeApi(api_client)

    try:
        # Get the portal theme
        api_response = api_instance.get_portal_theme()
        print("The response of PeopleThemeApi->get_portal_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleThemeApi->get_portal_theme: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

