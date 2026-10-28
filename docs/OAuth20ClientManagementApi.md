# docspace_api_sdk.ClientManagementApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_activation**](#change_activation) | **PATCH** /api/2.0/oauth2/clients/{clientId}/activation | Change client activation status
[**create_client**](#create_client) | **POST** /api/2.0/oauth2/clients | Create a new OAuth2 client
[**delete_client**](#delete_client) | **DELETE** /api/2.0/oauth2/clients/{clientId} | Delete an OAuth2 client
[**delete_tenant_clients**](#delete_tenant_clients) | **DELETE** /api/2.0/oauth2/clients/tenant | Delete all tenant OAuth2 clients
[**delete_user_clients**](#delete_user_clients) | **DELETE** /api/2.0/oauth2/clients | Delete all user OAuth2 clients
[**regenerate_secret**](#regenerate_secret) | **PATCH** /api/2.0/oauth2/clients/{clientId}/regenerate | Regenerate client secret
[**revoke_user_client**](#revoke_user_client) | **DELETE** /api/2.0/oauth2/clients/{clientId}/revoke | Revoke client consent
[**update_client**](#update_client) | **PUT** /api/2.0/oauth2/clients/{clientId} | Update an existing OAuth2 client


# **change_activation**
> change_activation(client_id, change_client_activation_request)

Enables or disables an existing client and answers 200 with an empty body. A disabled client can no longer obtain new tokens, but the tokens and consents it already holds stay valid until they expire on their own: disable a client to stop new authorizations, delete it to end the existing ones. An administrator may change any client of the tenant, a plain user only the clients they created. The body carries the single activation flag, and a client the caller may not see is reported as not found rather than as forbidden.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to change activation for | 
 **change_client_activation_request** | [**ChangeClientActivationRequest**](ChangeClientActivationRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_client_activation_request import ChangeClientActivationRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to change activation for
    change_client_activation_request = docspace_api_sdk.ChangeClientActivationRequest() # ChangeClientActivationRequest | 

    try:
        # Change client activation status
        api_instance.change_activation(client_id, change_client_activation_request)
    except Exception as e:
        print("Exception when calling ClientManagementApi->change_activation: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client activation status successfully changed |  -  |
**400** | The client ID is blank, or the activation status is missing |  -  |
**403** | Insufficient permissions to change client activation |  -  |
**404** | No client with this ID is visible to the caller, or the ID cannot be parsed as a client ID |  -  |
**415** | The Content-Type header is not application/json |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_client**
> ClientResponse create_client(create_client_request)

Registers a new OAuth2 client in the caller's tenant and returns it. The body must carry a name, a description, a logo and at least one redirect URI, allowed origin and scope, and every scope named must already exist in the tenant's scope catalogue. Administrators and users may both register clients; the caller is recorded as the creator, which is what later restricts a plain user to the clients they created. The response is the stored client with its generated client ID and secret, and it is the first place either value can be read. Some deployments cap how many clients one tenant may hold, and reaching that cap is reported as 400 together with the validation failures.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_client_request** | [**CreateClientRequest**](CreateClientRequest.md)|  | 

### Return type

[**ClientResponse**](ClientResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.client_response import ClientResponse
from docspace_api_sdk.models.create_client_request import CreateClientRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)
    create_client_request = docspace_api_sdk.CreateClientRequest() # CreateClientRequest | 

    try:
        # Create a new OAuth2 client
        api_response = api_instance.create_client(create_client_request)
        print("The response of ClientManagementApi->create_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->create_client: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Client successfully created |  -  |
**400** | Missing required fields, validation failed, an unknown scope was requested, or the client limit for this tenant has been reached |  -  |
**403** | Insufficient permissions to create client |  -  |
**415** | The Content-Type header is not application/json |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_client**
> delete_client(client_id)

Deletes one client from the tenant permanently and answers 200 with an empty body. An administrator may delete any client of the tenant, a plain user only the clients they created, and a client the caller may not see is reported as not found rather than as forbidden. The authorizations and consents issued for the client are removed too, but that cleanup is driven by a message and completes on the authorization service after this call has already returned. A delete that removes no row answers 400. The operation cannot be undone.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to delete | 

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to delete

    try:
        # Delete an OAuth2 client
        api_instance.delete_client(client_id)
    except Exception as e:
        print("Exception when calling ClientManagementApi->delete_client: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client successfully deleted |  -  |
**400** | The client ID is blank, or the client could not be deleted |  -  |
**403** | Insufficient permissions to delete client |  -  |
**404** | No client with this ID is visible to the caller, or the ID cannot be parsed as a client ID |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_tenant_clients**
> delete_tenant_clients()

Deletes every client registered in the current tenant and answers 200 with an empty body. Only an administrator may call it - for a plain user or a guest it is refused with 403 - and it removes the clients of all users of the tenant, not only those of the caller. The authorizations and consents of the deleted clients are cleaned up asynchronously on the authorization service, and the tenant's client cache is dropped as part of the call. Concurrent modification that survives the retries is reported as 400. The operation cannot be undone, and the response does not say how many clients were removed.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)

    try:
        # Delete all tenant OAuth2 clients
        api_instance.delete_tenant_clients()
    except Exception as e:
        print("Exception when calling ClientManagementApi->delete_tenant_clients: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client successfully deleted |  -  |
**400** | The clients could not be deleted because of concurrent modification |  -  |
**403** | Insufficient permissions to delete tenant clients |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_clients**
> delete_user_clients()

Deletes every client the calling user created in the current tenant and answers 200 with an empty body. The caller's own identity always selects the set, so this never reaches clients created by somebody else, not even for an administrator. The authorizations and consents of the deleted clients are cleaned up asynchronously on the authorization service, and the tenant's client cache is dropped as part of the call. Concurrent modification that survives the retries is reported as 400. The operation cannot be undone, and the response does not say how many clients were removed.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)

    try:
        # Delete all user OAuth2 clients
        api_instance.delete_user_clients()
    except Exception as e:
        print("Exception when calling ClientManagementApi->delete_user_clients: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client successfully deleted |  -  |
**400** | The clients could not be deleted because of concurrent modification |  -  |
**403** | Insufficient permissions to delete user clients |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_secret**
> ClientSecretResponse regenerate_secret(client_id)

Issues a new secret for the client and returns it. The previous secret stops working as soon as this call succeeds, there is no grace period and no way to recover it, so every deployed copy of the client has to be updated with the value returned here. An administrator may do this for any client of the tenant, a plain user only for the clients they created. Tokens already issued to the client keep working; only future client authentication is affected. The response carries the new secret and nothing else.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to regenerate secret for | 

### Return type

[**ClientSecretResponse**](ClientSecretResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.client_secret_response import ClientSecretResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to regenerate secret for

    try:
        # Regenerate client secret
        api_response = api_instance.regenerate_secret(client_id)
        print("The response of ClientManagementApi->regenerate_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientManagementApi->regenerate_secret: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client secret successfully regenerated |  -  |
**400** | The client ID is blank or contains only whitespace |  -  |
**403** | Insufficient permissions to regenerate client secret |  -  |
**404** | No client with this ID is visible to the caller, or the ID cannot be parsed as a client ID |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_user_client**
> revoke_user_client(client_id)

Revokes the calling user's own consent for one client and answers 200 with an empty body. It touches only the caller's grant: other users keep their consents and the client itself stays registered. Guests may call it as well as users and administrators, because it can never reach anyone else's data. The revocation is carried out by the authorization service over gRPC, so a service that reports nothing was revoked produces 400 and a service that cannot be reached produces 503. Once it succeeds the user has to authorize the client again before it can act on their behalf.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to revoke consent for | 

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to revoke consent for

    try:
        # Revoke client consent
        api_instance.revoke_user_client(client_id)
    except Exception as e:
        print("Exception when calling ClientManagementApi->revoke_user_client: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client consent successfully revoked |  -  |
**400** | The client ID is blank, or the authorization service reported that the consent was not revoked |  -  |
**403** | Insufficient permissions to revoke consent |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**503** | Authorization service unavailable |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client**
> update_client(client_id, update_client_request)

Updates the mutable settings of an existing client and answers 200 with an empty body. Only the fields carried in the request body change; the client ID, the secret, the tenant and the creator cannot be changed this way. An administrator may update any client of the tenant, a plain user only the clients they created, and a client the caller may not see is reported as not found rather than as forbidden. The write runs under optimistic locking and is retried a few times, so a request that still loses the race is rejected with 400 instead of silently overwriting a concurrent change. Nothing is returned in the body - read the client back to see the stored result.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to update | 
 **update_client_request** | [**UpdateClientRequest**](UpdateClientRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.update_client_request import UpdateClientRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientManagementApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to update
    update_client_request = docspace_api_sdk.UpdateClientRequest() # UpdateClientRequest | 

    try:
        # Update an existing OAuth2 client
        api_instance.update_client(client_id, update_client_request)
    except Exception as e:
        print("Exception when calling ClientManagementApi->update_client: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client successfully updated |  -  |
**400** | Missing required fields, validation failed, or the client could not be updated because of concurrent modification |  -  |
**403** | Insufficient permissions to update client |  -  |
**404** | No client with this ID is visible to the caller, or the ID cannot be parsed as a client ID |  -  |
**415** | The Content-Type header is not application/json |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

