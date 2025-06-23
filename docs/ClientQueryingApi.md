# docspace.ClientQueryingApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client**](ClientQueryingApi.md#get_client) | **GET** /api/2.0/clients/{clientId} | Get client details
[**get_client_info**](ClientQueryingApi.md#get_client_info) | **GET** /api/2.0/clients/{clientId}/info | Retrieves detailed information for a specific client
[**get_clients**](ClientQueryingApi.md#get_clients) | **GET** /api/2.0/clients | List clients
[**get_clients_info**](ClientQueryingApi.md#get_clients_info) | **GET** /api/2.0/clients/info | Retrieves a pageable list of client information
[**get_consents**](ClientQueryingApi.md#get_consents) | **GET** /api/2.0/clients/consents | Retrieves a pageable list of consents
[**get_public_client_info**](ClientQueryingApi.md#get_public_client_info) | **GET** /api/2.0/clients/{clientId}/public/info | Handles the GET request for public client information


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
    api_instance = docspace.ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to retrieve

    try:
        # Get client details
        api_response = api_instance.get_client(client_id)
        print("The response of ClientQueryingApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to retrieve | 

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

Retrieves detailed information for a specific client

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
    api_instance = docspace.ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to retrieve

    try:
        # Retrieves detailed information for a specific client
        api_response = api_instance.get_client_info(client_id)
        print("The response of ClientQueryingApi->get_client_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_client_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to retrieve | 

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

List clients

Retrieves a paginated list of OAuth2 clients. The results can be paginated using the limit parameter and last seen client ID/creation date.

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
    api_instance = docspace.ClientQueryingApi(api_client)
    limit = 1 # int | Pagination limit
    last_client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the last retrieved client (optional)
    last_created_on = '2024-04-04T12:00:00Z' # datetime | Date of the last retrieved client (optional)

    try:
        # List clients
        api_response = api_instance.get_clients(limit, last_client_id=last_client_id, last_created_on=last_created_on)
        print("The response of ClientQueryingApi->get_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_clients: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Pagination limit | 
 **last_client_id** | **str**| ID of the last retrieved client | [optional] 
 **last_created_on** | **datetime**| Date of the last retrieved client | [optional] 

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
**403** | Insufficient permissions to list clients |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients_info**
> PageableResponseClientInfoResponse get_clients_info(limit, last_client_id=last_client_id, last_created_on=last_created_on)

Retrieves a pageable list of client information

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
    api_instance = docspace.ClientQueryingApi(api_client)
    limit = 1 # int | Pagination limit
    last_client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the last retrieved client (optional)
    last_created_on = '2024-04-04T12:00:00Z' # datetime | Date of the last retrieved client (optional)

    try:
        # Retrieves a pageable list of client information
        api_response = api_instance.get_clients_info(limit, last_client_id=last_client_id, last_created_on=last_created_on)
        print("The response of ClientQueryingApi->get_clients_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_clients_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Pagination limit | 
 **last_client_id** | **str**| ID of the last retrieved client | [optional] 
 **last_created_on** | **datetime**| Date of the last retrieved client | [optional] 

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

Retrieves a pageable list of consents

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
    api_instance = docspace.ClientQueryingApi(api_client)
    limit = 1 # int | Pagination limit
    last_modified_on = '2024-04-04T12:00:00Z' # datetime | Date of the last retrieved consent (optional)

    try:
        # Retrieves a pageable list of consents
        api_response = api_instance.get_consents(limit, last_modified_on=last_modified_on)
        print("The response of ClientQueryingApi->get_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_consents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Pagination limit | 
 **last_modified_on** | **datetime**| Date of the last retrieved consent | [optional] 

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

Handles the GET request for public client information

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
    api_instance = docspace.ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to retrieve

    try:
        # Handles the GET request for public client information
        api_response = api_instance.get_public_client_info(client_id)
        print("The response of ClientQueryingApi->get_public_client_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_public_client_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to retrieve | 

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

