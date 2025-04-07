# docspace.PeopleThemeApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_theme**](PeopleThemeApi.md#change_theme) | **PUT** /api/2.0/people/theme | Change portal theme
[**get_theme**](PeopleThemeApi.md#get_theme) | **GET** /api/2.0/people/theme | Get portal theme


# **change_theme**
> DarkThemeSettingsWrapper change_theme(dark_theme_settings_request_dto=dark_theme_settings_request_dto)

Change portal theme

Changes the current portal theme.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.dark_theme_settings_request_dto import DarkThemeSettingsRequestDto
from docspace.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper
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
    api_instance = docspace.PeopleThemeApi(api_client)
    dark_theme_settings_request_dto = docspace.DarkThemeSettingsRequestDto() # DarkThemeSettingsRequestDto |  (optional)

    try:
        # Change portal theme
        api_response = api_instance.change_theme(dark_theme_settings_request_dto=dark_theme_settings_request_dto)
        print("The response of PeopleThemeApi->change_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleThemeApi->change_theme: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dark_theme_settings_request_dto** | [**DarkThemeSettingsRequestDto**](DarkThemeSettingsRequestDto.md)|  | [optional] 

### Return type

[**DarkThemeSettingsWrapper**](DarkThemeSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_theme**
> DarkThemeSettingsWrapper get_theme()

Get portal theme

Returns a theme which is set to the current portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper
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
    api_instance = docspace.PeopleThemeApi(api_client)

    try:
        # Get portal theme
        api_response = api_instance.get_theme()
        print("The response of PeopleThemeApi->get_theme:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleThemeApi->get_theme: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DarkThemeSettingsWrapper**](DarkThemeSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Theme |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

