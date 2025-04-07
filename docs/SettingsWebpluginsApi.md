# docspace.SettingsWebpluginsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_web_plugin_from_file**](SettingsWebpluginsApi.md#add_web_plugin_from_file) | **POST** /api/2.0/settings/webplugins | Adds web plugins from file
[**delete_web_plugin**](SettingsWebpluginsApi.md#delete_web_plugin) | **DELETE** /api/2.0/settings/webplugins/{name} | Deletes web plugins by name specified in request
[**get_web_plugin**](SettingsWebpluginsApi.md#get_web_plugin) | **GET** /api/2.0/settings/webplugins/{name} | Gets web plugins by name specified in request
[**get_web_plugins**](SettingsWebpluginsApi.md#get_web_plugins) | **GET** /api/2.0/settings/webplugins | Gets web plugins
[**update_web_plugin**](SettingsWebpluginsApi.md#update_web_plugin) | **PUT** /api/2.0/settings/webplugins/{name} | Updates web plugins


# **add_web_plugin_from_file**
> WebPluginWrapper add_web_plugin_from_file(system=system)

Adds web plugins from file

Adds web plugins from file

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.web_plugin_wrapper import WebPluginWrapper
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
    api_instance = docspace.SettingsWebpluginsApi(api_client)
    system = true # bool | System (optional)

    try:
        # Adds web plugins from file
        api_response = api_instance.add_web_plugin_from_file(system=system)
        print("The response of SettingsWebpluginsApi->add_web_plugin_from_file:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebpluginsApi->add_web_plugin_from_file: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **system** | **bool**| System | [optional] 

### Return type

[**WebPluginWrapper**](WebPluginWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web plugin |  -  |
**400** | bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Plugins disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_web_plugin**
> delete_web_plugin(name)

Deletes web plugins by name specified in request

Deletes web plugins by name specified in request

### Example

* Api Key Authentication (asc_auth_key):

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

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsWebpluginsApi(api_client)
    name = 'Winfield Upton' # str | Name

    try:
        # Deletes web plugins by name specified in request
        api_instance.delete_web_plugin(name)
    except Exception as e:
        print("Exception when calling SettingsWebpluginsApi->delete_web_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Plugins disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_plugin**
> WebPluginWrapper get_web_plugin(name)

Gets web plugins by name specified in request

Gets web plugins by name specified in request

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.web_plugin_wrapper import WebPluginWrapper
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
    api_instance = docspace.SettingsWebpluginsApi(api_client)
    name = 'Winfield Upton' # str | Name

    try:
        # Gets web plugins by name specified in request
        api_response = api_instance.get_web_plugin(name)
        print("The response of SettingsWebpluginsApi->get_web_plugin:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebpluginsApi->get_web_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 

### Return type

[**WebPluginWrapper**](WebPluginWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web plugin |  -  |
**401** | Unauthorized |  -  |
**403** | Plugins disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_web_plugins**
> WebPluginArrayWrapper get_web_plugins(enabled=enabled)

Gets web plugins

Gets web plugins

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.web_plugin_array_wrapper import WebPluginArrayWrapper
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
    api_instance = docspace.SettingsWebpluginsApi(api_client)
    enabled = true # bool | Enabled (optional)

    try:
        # Gets web plugins
        api_response = api_instance.get_web_plugins(enabled=enabled)
        print("The response of SettingsWebpluginsApi->get_web_plugins:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsWebpluginsApi->get_web_plugins: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enabled** | **bool**| Enabled | [optional] 

### Return type

[**WebPluginArrayWrapper**](WebPluginArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Web plugin |  -  |
**401** | Unauthorized |  -  |
**403** | Plugins disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_web_plugin**
> update_web_plugin(name, web_plugin_requests=web_plugin_requests)

Updates web plugins

Updates web plugins

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.web_plugin_requests import WebPluginRequests
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
    api_instance = docspace.SettingsWebpluginsApi(api_client)
    name = 'Winfield Upton' # str | Name
    web_plugin_requests = docspace.WebPluginRequests() # WebPluginRequests | Web plugin (optional)

    try:
        # Updates web plugins
        api_instance.update_web_plugin(name, web_plugin_requests=web_plugin_requests)
    except Exception as e:
        print("Exception when calling SettingsWebpluginsApi->update_web_plugin: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name | 
 **web_plugin_requests** | [**WebPluginRequests**](WebPluginRequests.md)| Web plugin | [optional] 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | Plugins disabled |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

