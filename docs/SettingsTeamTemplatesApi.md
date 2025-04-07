# docspace.SettingsTeamTemplatesApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**people_schema**](SettingsTeamTemplatesApi.md#people_schema) | **GET** /api/2.0/settings/customschemas/{id} | Get a team template by ID
[**people_schemas**](SettingsTeamTemplatesApi.md#people_schemas) | **GET** /api/2.0/settings/customschemas | Get team templates
[**save_custom_naming_settings**](SettingsTeamTemplatesApi.md#save_custom_naming_settings) | **PUT** /api/2.0/settings/customschemas | Create a custom team template
[**save_naming_settings**](SettingsTeamTemplatesApi.md#save_naming_settings) | **POST** /api/2.0/settings/customschemas | Save the naming settings


# **people_schema**
> SchemaRequestsWrapper people_schema(id)

Get a team template by ID

Returns a team template by the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.schema_requests_wrapper import SchemaRequestsWrapper
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
    api_instance = docspace.SettingsTeamTemplatesApi(api_client)
    id = '9846' # str | Id

    try:
        # Get a team template by ID
        api_response = api_instance.people_schema(id)
        print("The response of SettingsTeamTemplatesApi->people_schema:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTeamTemplatesApi->people_schema: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Id | 

### Return type

[**SchemaRequestsWrapper**](SchemaRequestsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team template with the following parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **people_schemas**
> SchemaRequestsArrayWrapper people_schemas()

Get team templates

Returns all portal team templates that allow users to name their organization (or group), add members, and define their activities within the portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.schema_requests_array_wrapper import SchemaRequestsArrayWrapper
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
    api_instance = docspace.SettingsTeamTemplatesApi(api_client)

    try:
        # Get team templates
        api_response = api_instance.people_schemas()
        print("The response of SettingsTeamTemplatesApi->people_schemas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTeamTemplatesApi->people_schemas: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**SchemaRequestsArrayWrapper**](SchemaRequestsArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of team templates with the following parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_custom_naming_settings**
> SchemaRequestsWrapper save_custom_naming_settings(schema_requests_dto=schema_requests_dto)

Create a custom team template

Creates a custom team template with the parameters specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.schema_requests_dto import SchemaRequestsDto
from docspace.models.schema_requests_wrapper import SchemaRequestsWrapper
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
    api_instance = docspace.SettingsTeamTemplatesApi(api_client)
    schema_requests_dto = docspace.SchemaRequestsDto() # SchemaRequestsDto |  (optional)

    try:
        # Create a custom team template
        api_response = api_instance.save_custom_naming_settings(schema_requests_dto=schema_requests_dto)
        print("The response of SettingsTeamTemplatesApi->save_custom_naming_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTeamTemplatesApi->save_custom_naming_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_requests_dto** | [**SchemaRequestsDto**](SchemaRequestsDto.md)|  | [optional] 

### Return type

[**SchemaRequestsWrapper**](SchemaRequestsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Custom team template with the following parameters |  -  |
**400** | Please fill in all fields |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_naming_settings**
> SchemaRequestsWrapper save_naming_settings(schema_base_requests_dto=schema_base_requests_dto)

Save the naming settings

Saves the names from the team template with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.schema_base_requests_dto import SchemaBaseRequestsDto
from docspace.models.schema_requests_wrapper import SchemaRequestsWrapper
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
    api_instance = docspace.SettingsTeamTemplatesApi(api_client)
    schema_base_requests_dto = docspace.SchemaBaseRequestsDto() # SchemaBaseRequestsDto |  (optional)

    try:
        # Save the naming settings
        api_response = api_instance.save_naming_settings(schema_base_requests_dto=schema_base_requests_dto)
        print("The response of SettingsTeamTemplatesApi->save_naming_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsTeamTemplatesApi->save_naming_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **schema_base_requests_dto** | [**SchemaBaseRequestsDto**](SchemaBaseRequestsDto.md)|  | [optional] 

### Return type

[**SchemaRequestsWrapper**](SchemaRequestsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Team template with the following parameters |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

