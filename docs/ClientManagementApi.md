# docspace.ClientManagementApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_activation**](ClientManagementApi.md#change_activation) | **PATCH** /api/2.0/clients/{clientId}/activation | Change client activation status
[**create_client**](ClientManagementApi.md#create_client) | **POST** /api/2.0/clients | Create a new OAuth2 client
[**delete_client**](ClientManagementApi.md#delete_client) | **DELETE** /api/2.0/clients/{clientId} | Delete an OAuth2 client
[**regenerate_secret**](ClientManagementApi.md#regenerate_secret) | **PATCH** /api/2.0/clients/{clientId}/regenerate | Regenerate client secret
[**revoke_user_client**](ClientManagementApi.md#revoke_user_client) | **DELETE** /api/2.0/clients/{clientId}/revoke | Revoke client consent
[**update_client**](ClientManagementApi.md#update_client) | **PUT** /api/2.0/clients/{clientId} | Update an existing OAuth2 client


# **change_activation**
> object change_activation(client_id, change_client_activation_request)

Change client activation status

Activates or deactivates an OAuth2 client. When deactivated, the client cannot request new access tokens, but existing tokens will remain valid until they expire.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.change_client_activation_request import ChangeClientActivationRequest
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
    api_instance = docspace.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to change activation for
    change_client_activation_request = docspace.ChangeClientActivationRequest() # ChangeClientActivationRequest | 

    try:
        # Change client activation status
        api_response = api_instance.change_activation(client_id, change_client_activation_request)
        print("The response of ClientManagementApi->change_activation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->change_activation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to change activation for | 
 **change_client_activation_request** | [**ChangeClientActivationRequest**](ChangeClientActivationRequest.md)|  | 

### Return type

**object**

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client activation status successfully changed |  -  |
**400** | Invalid client ID format or activation status |  -  |
**403** | Insufficient permissions to change client activation |  -  |
**404** | Client not found |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client**
> ClientResponse create_client(create_client_request)

Create a new OAuth2 client

Creates a new OAuth2 client with the specified configuration. The client will be created with the provided scopes, redirect URIs, and other settings. Returns the created client details including the generated client ID.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.client_response import ClientResponse
from docspace.models.create_client_request import CreateClientRequest
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
    api_instance = docspace.ClientManagementApi(api_client)
    create_client_request = docspace.CreateClientRequest() # CreateClientRequest | 

    try:
        # Create a new OAuth2 client
        api_response = api_instance.create_client(create_client_request)
        print("The response of ClientManagementApi->create_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->create_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_request** | [**CreateClientRequest**](CreateClientRequest.md)|  | 

### Return type

[**ClientResponse**](ClientResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Client successfully created |  -  |
**400** | Invalid request - missing required fields or validation failed |  -  |
**403** | Insufficient permissions to create client |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> object delete_client(client_id)

Delete an OAuth2 client

Permanently deletes an OAuth2 client and all associated data. This will invalidate all access tokens and refresh tokens issued to this client. This operation cannot be undone.

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
    api_instance = docspace.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to delete

    try:
        # Delete an OAuth2 client
        api_response = api_instance.delete_client(client_id)
        print("The response of ClientManagementApi->delete_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->delete_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to delete | 

### Return type

**object**

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client successfully deleted |  -  |
**400** | Invalid client ID format |  -  |
**403** | Insufficient permissions to delete client |  -  |
**404** | Client not found |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_secret**
> ClientSecretResponse regenerate_secret(client_id)

Regenerate client secret

Generates a new client secret for the specified OAuth2 client. The old secret will be immediately invalidated. This operation should be used with caution as it requires updating the secret in all client applications.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.client_secret_response import ClientSecretResponse
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
    api_instance = docspace.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to regenerate secret for

    try:
        # Regenerate client secret
        api_response = api_instance.regenerate_secret(client_id)
        print("The response of ClientManagementApi->regenerate_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->regenerate_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to regenerate secret for | 

### Return type

[**ClientSecretResponse**](ClientSecretResponse.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client secret successfully regenerated |  -  |
**400** | Invalid client ID format |  -  |
**403** | Insufficient permissions to regenerate client secret |  -  |
**404** | Client not found |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_client**
> object revoke_user_client(client_id)

Revoke client consent

Revokes all user consents for the specified OAuth2 client. This will invalidate all access tokens and refresh tokens issued to this client for the current user. The user will need to re-authorize the client to access their resources.

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
    api_instance = docspace.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to revoke consent for

    try:
        # Revoke client consent
        api_response = api_instance.revoke_user_client(client_id)
        print("The response of ClientManagementApi->revoke_user_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->revoke_user_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to revoke consent for | 

### Return type

**object**

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client consent successfully revoked |  -  |
**400** | Invalid client ID format |  -  |
**403** | Insufficient permissions to revoke consent |  -  |
**404** | Client not found |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**503** | Authorization service unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> object update_client(client_id, update_client_request)

Update an existing OAuth2 client

Updates the configuration of an existing OAuth2 client. Allows modification of client name, description, redirect URIs, and other settings. The client ID cannot be modified.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.update_client_request import UpdateClientRequest
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
    api_instance = docspace.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to update
    update_client_request = docspace.UpdateClientRequest() # UpdateClientRequest | 

    try:
        # Update an existing OAuth2 client
        api_response = api_instance.update_client(client_id, update_client_request)
        print("The response of ClientManagementApi->update_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->update_client: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to update | 
 **update_client_request** | [**UpdateClientRequest**](UpdateClientRequest.md)|  | 

### Return type

**object**

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client successfully updated |  -  |
**400** | Invalid request - missing required fields or validation failed |  -  |
**403** | Insufficient permissions to update client |  -  |
**404** | Client not found |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

