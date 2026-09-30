# docspace_api_sdk.EncryptionApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_encryption_progress**](#get_storage_encryption_progress) | **GET** /api/2.0/settings/encryption/progress | Get the storage encryption progress
[**get_storage_encryption_settings**](#get_storage_encryption_settings) | **GET** /api/2.0/settings/encryption/settings | Get the storage encryption settings
[**start_storage_encryption**](#start_storage_encryption) | **POST** /api/2.0/settings/encryption/start | Start the storage encryption


# **get_storage_encryption_progress**
> DoubleNullableWrapper get_storage_encryption_progress()

Returns how far the running encryption or decryption of the installation storage has got, as a percentage from
0 to 100. It reports the run started by `POST api/2.0/settings/encryption/start`, whose direction, encryption
or decryption, is told by `GET api/2.0/settings/encryption/settings`. An empty response means no run is in
flight and no recent result is remembered: the value of a finished run is kept for one minute after it
completes and then dropped, so poll often enough not to miss the end of the operation. A value of -1 means the
build does not offer storage encryption at all, and on an installation that is not a server one the call is
refused rather than answered. Unlike the other encryption operations, this one asks for no portal-settings
permission: any authenticated member of the portal may read the progress, which is intentional, because the
portals are unavailable while the run is on and their users need to see when it ends. Nothing is written and
the call is safe to repeat.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DoubleNullableWrapper**](DoubleNullableWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.double_nullable_wrapper import DoubleNullableWrapper
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
    api_instance = docspace_api_sdk.EncryptionApi(api_client)

    try:
        # Get the storage encryption progress
        api_response = api_instance.get_storage_encryption_progress()
        print("The response of EncryptionApi->get_storage_encryption_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->get_storage_encryption_progress: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Encryption or decryption progress as a percentage, or empty when no run is in flight |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**405** | Storage encryption is not available on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_encryption_settings**
> EncryptionSettingsWrapper get_storage_encryption_settings()

Returns the encryption state of the installation storage: the status, which is one of decrypted, encryption
started, encrypted or decryption started, and the flag saying whether users are mailed when an encryption run
begins. The password is deliberately blanked out, so the field always comes back empty even on an encrypted
installation. The caller is expected to have the permission to edit portal settings, which in practice means
the portal owner or a DocSpace admin, on a server installation with an unrestricted access space; on any other
installation, and whenever the check fails, the operation answers with an empty body instead of an error. An
empty answer is therefore not proof that encryption is off, only that the settings cannot be read in this
context. Nothing is written and the call is safe to repeat. Use `GET api/2.0/settings/encryption/progress` to
follow a run that is in flight, and `POST api/2.0/settings/encryption/start` to encrypt or decrypt the
storage.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**EncryptionSettingsWrapper**](EncryptionSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.encryption_settings_wrapper import EncryptionSettingsWrapper
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
    api_instance = docspace_api_sdk.EncryptionApi(api_client)

    try:
        # Get the storage encryption settings
        api_response = api_instance.get_storage_encryption_settings()
        print("The response of EncryptionApi->get_storage_encryption_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->get_storage_encryption_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The encryption status and the notify-users flag, with the password blanked out; empty where encryption settings cannot be read |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit portal settings |  -  |
**405** | Storage encryption is not available on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_storage_encryption**
> BooleanWrapper start_storage_encryption(storage_encryption_requests_dto=storage_encryption_requests_dto)

Queues encryption of everything the installation keeps in its local storage, or decryption of it when the data
is already encrypted: the saved encryption state decides the direction, so the same call encrypts a decrypted
installation and decrypts an encrypted one. It covers the whole server, not one portal, and only a server
installation with the feature switched on can run it, with neither the portal storage nor the CDN pointing at
a third-party provider: reset those first with `DELETE api/2.0/settings/storage` and
`DELETE api/2.0/settings/storage/cdn`. No backup may be running, and the backup schedules of all portals are
dropped as part of starting. The caller needs the permission to edit portal settings, that is the portal owner
or a DocSpace admin, and an unrestricted access space. This is a long, disruptive operation: every portal is
put into the encryption state and stays unavailable until it ends, so do not repeat the call while it runs,
and follow it with `GET api/2.0/settings/encryption/progress` instead. The password is generated on the server
and never returned by the API. Pass `notifyUsers=true` to mail every user before the portals go down. The
response is true once the job is queued, and false where encryption is switched off, nothing being started
then.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_encryption_requests_dto** | [**StorageEncryptionRequestsDto**](StorageEncryptionRequestsDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.storage_encryption_requests_dto import StorageEncryptionRequestsDto
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
    api_instance = docspace_api_sdk.EncryptionApi(api_client)
    storage_encryption_requests_dto = docspace_api_sdk.StorageEncryptionRequestsDto() # StorageEncryptionRequestsDto |  (optional)

    try:
        # Start the storage encryption
        api_response = api_instance.start_storage_encryption(storage_encryption_requests_dto=storage_encryption_requests_dto)
        print("The response of EncryptionApi->start_storage_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EncryptionApi->start_storage_encryption: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | True when the encryption job has been queued; false in a build where storage encryption is switched off |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**402** | The portal pricing plan does not include storage encryption |  -  |
**403** | The caller may not edit portal settings, or this installation does not allow storage encryption |  -  |
**405** | Storage encryption is not available on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

