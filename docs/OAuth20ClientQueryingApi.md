# docspace_api_sdk.ClientQueryingApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_client**](#get_client) | **GET** /api/2.0/oauth2/clients/{clientId} | Get client details
[**get_client_info**](#get_client_info) | **GET** /api/2.0/oauth2/clients/{clientId}/info | Get client info
[**get_clients**](#get_clients) | **GET** /api/2.0/oauth2/clients | List clients
[**get_clients_info**](#get_clients_info) | **GET** /api/2.0/oauth2/clients/info | List client info
[**get_consents**](#get_consents) | **GET** /api/2.0/oauth2/clients/consents | List user consents
[**get_public_client_info**](#get_public_client_info) | **GET** /api/2.0/oauth2/clients/{clientId}/public/info | Get public client info


# **get_client**
> ClientResponse get_client(client_id)

Returns the whole stored record of one client: its name and description, its secret, scopes, redirect URIs, allowed origins, logout redirect URIs and audit fields. An administrator sees any client of the tenant, a plain user only the clients they created, and a guest none of them. Whatever the caller may not see is reported as 404 rather than 403, so absence and lack of access are deliberately indistinguishable, and an identifier that is not a valid client ID is reported the same way. The response is a single object, not a collection.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to retrieve | 

### Return type

[**ClientResponse**](ClientResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.client_response import ClientResponse
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
    api_instance = docspace_api_sdk.ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to retrieve

    try:
        # Get client details
        api_response = api_instance.get_client(client_id)
        print("The response of ClientQueryingApi->get_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_client: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client details successfully retrieved |  -  |
**400** | The client ID is blank or contains only whitespace |  -  |
**403** | Insufficient permissions to view client |  -  |
**404** | No client with this ID is visible to the caller, or the ID cannot be parsed as a client ID |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_info**
> ClientInfoResponse get_client_info(client_id)

Retrieves the detailed information for a client with the ID specified in the request. It returns the consent-facing subset of the client - name, description, logo, the website, terms and policy URLs, authentication methods and scopes - and deliberately omits the secret, the redirect URIs and the allowed origins, which is what makes it safe to render on a consent screen. An administrator sees any client of the tenant, a plain user only the clients they created, and a guest none of them. A client the caller may not see is reported as 404, exactly like an unknown one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to retrieve | 

### Return type

[**ClientInfoResponse**](ClientInfoResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.client_info_response import ClientInfoResponse
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
    api_instance = docspace_api_sdk.ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to retrieve

    try:
        # Get client info
        api_response = api_instance.get_client_info(client_id)
        print("The response of ClientQueryingApi->get_client_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_client_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved client info |  -  |
**400** | The client ID is blank or contains only whitespace |  -  |
**403** | Insufficient permissions to view client information |  -  |
**404** | No client with this ID is visible to the caller, or the ID cannot be parsed as a client ID |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients**
> PageableClientResponse get_clients(limit=limit, last_client_id=last_client_id, last_created_on=last_created_on)

Returns one page of the tenant's clients, newest first, each in the same full form as the single-client read. An administrator sees every client of the tenant, a plain user only the clients they created. Paging is keyset-based rather than offset-based: limit sets the page size, and last_client_id and last_created_on are carried over from the previous page to ask for the next one. The limit defaults to 30 and has to lie between 1 and 50; a value outside that range, or a last_created_on that cannot be parsed as a date, is rejected with 400.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many entries to return, between 1 and 50. Defaults to 30 when omitted. | [optional] [default to 30]
 **last_client_id** | **str**| ID of the last retrieved client | [optional] 
 **last_created_on** | **datetime**| Date of the last retrieved client | [optional] 

### Return type

[**PageableClientResponse**](PageableClientResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.pageable_client_response import PageableClientResponse
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
    api_instance = docspace_api_sdk.ClientQueryingApi(api_client)
    limit = 30 # int | How many entries to return, between 1 and 50. Defaults to 30 when omitted. (optional) (default to 30)
    last_client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the last retrieved client (optional)
    last_created_on = '2024-04-04T12:00:00Z' # datetime | Date of the last retrieved client (optional)

    try:
        # List clients
        api_response = api_instance.get_clients(limit=limit, last_client_id=last_client_id, last_created_on=last_created_on)
        print("The response of ClientQueryingApi->get_clients:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_clients: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Client list successfully retrieved |  -  |
**400** | Invalid pagination parameters, including a last_created_on that cannot be parsed as a date-time |  -  |
**403** | Insufficient permissions to list clients |  -  |
**406** | The Accept header does not allow application/json |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_clients_info**
> PageableClientInfoResponse get_clients_info(limit, last_client_id=last_client_id, last_created_on=last_created_on)

Retrieves a paginated list of information for all clients, each in the same consent-facing form as the single-client info read. An administrator sees every client of the tenant, a plain user only the clients they created. Paging is keyset-based: limit sets the page size, and last_client_id and last_created_on are carried over from the previous page. Unlike the full client listing, limit has no default here - it has to be supplied on every call and has to lie between 1 and 50, and a missing or out-of-range value is rejected with 400.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many entries to return, between 1 and 50. It has no default and has to be sent on every call. | 
 **last_client_id** | **str**| ID of the last retrieved client | [optional] 
 **last_created_on** | **datetime**| Date of the last retrieved client | [optional] 

### Return type

[**PageableClientInfoResponse**](PageableClientInfoResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.pageable_client_info_response import PageableClientInfoResponse
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
    api_instance = docspace_api_sdk.ClientQueryingApi(api_client)
    limit = 30 # int | How many entries to return, between 1 and 50. It has no default and has to be sent on every call.
    last_client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the last retrieved client (optional)
    last_created_on = '2024-04-04T12:00:00Z' # datetime | Date of the last retrieved client (optional)

    try:
        # List client info
        api_response = api_instance.get_clients_info(limit, last_client_id=last_client_id, last_created_on=last_created_on)
        print("The response of ClientQueryingApi->get_clients_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_clients_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved clients info |  -  |
**400** | The limit parameter is missing, is outside the range 1-50, or last_created_on cannot be parsed as a date-time |  -  |
**403** | Insufficient permissions to list client information |  -  |
**406** | The Accept header does not allow application/json |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_consents**
> PageableModificationResponse get_consents(limit, last_modified_on=last_modified_on)

Retrieves a paginated list of user consents: the clients the calling user has authorized, each with the scopes granted, the moment the consent was last changed and the client's consent-facing details. It always reports the caller's own consents and nothing else - there is no role check on this endpoint, so guests may call it too, and no parameter widens it to another user. The consents are read from the authorization service over gRPC, so an authorization service that cannot be reached surfaces as 503. Paging is keyset-based on last_modified_on, and limit has no default: it has to be supplied on every call and has to lie between 1 and 50.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| How many entries to return, between 1 and 50. It has no default and has to be sent on every call. | 
 **last_modified_on** | **datetime**| Date of the last retrieved consent | [optional] 

### Return type

[**PageableModificationResponse**](PageableModificationResponse.md)

### Authorization

[x-signature](../README.md#x-signature)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.pageable_modification_response import PageableModificationResponse
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
    api_instance = docspace_api_sdk.ClientQueryingApi(api_client)
    limit = 30 # int | How many entries to return, between 1 and 50. It has no default and has to be sent on every call.
    last_modified_on = '2024-04-04T12:00:00Z' # datetime | Date of the last retrieved consent (optional)

    try:
        # List user consents
        api_response = api_instance.get_consents(limit, last_modified_on=last_modified_on)
        print("The response of ClientQueryingApi->get_consents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_consents: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved user consents |  -  |
**400** | The limit parameter is missing, is outside the range 1-50, or last_modified_on cannot be parsed as a date-time |  -  |
**403** | The request carries no valid portal signature |  -  |
**406** | The Accept header does not allow application/json |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**503** | Authorization service unavailable |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_public_client_info**
> ClientInfoResponse get_public_client_info(client_id)

Returns the same consent-facing client information as the signed read, but without requiring a portal signature. It is meant for a login or consent page that has to render the client before the user is known, so it resolves the client by ID alone: there is no authentication, no tenant scoping and no creator check, and any caller who knows a client ID can read that client's public details. It still exposes no secret, no redirect URIs and no allowed origins. Being unauthenticated it is rate-limited on a separate, tighter budget than the signed endpoints. An unknown client ID, and an identifier that is not a client ID at all, are both reported as 404.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**| ID of the client to retrieve | 

### Return type

[**ClientInfoResponse**](ClientInfoResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.client_info_response import ClientInfoResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ClientQueryingApi(api_client)
    client_id = '6c7cf17b-1bd3-47d5-94c6-be2d3570e168' # str | ID of the client to retrieve

    try:
        # Get public client info
        api_response = api_instance.get_public_client_info(client_id)
        print("The response of ClientQueryingApi->get_public_client_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ClientQueryingApi->get_public_client_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully retrieved client public info |  -  |
**400** | The client ID is blank or contains only whitespace |  -  |
**404** | No client with this ID exists, or the ID cannot be parsed as a client ID |  -  |
**429** | Too many requests - rate limit exceeded |  -  |
**500** | Internal server error occurred |  -  |
**405** | The HTTP method is not allowed for this path |  -  |
**406** | The Accept header does not allow application/json |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

