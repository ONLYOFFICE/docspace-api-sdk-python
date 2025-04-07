# docspace.SettingsTipsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tips_subscription**](SettingsTipsApi.md#get_tips_subscription) | **GET** /api/2.0/settings/tips/subscription | Check the tip subscription
[**update_tips_settings**](SettingsTipsApi.md#update_tips_settings) | **PUT** /api/2.0/settings/tips | Update the tip settings
[**update_tips_subscription**](SettingsTipsApi.md#update_tips_subscription) | **PUT** /api/2.0/settings/tips/change/subscription | Update the tip subscription


# **get_tips_subscription**
> BooleanWrapper get_tips_subscription()

Check the tip subscription

Checks if the current user is subscribed to the tips or not.

### Example

* Api Key Authentication (asc_auth_key):

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
    api_instance = docspace.SettingsTipsApi(api_client)

    try:
        # Check the tip subscription
        api_response = api_instance.get_tips_subscription()
        print("The response of SettingsTipsApi->get_tips_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTipsApi->get_tips_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the user is subscribed to the tips |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tips_settings**
> TipsSettingsWrapper update_tips_settings(tips_request_dto=tips_request_dto)

Update the tip settings

Updates the tip settings with a parameter specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.tips_request_dto import TipsRequestDto
from docspace.models.tips_settings_wrapper import TipsSettingsWrapper
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
    api_instance = docspace.SettingsTipsApi(api_client)
    tips_request_dto = docspace.TipsRequestDto() # TipsRequestDto |  (optional)

    try:
        # Update the tip settings
        api_response = api_instance.update_tips_settings(tips_request_dto=tips_request_dto)
        print("The response of SettingsTipsApi->update_tips_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTipsApi->update_tips_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tips_request_dto** | [**TipsRequestDto**](TipsRequestDto.md)|  | [optional] 

### Return type

[**TipsSettingsWrapper**](TipsSettingsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated tip settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tips_subscription**
> BooleanWrapper update_tips_subscription()

Update the tip subscription

Updates the tip subscription.

### Example

* Api Key Authentication (asc_auth_key):

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
    api_instance = docspace.SettingsTipsApi(api_client)

    try:
        # Update the tip subscription
        api_response = api_instance.update_tips_subscription()
        print("The response of SettingsTipsApi->update_tips_subscription:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTipsApi->update_tips_subscription: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the user is subscribed to the tips |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

