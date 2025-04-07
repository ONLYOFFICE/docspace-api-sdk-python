# docspace.SettingsCustomNavigationApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_custom_navigation_item**](SettingsCustomNavigationApi.md#create_custom_navigation_item) | **POST** /api/2.0/settings/customnavigation/create | Add a custom navigation item
[**delete_custom_navigation_item**](SettingsCustomNavigationApi.md#delete_custom_navigation_item) | **DELETE** /api/2.0/settings/customnavigation/delete/{id} | Delete a custom navigation item
[**get_custom_navigation_item**](SettingsCustomNavigationApi.md#get_custom_navigation_item) | **GET** /api/2.0/settings/customnavigation/get/{id} | Get a custom navigation item by ID
[**get_custom_navigation_item_sample**](SettingsCustomNavigationApi.md#get_custom_navigation_item_sample) | **GET** /api/2.0/settings/customnavigation/getsample | Get a custom navigation item sample
[**get_custom_navigation_items**](SettingsCustomNavigationApi.md#get_custom_navigation_items) | **GET** /api/2.0/settings/customnavigation/getall | Get the custom navigation items


# **create_custom_navigation_item**
> CustomNavigationItemWrapper create_custom_navigation_item(custom_navigation_item=custom_navigation_item)

Add a custom navigation item

Adds a custom navigation item with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.custom_navigation_item import CustomNavigationItem
from docspace.models.custom_navigation_item_wrapper import CustomNavigationItemWrapper
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
    api_instance = docspace.SettingsCustomNavigationApi(api_client)
    custom_navigation_item = docspace.CustomNavigationItem() # CustomNavigationItem |  (optional)

    try:
        # Add a custom navigation item
        api_response = api_instance.create_custom_navigation_item(custom_navigation_item=custom_navigation_item)
        print("The response of SettingsCustomNavigationApi->create_custom_navigation_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsCustomNavigationApi->create_custom_navigation_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_navigation_item** | [**CustomNavigationItem**](CustomNavigationItem.md)|  | [optional] 

### Return type

[**CustomNavigationItemWrapper**](CustomNavigationItemWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom navigation item |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_custom_navigation_item**
> delete_custom_navigation_item(id)

Delete a custom navigation item

Deletes a custom navigation item with the ID specified in the request.

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
    api_instance = docspace.SettingsCustomNavigationApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | Id

    try:
        # Delete a custom navigation item
        api_instance.delete_custom_navigation_item(id)
    except Exception as e:
        print("Exception when calling SettingsCustomNavigationApi->delete_custom_navigation_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

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
**200** | OK |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_navigation_item**
> CustomNavigationItemWrapper get_custom_navigation_item(id)

Get a custom navigation item by ID

Returns a custom navigation item by the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.custom_navigation_item_wrapper import CustomNavigationItemWrapper
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
    api_instance = docspace.SettingsCustomNavigationApi(api_client)
    id = 'aae1e103-bca5-9fa1-ba8c-42058b4abf28' # str | Id

    try:
        # Get a custom navigation item by ID
        api_response = api_instance.get_custom_navigation_item(id)
        print("The response of SettingsCustomNavigationApi->get_custom_navigation_item:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsCustomNavigationApi->get_custom_navigation_item: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

[**CustomNavigationItemWrapper**](CustomNavigationItemWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom navigation item |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_navigation_item_sample**
> CustomNavigationItemWrapper get_custom_navigation_item_sample()

Get a custom navigation item sample

Returns a custom navigation item sample.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.custom_navigation_item_wrapper import CustomNavigationItemWrapper
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
    api_instance = docspace.SettingsCustomNavigationApi(api_client)

    try:
        # Get a custom navigation item sample
        api_response = api_instance.get_custom_navigation_item_sample()
        print("The response of SettingsCustomNavigationApi->get_custom_navigation_item_sample:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsCustomNavigationApi->get_custom_navigation_item_sample: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomNavigationItemWrapper**](CustomNavigationItemWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom navigation item |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_navigation_items**
> CustomNavigationItemArrayWrapper get_custom_navigation_items()

Get the custom navigation items

Returns a list of the custom navigation items.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.custom_navigation_item_array_wrapper import CustomNavigationItemArrayWrapper
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
    api_instance = docspace.SettingsCustomNavigationApi(api_client)

    try:
        # Get the custom navigation items
        api_response = api_instance.get_custom_navigation_items()
        print("The response of SettingsCustomNavigationApi->get_custom_navigation_items:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsCustomNavigationApi->get_custom_navigation_items: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**CustomNavigationItemArrayWrapper**](CustomNavigationItemArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of the custom navigation items |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

