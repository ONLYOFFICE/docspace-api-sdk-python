# docspace_api_sdk.StorageApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_backup_storages**](#get_all_backup_storages) | **GET** /api/2.0/settings/storage/backup | Get the backup storages
[**get_all_cdn_storages**](#get_all_cdn_storages) | **GET** /api/2.0/settings/storage/cdn | Get the CDN storages
[**get_all_storages**](#get_all_storages) | **GET** /api/2.0/settings/storage | Get the portal storages
[**get_amazon_s3_regions**](#get_amazon_s3_regions) | **GET** /api/2.0/settings/storage/s3/regions | Get the Amazon S3 regions
[**get_storage_progress**](#get_storage_progress) | **GET** /api/2.0/settings/storage/progress | Get the storage migration progress
[**reset_cdn_to_default**](#reset_cdn_to_default) | **DELETE** /api/2.0/settings/storage/cdn | Reset the CDN storage settings
[**reset_storage_to_default**](#reset_storage_to_default) | **DELETE** /api/2.0/settings/storage | Reset the storage settings
[**update_cdn_storage**](#update_cdn_storage) | **PUT** /api/2.0/settings/storage/cdn | Update the CDN storage
[**update_storage**](#update_storage) | **PUT** /api/2.0/settings/storage | Switch the portal storage


# **get_all_backup_storages**
> StorageArrayWrapper get_all_backup_storages(dump=dump)

Returns the storages that can hold portal backups, with the one the saved backup schedule writes to marked as
`current` and its parameters filled in from that schedule; when no schedule is saved, or when the schedule
stores backups somewhere else than a third-party provider, none of the entries is current. Each entry has the
same shape as in `GET api/2.0/settings/storage`: identifier, title, the authentication keys the provider
expects, and `isSet` telling whether those keys are filled in on the server. Pass `dump=true` to read the
schedule of the whole server instead of the one of the current portal, which only makes sense on a server
installation. The caller needs the permission to edit portal settings, which in practice means the portal
owner or a DocSpace admin, and on an installation that is not a server one the call is also refused unless
backup is available there. Nothing is written and the call is safe to repeat. This operation says nothing
about where the portal data itself lives; the backup schedule is configured through the backup API, and the
storage of the documents through `PUT api/2.0/settings/storage`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dump** | **bool**| Whether the schedule of the whole server is read instead of the one of the current portal. It only changes  which schedule marks an entry as `current`; the list of storages itself is the same either way, and the flag  makes sense only on a self-hosted installation. | [optional] 

### Return type

[**StorageArrayWrapper**](StorageArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.storage_array_wrapper import StorageArrayWrapper
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
    api_instance = docspace_api_sdk.StorageApi(api_client)
    dump = true # bool | Whether the schedule of the whole server is read instead of the one of the current portal. It only changes  which schedule marks an entry as `current`; the list of storages itself is the same either way, and the flag  makes sense only on a self-hosted installation. (optional)

    try:
        # Get the backup storages
        api_response = api_instance.get_all_backup_storages(dump=dump)
        print("The response of StorageApi->get_all_backup_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_all_backup_storages: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storages that can hold portal backups, with the scheduled one marked as current |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit portal settings, or backup is not available on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_cdn_storages**
> StorageArrayWrapper get_all_cdn_storages()

Returns the storages that can serve the static content of the portal through a content delivery network, which
is the subset of the providers of `GET api/2.0/settings/storage` that offer a CDN of their own. The entries
have the same shape as in the storage listing: identifier and title, the authentication keys the provider
expects, `isSet` telling whether those keys are filled in on the server, and `current` marking the CDN the
portal uses now. Keys of the current entry come from the saved CDN settings and keys of the others from the
provider configuration. An empty list means the build ships no CDN-capable provider, and a list where nothing
is current means the portal serves its static content itself. The caller needs the permission to edit portal
settings, which in practice means the portal owner or a DocSpace admin, on a server installation with an
unrestricted access space. Nothing is written and the call is safe to repeat. Use
`PUT api/2.0/settings/storage/cdn` to select a CDN and `DELETE api/2.0/settings/storage/cdn` to stop using
one.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StorageArrayWrapper**](StorageArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.storage_array_wrapper import StorageArrayWrapper
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
    api_instance = docspace_api_sdk.StorageApi(api_client)

    try:
        # Get the CDN storages
        api_response = api_instance.get_all_cdn_storages()
        print("The response of StorageApi->get_all_cdn_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_all_cdn_storages: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storages that can serve as the portal CDN, with the one in use marked as current |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit portal settings, or this installation does not allow changing the storage |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_storages**
> StorageArrayWrapper get_all_storages()

Returns the third-party storages the installation can keep portal data in, the providers the build ships with,
such as Amazon S3, Google Cloud Storage or Rackspace. The built-in local storage is not among them: when none
of the entries is `current`, the portal data sits in the local storage. Each entry carries the storage
identifier and title, the authentication keys the provider expects, `isSet` telling whether those keys are
already filled in on the server, and `current` marking the one the portal uses right now. Keys of the current
storage are read from the saved settings, keys of the others from the provider configuration, so a value that
was never configured comes back empty. The caller needs the permission to edit portal settings, which in
practice means the portal owner or a DocSpace admin, and the installation has to be a server one whose access
space is not restricted; otherwise the call is refused with 403. Nothing is written and the call is safe to
repeat. Use `PUT api/2.0/settings/storage` to switch the storage, `DELETE api/2.0/settings/storage` to go back
to the local one, and `GET api/2.0/settings/storage/cdn` or `GET api/2.0/settings/storage/backup` for the CDN
and backup targets.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**StorageArrayWrapper**](StorageArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.storage_array_wrapper import StorageArrayWrapper
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
    api_instance = docspace_api_sdk.StorageApi(api_client)

    try:
        # Get the portal storages
        api_response = api_instance.get_all_storages()
        print("The response of StorageApi->get_all_storages:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_all_storages: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storages available to the portal, each marked as configured and as currently in use |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit portal settings, or this installation does not allow changing the storage |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_amazon_s3_regions**
> AmazonS3RegionArrayWrapper get_amazon_s3_regions()

Returns the Amazon regions the server knows about, each with its system name such as `eu-central-1`, the
display name to show a user, and the partition details the region belongs to: partition name, DNS suffix, the
pattern its region names match and the template its host names are built from. This is static reference data
compiled into the server rather than portal configuration: nothing is read from the settings, nothing is
written, the answer is the same for every portal and changes only when the server is updated, so it can be
cached by the caller. Use the system name of an entry as the region value in `props` when configuring an
Amazon S3 storage with `PUT api/2.0/settings/storage`, `PUT api/2.0/settings/storage/cdn` or a backup
schedule, and prefer picking a value from here over typing one, because a region the server does not know
cannot be reached. Any authenticated caller may read the list, no portal-settings permission is asked for, and
the result is neither paginated nor filtered.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AmazonS3RegionArrayWrapper**](AmazonS3RegionArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.amazon_s3_region_array_wrapper import AmazonS3RegionArrayWrapper
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
    api_instance = docspace_api_sdk.StorageApi(api_client)

    try:
        # Get the Amazon S3 regions
        api_response = api_instance.get_amazon_s3_regions()
        print("The response of StorageApi->get_amazon_s3_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_amazon_s3_regions: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The Amazon regions known to this installation |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_storage_progress**
> DoubleWrapper get_storage_progress()

Returns how far the current portal has got in moving its data to another storage, as a percentage from 0 to
100. The migration itself is started by `PUT api/2.0/settings/storage` or `DELETE api/2.0/settings/storage`,
which put the portal into the migrating state; poll this operation until the value reaches 100, then the
portal is served from the new storage. A value of -1 means storage migration is not offered on this
installation, which is the case for every portal that is not a server one. Ask for the progress only once a
migration has actually been started: for a portal whose migration the server does not remember, the call fails
instead of answering with a zero. The response carries the percentage only, without the error flag the
migration service reports internally, so a value that stops advancing is a reason to check the portal state
with `GET api/2.0/portal` rather than proof of progress. The caller needs the permission to edit portal
settings, which in practice means the portal owner or a DocSpace admin, and the call is accepted even when the
portal payment has lapsed. Nothing is written and the call is safe to repeat.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DoubleWrapper**](DoubleWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.double_wrapper import DoubleWrapper
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
    api_instance = docspace_api_sdk.StorageApi(api_client)

    try:
        # Get the storage migration progress
        api_response = api_instance.get_storage_progress()
        print("The response of StorageApi->get_storage_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->get_storage_progress: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Migration progress as a percentage, or -1 where storage migration is not offered |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_cdn_to_default**
> reset_cdn_to_default()

Drops the CDN configuration of the current portal, module and saved credentials alike, so that the static
content is served by the portal itself again. Nothing is uploaded or migrated, no state change is queued and
the call gives back no body: only the settings are cleared, and files already copied to the content delivery
network are left where they are, to be removed in the provider's own console if that is wanted. The change
takes effect for links built after it, so a page that is already open may keep pointing at the CDN until it is
reloaded. Repeating the call is harmless, because clearing an empty configuration does nothing. The caller
needs the permission to edit portal settings, which in practice means the portal owner or a DocSpace admin, on
a server installation with an unrestricted access space. Use `GET api/2.0/settings/storage/cdn` to see what is
configured now and `PUT api/2.0/settings/storage/cdn` to select a CDN again; the portal storage of the
documents is untouched by this operation and is reset with `DELETE api/2.0/settings/storage` instead.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.StorageApi(api_client)

    try:
        # Reset the CDN storage settings
        api_instance.reset_cdn_to_default()
    except Exception as e:
        print("Exception when calling StorageApi->reset_cdn_to_default: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The CDN configuration has been cleared and static content is served by the portal again |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit portal settings, or this installation does not allow changing the storage |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_storage_to_default**
> reset_storage_to_default()

Drops the third-party storage configuration of the current portal, module and saved credentials alike, and
starts an asynchronous migration of the portal data back into the built-in local storage. The portal moves
into the migrating state and stays unavailable until the transfer ends, so follow it with
`GET api/2.0/settings/storage/progress`; the call itself returns as soon as the migration has been handed to
the storage service and gives back no body. The caller needs the permission to edit portal settings, which in
practice means the portal owner or a DocSpace admin, on a server installation with an unrestricted access
space. This is a mutating and slow operation rather than a destructive one: documents are copied back rather
than deleted, but the credentials of the previous storage are gone from the settings and have to be sent again
with `PUT api/2.0/settings/storage` to switch back. Repeating the call while a migration is running starts
another one, so poll instead. Resetting the storage is also the step that makes
`POST api/2.0/settings/encryption/start` possible, since encryption only covers the local storage.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

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
    api_instance = docspace_api_sdk.StorageApi(api_client)

    try:
        # Reset the storage settings
        api_instance.reset_storage_to_default()
    except Exception as e:
        print("Exception when calling StorageApi->reset_storage_to_default: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The storage configuration has been cleared and migration back to the local storage has started |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit portal settings, or this installation does not allow changing the storage |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_cdn_storage**
> CdnStorageSettingsWrapper update_cdn_storage(storage_requests_dto=storage_requests_dto)

Selects the content delivery network that serves the static content of the portal and saves the credentials it
needs: `module` is the identifier of one of the entries of `GET api/2.0/settings/storage/cdn`, and `props`
carries that provider's authentication keys as name and value pairs. The provider has to be available on the
server, which the `isSet` flag of the listing tells, otherwise the request is rejected as invalid. Sending the
module the portal already uses changes nothing and returns the saved settings as they are. Any other module is
saved and the upload of the static content is handed to the storage service; the settings come back only when
that hand-over succeeds, a failure being reported as a server error. Unlike the portal storage this has no
progress operation, so there is nothing to poll: the content appears on the CDN once the service has copied
it. Only static content is affected here, never documents; for those use `PUT api/2.0/settings/storage`. The
caller needs the permission to edit portal settings, which in practice means the portal owner or a DocSpace
admin, on a server installation with an unrestricted access space. The response is the stored CDN
configuration.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_requests_dto** | [**StorageRequestsDto**](StorageRequestsDto.md)|  | [optional] 

### Return type

[**CdnStorageSettingsWrapper**](CdnStorageSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.cdn_storage_settings_wrapper import CdnStorageSettingsWrapper
from docspace_api_sdk.models.storage_requests_dto import StorageRequestsDto
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
    api_instance = docspace_api_sdk.StorageApi(api_client)
    storage_requests_dto = docspace_api_sdk.StorageRequestsDto() # StorageRequestsDto |  (optional)

    try:
        # Update the CDN storage
        api_response = api_instance.update_cdn_storage(storage_requests_dto=storage_requests_dto)
        print("The response of StorageApi->update_cdn_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->update_cdn_storage: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The saved CDN configuration; the upload of the static content has been handed to the storage service |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The requested CDN module is not configured on this installation |  -  |
**403** | The caller may not edit portal settings, or this installation does not allow changing the storage |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_storage**
> StorageSettingsWrapper update_storage(storage_requests_dto=storage_requests_dto)

Points the current portal at another storage and saves the credentials it needs: `module` is the identifier of
one of the storages listed by `GET api/2.0/settings/storage`, and `props` carries that provider's
authentication keys as name and value pairs, for example the bucket, region and access key of an Amazon S3
storage. The provider has to be available on the server, which the `isSet` flag of the listing tells,
otherwise the request is rejected as invalid. Sending the module the portal already uses changes nothing and
returns the saved settings as they are. Any other module starts an asynchronous migration of the portal data:
the portal moves into the migrating state and stays unavailable until the transfer ends, so follow it with
`GET api/2.0/settings/storage/progress` and do not send a second switch while it runs. The caller needs the
permission to edit portal settings, which in practice means the portal owner or a DocSpace admin, on a server
installation with an unrestricted access space. The response is the stored configuration, module and
properties, not the state of the migration. To return to the built-in local storage call
`DELETE api/2.0/settings/storage`, and for the CDN use `PUT api/2.0/settings/storage/cdn`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_requests_dto** | [**StorageRequestsDto**](StorageRequestsDto.md)|  | [optional] 

### Return type

[**StorageSettingsWrapper**](StorageSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.storage_requests_dto import StorageRequestsDto
from docspace_api_sdk.models.storage_settings_wrapper import StorageSettingsWrapper
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
    api_instance = docspace_api_sdk.StorageApi(api_client)
    storage_requests_dto = docspace_api_sdk.StorageRequestsDto() # StorageRequestsDto |  (optional)

    try:
        # Switch the portal storage
        api_response = api_instance.update_storage(storage_requests_dto=storage_requests_dto)
        print("The response of StorageApi->update_storage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StorageApi->update_storage: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The saved storage configuration; migration of the portal data to it has been started |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The requested storage module is not configured on this installation |  -  |
**403** | The caller may not edit portal settings, or this installation does not allow changing the storage |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

