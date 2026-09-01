# docspace_api_sdk.PrivacyRoomApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_keys**](#delete_keys) | **DELETE** /api/2.0/privacyroom/keys/{id} | Deletes an encryption key and removes it from the system.
[**get_user_keys**](#get_user_keys) | **GET** /api/2.0/privacyroom/keys | Retrieves encryption keys associated with the current user.
[**get_user_keys_for_room**](#get_user_keys_for_room) | **GET** /api/2.0/privacyroom/{roomId}/access | Retrieves the encryption keys associated with a specific privacy room.
[**replace_key**](#replace_key) | **PUT** /api/2.0/privacyroom/keys | Replaces an existing encryption key with a new one for the user.
[**set_keys**](#set_keys) | **POST** /api/2.0/privacyroom/keys | Creates and sets encryption keys for the user.


# **delete_keys**
> delete_keys(id)

Deletes an encryption key and removes it from the system based on the provided key identifier.

Breaking change in DocSpace 4.0: the endpoint used to answer 200 with the caller's remaining
encryption keys and now answers 204 with no body. A client that read that list must call
`GET api/2.0/privacyroom/keys` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **UUID**| The unique identifier of the encryption key to be deleted. | 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PrivacyRoomApi(api_client)
    id = UUID('00000000-0000-0000-0000-000000000000') # UUID | The unique identifier of the encryption key to be deleted.

    try:
        # Deletes an encryption key and removes it from the system.
        api_instance.delete_keys(id)
    except Exception as e:
        print("Exception when calling PrivacyRoomApi->delete_keys: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The encryption key is deleted. Answered 200 with the remaining keys before DocSpace 4.0 |  -  |
**400** | The key identifier is not a valid GUID |  -  |
**404** | The encryption key is not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_keys**
> EncryptionKeyArrayWrapper get_user_keys()

Retrieves encryption keys associated with the current user.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**EncryptionKeyArrayWrapper**](EncryptionKeyArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.encryption_key_array_wrapper import EncryptionKeyArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PrivacyRoomApi(api_client)

    try:
        # Retrieves encryption keys associated with the current user.
        api_response = api_instance.get_user_keys()
        print("The response of PrivacyRoomApi->get_user_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivacyRoomApi->get_user_keys: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_keys_for_room**
> EncryptionKeyArrayWrapper get_user_keys_for_room(room_id)

Retrieves the encryption keys associated with a specific privacy room.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_id** | **int**| The identifier of the privacy room. | 

### Return type

[**EncryptionKeyArrayWrapper**](EncryptionKeyArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.encryption_key_array_wrapper import EncryptionKeyArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PrivacyRoomApi(api_client)
    room_id = 56 # int | The identifier of the privacy room.

    try:
        # Retrieves the encryption keys associated with a specific privacy room.
        api_response = api_instance.get_user_keys_for_room(room_id)
        print("The response of PrivacyRoomApi->get_user_keys_for_room:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivacyRoomApi->get_user_keys_for_room: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_key**
> EncryptionKeyArrayWrapper replace_key(encryption_key_request_dto=encryption_key_request_dto)

Replaces an existing encryption key with a new one for the user.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encryption_key_request_dto** | [**EncryptionKeyRequestDto**](EncryptionKeyRequestDto.md)| The request object containing the public and private key information to replace the existing key. | [optional] 

### Return type

[**EncryptionKeyArrayWrapper**](EncryptionKeyArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.encryption_key_array_wrapper import EncryptionKeyArrayWrapper
from docspace_api_sdk.models.encryption_key_request_dto import EncryptionKeyRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PrivacyRoomApi(api_client)
    encryption_key_request_dto = docspace_api_sdk.EncryptionKeyRequestDto() # EncryptionKeyRequestDto | The request object containing the public and private key information to replace the existing key. (optional)

    try:
        # Replaces an existing encryption key with a new one for the user.
        api_response = api_instance.replace_key(encryption_key_request_dto=encryption_key_request_dto)
        print("The response of PrivacyRoomApi->replace_key:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivacyRoomApi->replace_key: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The encryption key is replaced |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The key material is missing, blank or too large to be stored |  -  |
**404** | The encryption key to replace is not found |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_keys**
> EncryptionKeyArrayWrapper set_keys(encryption_key_request_dto=encryption_key_request_dto)

Creates and sets encryption keys for the user.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **encryption_key_request_dto** | [**EncryptionKeyRequestDto**](EncryptionKeyRequestDto.md)| The request object containing public and private key information. | [optional] 

### Return type

[**EncryptionKeyArrayWrapper**](EncryptionKeyArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.encryption_key_array_wrapper import EncryptionKeyArrayWrapper
from docspace_api_sdk.models.encryption_key_request_dto import EncryptionKeyRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PrivacyRoomApi(api_client)
    encryption_key_request_dto = docspace_api_sdk.EncryptionKeyRequestDto() # EncryptionKeyRequestDto | The request object containing public and private key information. (optional)

    try:
        # Creates and sets encryption keys for the user.
        api_response = api_instance.set_keys(encryption_key_request_dto=encryption_key_request_dto)
        print("The response of PrivacyRoomApi->set_keys:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PrivacyRoomApi->set_keys: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The encryption key is created. Answered 200 before DocSpace 4.0; the response body is unchanged |  -  |
**400** | The key material is missing, blank or too large to be stored |  -  |
**409** | A key with the same identifier already exists |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

