# docspace.OAuth20ClientQueryingApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client**](OAuth20ClientQueryingApi.md#get_client) | **GET** /api/2.0/clients/{clientId} | Get client details
[**get_client_info**](OAuth20ClientQueryingApi.md#get_client_info) | **GET** /api/2.0/clients/{clientId}/info | Get detailed client information
[**get_clients**](OAuth20ClientQueryingApi.md#get_clients) | **GET** /api/2.0/clients | Get clients
[**get_clients_info**](OAuth20ClientQueryingApi.md#get_clients_info) | **GET** /api/2.0/clients/info | Get detailed information of clients
[**get_consents**](OAuth20ClientQueryingApi.md#get_consents) | **GET** /api/2.0/clients/consents | Get user consents
[**get_public_client_info**](OAuth20ClientQueryingApi.md#get_public_client_info) | **GET** /api/2.0/clients/{clientId}/public/info | Get public client information


# **get_client**
> ClientResponse get_client(client_id)

Get client details

Retrieves detailed information about a specific OAuth2 client including its name, description, redirect URIs, and scopes.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.client_response import ClientResponse
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
    api_instance = docspace.OAuth20ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The client identifier.

    try:
        # Get client details
        api_response = api_instance.get_client(client_id)
        print("The response of OAuth20ClientQueryingApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ClientQueryingApi->get_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client identifier. | 

### Return type

[**ClientResponse**](ClientResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client details successfully retrieved |  -  |
**400** | Invalid client ID format |  -  |
**403** | Insufficient permissions to view client |  -  |
**404** | Client not found |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_info**
> ClientInfoResponse get_client_info(client_id)

Get detailed client information

Retrieves the detailed information for a client with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.client_info_response import ClientInfoResponse
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
    api_instance = docspace.OAuth20ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The client identifier.

    try:
        # Get detailed client information
        api_response = api_instance.get_client_info(client_id)
        print("The response of OAuth20ClientQueryingApi->get_client_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ClientQueryingApi->get_client_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client identifier. | 

### Return type

[**ClientInfoResponse**](ClientInfoResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved client info |  -  |
**400** | Bad request |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients**
> PageableResponse get_clients(limit, last_client_id=last_client_id, last_created_on=last_created_on)

Get clients

Retrieves a paginated list of OAuth2 clients. The results can be paginated using the 'limit' parameter and the last seen client ID or creation date.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.pageable_response import PageableResponse
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
    api_instance = docspace.OAuth20ClientQueryingApi(api_client)
    limit = 1 # int | The maximum number of results returned per page.
    last_client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The ID of the last retrieved client. (optional)
    last_created_on = '2024-04-04T12:00:00Z' # datetime | The creation date of the last retrieved client. (optional)

    try:
        # Get clients
        api_response = api_instance.get_clients(limit, last_client_id=last_client_id, last_created_on=last_created_on)
        print("The response of OAuth20ClientQueryingApi->get_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ClientQueryingApi->get_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results returned per page. | 
 **last_client_id** | **str**| The ID of the last retrieved client. | [optional] 
 **last_created_on** | **datetime**| The creation date of the last retrieved client. | [optional] 

### Return type

[**PageableResponse**](PageableResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client list successfully retrieved |  -  |
**400** | Invalid pagination parameters |  -  |
**403** | Insufficient permissions to create a client list |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients_info**
> PageableResponseClientInfoResponse get_clients_info(limit, last_client_id=last_client_id, last_created_on=last_created_on)

Get detailed information of clients

Retrieves a paginated list of information for all clients.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.pageable_response_client_info_response import PageableResponseClientInfoResponse
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
    api_instance = docspace.OAuth20ClientQueryingApi(api_client)
    limit = 1 # int | The maximum number of results returned per page.
    last_client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The identifier of the last retrieved client. (optional)
    last_created_on = '2024-04-04T12:00:00Z' # datetime | The creation date of the last retrieved client. (optional)

    try:
        # Get detailed information of clients
        api_response = api_instance.get_clients_info(limit, last_client_id=last_client_id, last_created_on=last_created_on)
        print("The response of OAuth20ClientQueryingApi->get_clients_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ClientQueryingApi->get_clients_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results returned per page. | 
 **last_client_id** | **str**| The identifier of the last retrieved client. | [optional] 
 **last_created_on** | **datetime**| The creation date of the last retrieved client. | [optional] 

### Return type

[**PageableResponseClientInfoResponse**](PageableResponseClientInfoResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved clients info |  -  |
**400** | Bad request |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents**
> PageableModificationResponse get_consents(limit, last_modified_on=last_modified_on)

Get user consents

Retrieves a paginated list of user consents.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.pageable_modification_response import PageableModificationResponse
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
    api_instance = docspace.OAuth20ClientQueryingApi(api_client)
    limit = 1 # int | The maximum number of results returned per page.
    last_modified_on = '2024-04-04T12:00:00Z' # datetime | The date when the user consent was last modified. (optional)

    try:
        # Get user consents
        api_response = api_instance.get_consents(limit, last_modified_on=last_modified_on)
        print("The response of OAuth20ClientQueryingApi->get_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ClientQueryingApi->get_consents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| The maximum number of results returned per page. | 
 **last_modified_on** | **datetime**| The date when the user consent was last modified. | [optional] 

### Return type

[**PageableModificationResponse**](PageableModificationResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved user consents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_client_info**
> ClientInfoResponse get_public_client_info(client_id)

Get public client information

Returns the public information for a client with the ID secified din the request.

### Example


```python
import docspace
from docspace.models.client_info_response import ClientInfoResponse
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
    api_instance = docspace.OAuth20ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | The client identifier.

    try:
        # Get public client information
        api_response = api_instance.get_public_client_info(client_id)
        print("The response of OAuth20ClientQueryingApi->get_public_client_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuth20ClientQueryingApi->get_public_client_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| The client identifier. | 

### Return type

[**ClientInfoResponse**](ClientInfoResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved client public info |  -  |
**400** | Bad request |  -  |
**429** | Too many requests |  -  |
**500** | Internal server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

