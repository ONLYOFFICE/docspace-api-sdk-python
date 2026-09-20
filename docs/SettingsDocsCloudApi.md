# docspace_api_sdk.DocsCloudApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_dev_pack**](#calculate_dev_pack) | **POST** /api/2.0/settings/docscloud/calculatedevpack | Calculate the DocsCloudDevPack switch cost
[**create_tenant_quota_report**](#create_tenant_quota_report) | **POST** /api/2.0/settings/docscloud/tenant/quota/report | Start the DocsCloud quota report
[**get_tenant**](#get_tenant) | **GET** /api/2.0/settings/docscloud/tenant | Get the DocsCloud tenant
[**get_tenant_config**](#get_tenant_config) | **GET** /api/2.0/settings/docscloud/tenant/config | Get the DocsCloud tenant configuration
[**get_tenant_info**](#get_tenant_info) | **GET** /api/2.0/settings/docscloud/tenant/info | Get the DocsCloud tenant information
[**get_tenant_quota**](#get_tenant_quota) | **GET** /api/2.0/settings/docscloud/tenant/quota | Get the DocsCloud tenant quota
[**get_tenant_quota_report**](#get_tenant_quota_report) | **GET** /api/2.0/settings/docscloud/tenant/quota/report | Get the DocsCloud quota report status
[**get_tenant_usage**](#get_tenant_usage) | **GET** /api/2.0/settings/docscloud/tenant/usage | Get the DocsCloud tenant usage
[**start_docs_cloud_trial**](#start_docs_cloud_trial) | **POST** /api/2.0/settings/docscloud/trial | Start the DocsCloud trial
[**switch_to_dev_pack**](#switch_to_dev_pack) | **POST** /api/2.0/settings/docscloud/switchtodevpack | Switch DocsCloud to DocsCloudDevPack
[**terminate_tenant_quota_report**](#terminate_tenant_quota_report) | **DELETE** /api/2.0/settings/docscloud/tenant/quota/report | Terminate the DocsCloud quota report
[**update_tenant_config**](#update_tenant_config) | **PUT** /api/2.0/settings/docscloud/tenant/config | Update the DocsCloud tenant configuration


# **calculate_dev_pack**
> PaymentCalculationWrapper calculate_dev_pack(docs_cloud_dev_pack_request_dto=docs_cloud_dev_pack_request_dto)

Prices the upgrade of the paid DocsCloud subscription of the current portal to DocsCloudDevPack for
the requested number of users, without changing the subscription or charging anything. It applies the
same preconditions as the switch itself: the portal must hold an active DocsCloud subscription, must
not already hold a DocsCloudDevPack one, and its tariff must not be delayed or unpaid; the quotas and
the state of the current tariff are listed by `GET api/2.0/portal/tariff`. The caller must be a
DocSpace administrator of a portal registered with the billing service. The call is read-only and
idempotent, so it can be repeated for different quantities before any switch is made. It returns the
amount that switching would cost, the three-letter ISO 4217 currency of that amount, the quantity the
amount was calculated for, and the identifier of the billing operation; an empty result means the
billing service could not price the switch, which should then not be attempted. The switch itself is
performed by `POST api/2.0/settings/docscloud/switchtodevpack` with the same `quantity` and takes no
identifier from this response; to price a change in the number of users of a subscription the portal
already has, use `PUT api/2.0/portal/payment/calculatewallet` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docs_cloud_dev_pack_request_dto** | [**DocsCloudDevPackRequestDto**](DocsCloudDevPackRequestDto.md)|  | [optional] 

### Return type

[**PaymentCalculationWrapper**](PaymentCalculationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_dev_pack_request_dto import DocsCloudDevPackRequestDto
from docspace_api_sdk.models.payment_calculation_wrapper import PaymentCalculationWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    docs_cloud_dev_pack_request_dto = docspace_api_sdk.DocsCloudDevPackRequestDto() # DocsCloudDevPackRequestDto |  (optional)

    try:
        # Calculate the DocsCloudDevPack switch cost
        api_response = api_instance.calculate_dev_pack(docs_cloud_dev_pack_request_dto=docs_cloud_dev_pack_request_dto)
        print("The response of DocsCloudApi->calculate_dev_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->calculate_dev_pack: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cost of switching to DocsCloudDevPack for the requested quantity, or an empty result if the billing service could not price it |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The quantity is below the allowed minimum, the portal has no active DocsCloud subscription, or it already has a DocsCloudDevPack subscription |  -  |
**402** | The portal tariff is delayed or not paid, so the switch cannot be priced |  -  |
**403** | The caller is not a DocSpace administrator, or the billing service is not configured |  -  |
**404** | The portal is not registered as a billing customer, or the DocsCloud and DocsCloudDevPack wallet products are not configured on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_tenant_quota_report**
> DocumentBuilderTaskWrapper create_tenant_quota_report()

Queues a background job that renders the current DocsCloud user quota of the portal into an xlsx file and
saves that file in the My documents folder of the calling user; the report lists the editor and the viewer
users with the type and the expiration date of each, and summarizes the internal, external and remaining users
against the license limits. The file is not ready when the response arrives: poll
`GET api/2.0/settings/docscloud/tenant/quota/report` until `isCompleted` is true, then take the file from
`resultFileId` or `resultFileUrl`, and use `DELETE api/2.0/settings/docscloud/tenant/quota/report` to cancel a
job that is still running. The caller must be a portal administrator allowed to edit the portal settings. The
portal should have an activated DocsCloud tenant: this call does not check that, and without a tenant the job
itself fails and reports the reason in the `error` of the status response. One report per caller runs at a
time: while a report of this user is still being built, the call describes that running job and no second
generation is started, so a repeated call is safe. What comes back is the initial state of the job, with
`percentage` 0 and a created `status`, not the report; the report is a point-in-time snapshot and carries the
generation date in its file name. To read the same data as JSON, without building a file, use
`GET api/2.0/settings/docscloud/tenant/quota`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)

    try:
        # Start the DocsCloud quota report
        api_response = api_instance.create_tenant_quota_report()
        print("The response of DocsCloudApi->create_tenant_quota_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->create_tenant_quota_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The initial state of the queued report generation job, with zero progress and an uncompleted status |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant**
> DocsCloudTenantWrapper get_tenant(refresh=refresh)

Returns the DocsCloud tenant of the current portal: the DocsCloud server assigned to the portal, with its
address, the date the tenant subscription ends and the payment the tenant was created for. A tenant exists
only after a DocsCloud subscription has been granted, by `POST api/2.0/settings/docscloud/trial` or by a
DocsCloud purchase, and only on an installation where the DocsCloud service is configured. The caller must
be a portal administrator allowed to edit the portal settings. The call is read-only and idempotent, and it
is served from a cache that keeps the tenant for an hour and the absence of a tenant for a minute, so pass
`refresh=true` right after a subscription change to read the current state from DocsCloud instead. In the
result, `address` is the absolute URL of the assigned server, `isActive` tells whether `endDate` is still in
the future, and the dates are in UTC. An empty result means the portal has no DocsCloud tenant yet, which is
the normal state before a subscription and not an error, so this is the operation to call to find out whether
DocsCloud is activated at all. The license and server details, the editing settings, the user quota and the
usage statistics are not part of it: they live in `GET api/2.0/settings/docscloud/tenant/info`,
`.../tenant/config`, `.../tenant/quota` and `.../tenant/usage`, each of which fails with 400 while the
portal has no activated tenant.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Pass `true` to skip the cached copy and request the tenant from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to an hour old, or up to a minute old while the portal has no tenant. | [optional] [default to False]

### Return type

[**DocsCloudTenantWrapper**](DocsCloudTenantWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_tenant_wrapper import DocsCloudTenantWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    refresh = False # bool | Pass `true` to skip the cached copy and request the tenant from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to an hour old, or up to a minute old while the portal has no tenant. (optional) (default to False)

    try:
        # Get the DocsCloud tenant
        api_response = api_instance.get_tenant(refresh=refresh)
        print("The response of DocsCloudApi->get_tenant:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->get_tenant: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DocsCloud tenant of the portal, or an empty result if no DocsCloud tenant is assigned to it |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_config**
> DocsCloudConfigWrapper get_tenant_config(refresh=refresh)

Returns the configuration of the DocsCloud tenant of the current portal: its name, the security secret and
header name, the file size limit and anonymous access switch of the server, the WOPI switch and the IP filter
rules. The portal must have an activated DocsCloud tenant, granted by `POST api/2.0/settings/docscloud/trial`
or by a DocsCloud purchase: an empty result from `GET api/2.0/settings/docscloud/tenant` means there is none
and this call fails with 400. The caller must be a portal administrator allowed to edit the portal settings,
on an installation where the DocsCloud service is configured. The call is read-only, idempotent and cached for
an hour, so pass `refresh=true` to read the current state from DocsCloud; the same values are changed by
`PUT api/2.0/settings/docscloud/tenant/config`, which drops the cached copy itself, so no refresh is needed
after an update. In the result, `security.secret` is a credential, so the response should be treated as
sensitive; `server.fileSizeLimit` is in bytes and an update cannot raise it above 209715200 (200 MB); and an
empty or absent `ipFilter.rules` means no address restriction is configured. The license and server version,
the address of the assigned server, the per-user quota and the usage counters are not part of it: they live in
`.../tenant/info`, `.../tenant`, `.../tenant/quota` and `.../tenant/usage`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Pass `true` to skip the cached copy and request the configuration from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to an hour old. | [optional] [default to False]

### Return type

[**DocsCloudConfigWrapper**](DocsCloudConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_config_wrapper import DocsCloudConfigWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    refresh = False # bool | Pass `true` to skip the cached copy and request the configuration from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to an hour old. (optional) (default to False)

    try:
        # Get the DocsCloud tenant configuration
        api_response = api_instance.get_tenant_config(refresh=refresh)
        print("The response of DocsCloudApi->get_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->get_tenant_config: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration of the DocsCloud tenant of the portal, with its security, server, WOPI and IP filter settings |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The portal has no activated DocsCloud tenant, so there is no configuration to return |  -  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_info**
> DocsCloudTenantInfoWrapper get_tenant_info(refresh=refresh)

Returns the DocsCloud license of the current portal, the DocsCloud server serving it, the user limits of
that license and the editor and viewer usage counted against them for the current period. The portal must
have an activated DocsCloud tenant, granted by `POST api/2.0/settings/docscloud/trial` or by a DocsCloud
purchase: an empty result from `GET api/2.0/settings/docscloud/tenant` means there is none and this call
fails with 400. The caller must be a portal administrator allowed to edit the portal settings, on an
installation where the DocsCloud service is configured. The call is read-only, idempotent and cached for a
minute, so pass `refresh=true` right after a subscription change to read the current state from DocsCloud.
In the result, `license.valid` is when the license expires and `license.trial` is reported as `false` once
the portal holds a paid DocsCloud or DocsCloudDevPack subscription, even when the license itself still says
trial; `usersLimit` caps the editors and the viewers allowed, `stats` counts the active, internal, external
and remaining users of each of those two kinds over the last `stats.periodDay` days, and the dates are in
UTC. The editing settings, the per-user quota lists and the address of the assigned server live in
`.../tenant/config`, `.../tenant/quota` and `.../tenant`, while `.../tenant/usage` gives one active-user
total instead of this per-role breakdown.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Pass `true` to skip the cached copy and request the license, server and usage information from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to a minute old. | [optional] [default to False]

### Return type

[**DocsCloudTenantInfoWrapper**](DocsCloudTenantInfoWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_tenant_info_wrapper import DocsCloudTenantInfoWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    refresh = False # bool | Pass `true` to skip the cached copy and request the license, server and usage information from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to a minute old. (optional) (default to False)

    try:
        # Get the DocsCloud tenant information
        api_response = api_instance.get_tenant_info(refresh=refresh)
        print("The response of DocsCloudApi->get_tenant_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->get_tenant_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The DocsCloud license and server information of the portal, with the user limits of the license and the usage statistics for the current period |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The portal has no activated DocsCloud tenant, so there is no license information to return |  -  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_quota**
> DocsCloudQuotaWrapper get_tenant_quota(refresh=refresh)

Returns the DocsCloud user quota of the current portal: the users who currently count as DocsCloud editors and
the users who count as viewers, each with the identifier DocsCloud knows them by and the date their quota entry
expires. The portal must have an activated DocsCloud tenant, granted by `POST api/2.0/settings/docscloud/trial`
or by a DocsCloud purchase: an empty result from `GET api/2.0/settings/docscloud/tenant` means there is none
and this call fails with 400. The caller must be a portal administrator allowed to edit the portal settings,
on an installation where the DocsCloud service is configured. The call is read-only, idempotent and cached for
a minute, so pass `refresh=true` to read the current state from DocsCloud. In the result, `users` holds the
editor entries and `usersView` the viewer entries, both unordered; `userId` is the DocSpace user ID for a
portal member and an identifier of DocsCloud's own for anyone else; `expire` is the date and time the entry
expires, as a UTC string; and empty lists mean no user has been counted yet. It lists the users themselves,
not the counters: the license limits with the per-role totals are in
`GET api/2.0/settings/docscloud/tenant/info`, a single active-user total is in `.../tenant/usage`, and the
same lists as a downloadable xlsx file are produced by
`POST api/2.0/settings/docscloud/tenant/quota/report`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Pass `true` to skip the cached copy and request the user quota from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to a minute old. | [optional] [default to False]

### Return type

[**DocsCloudQuotaWrapper**](DocsCloudQuotaWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_quota_wrapper import DocsCloudQuotaWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    refresh = False # bool | Pass `true` to skip the cached copy and request the user quota from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to a minute old. (optional) (default to False)

    try:
        # Get the DocsCloud tenant quota
        api_response = api_instance.get_tenant_quota(refresh=refresh)
        print("The response of DocsCloudApi->get_tenant_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->get_tenant_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The editor and viewer users of the DocsCloud tenant of the portal, with the expiration date of each entry |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The portal has no activated DocsCloud tenant, so there is no user quota to return |  -  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_quota_report**
> DocumentBuilderTaskWrapper get_tenant_quota_report()

Returns the state of the DocsCloud user quota report that the current user started with
`POST api/2.0/settings/docscloud/tenant/quota/report`, so that the caller can follow the generation and pick
up the resulting file. It reports the caller's own job only: a report started by another administrator is not
visible here, and an empty result means this user has no job, because none was started, because it was
terminated, or because a finished one has already been cleared (a job state is kept for a day, and starting a
new report drops the previous finished one); that is a normal state and not an error. The caller must be a
portal administrator allowed to edit the portal settings. The call is read-only and idempotent, and it is
meant to be polled while the job runs. In the result, `percentage` goes from 0 to 100 and `isCompleted`
becomes true both on success and on failure, so check `error`: it is empty when the report was built and
carries the failure message otherwise;
`resultFileId`, `resultFileName` and `resultFileUrl` are filled in only once the file exists, and that file
also stays in the My documents folder of the caller. Use the `POST` operation on this path to start a report
and the `DELETE` one to cancel it.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.document_builder_task_wrapper import DocumentBuilderTaskWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)

    try:
        # Get the DocsCloud quota report status
        api_response = api_instance.get_tenant_quota_report()
        print("The response of DocsCloudApi->get_tenant_quota_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->get_tenant_quota_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of the DocsCloud quota report job of the caller, or an empty result if there is no such job |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_usage**
> DocsCloudUsageWrapper get_tenant_usage(refresh=refresh)

Returns the DocsCloud usage of the current portal: the number of users who have been active in DocsCloud in
the current period, and the moment that period is counted from. The portal must have an activated DocsCloud
tenant, granted by `POST api/2.0/settings/docscloud/trial` or by a DocsCloud purchase: an empty result from
`GET api/2.0/settings/docscloud/tenant` means there is none and this call fails with 400. The caller must be a
portal administrator allowed to edit the portal settings, on an installation where the DocsCloud service is
configured. The call is read-only, idempotent and cached for a minute, so pass `refresh=true` to read the
current state from DocsCloud. In the result, `activeCount` counts the users seen since `since`, which is in
UTC, and it is one total for the whole tenant, with no split by role and no limit to compare it against. For
the editor and viewer breakdown with the license limits use `GET api/2.0/settings/docscloud/tenant/info`, and
for the users counted one by one `GET api/2.0/settings/docscloud/tenant/quota`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Pass `true` to skip the cached copy and request the usage statistics from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to a minute old. | [optional] [default to False]

### Return type

[**DocsCloudUsageWrapper**](DocsCloudUsageWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_usage_wrapper import DocsCloudUsageWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    refresh = False # bool | Pass `true` to skip the cached copy and request the usage statistics from DocsCloud again, replacing the cached one; with the default `false` the answer may be up to a minute old. (optional) (default to False)

    try:
        # Get the DocsCloud tenant usage
        api_response = api_instance.get_tenant_usage(refresh=refresh)
        print("The response of DocsCloudApi->get_tenant_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->get_tenant_usage: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The number of active DocsCloud users of the portal and the date the count starts from |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The portal has no activated DocsCloud tenant, so there is no usage information to return |  -  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_docs_cloud_trial**
> BooleanWrapper start_docs_cloud_trial()

Activates the free DocsCloud trial subscription for the current portal, and, once a DocsCloud server is
assigned to the portal, allows the address of that server in the Content Security Policy settings.
The portal tariff must be in the trial or paid state (not delayed and not unpaid), and the portal must not
already hold a DocsCloud trial, DocsCloud or DocsCloudDevPack subscription: the quotas of the current
tariff are listed by `GET api/2.0/portal/tariff`. The caller must be a portal administrator allowed to edit
the portal settings, on an installation where the billing service is configured. The operation changes the
portal subscription and is not idempotent: repeating it after a successful activation fails with 400.
It returns `true` when the trial has been granted, and `false` when the billing service declines it
(for example, when this portal has already used its trial), in which case nothing is changed. It never buys
a paid plan: an existing paid DocsCloud subscription is moved to DocsCloudDevPack by
`POST api/2.0/settings/docscloud/switchtodevpack` instead.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)

    try:
        # Start the DocsCloud trial
        api_response = api_instance.start_docs_cloud_trial()
        print("The response of DocsCloudApi->start_docs_cloud_trial:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->start_docs_cloud_trial: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the trial subscription is activated, false if the billing service declines it |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The portal already has a DocsCloud trial, DocsCloud or DocsCloudDevPack subscription |  -  |
**402** | The portal tariff is delayed or not paid, so the trial cannot be started |  -  |
**403** | The caller is not allowed to edit the portal settings, or the billing service is not configured |  -  |
**404** | The DocsCloud trial quota is not available on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **switch_to_dev_pack**
> BooleanWrapper switch_to_dev_pack(docs_cloud_dev_pack_request_dto=docs_cloud_dev_pack_request_dto)

Upgrades the paid DocsCloud subscription of the current portal to DocsCloudDevPack for the requested
number of users, charging the price difference to the portal wallet and moving the DocsCloud license
to the new product. The portal must hold an active DocsCloud subscription, must not already hold a
DocsCloudDevPack one, and its tariff must not be delayed or unpaid: the quotas and the state of the
current tariff are listed by `GET api/2.0/portal/tariff`, and the amount that will be charged is
returned by `POST api/2.0/settings/docscloud/calculatedevpack` for the same `quantity`. The caller
must be a DocSpace administrator of a portal registered with the billing service. The switch is
synchronous, mutating and not idempotent: repeating it after a successful call fails with 400, and
concurrent calls for one portal are serialized so that the wallet is charged only once. It returns
`true` when the subscription has been switched, and `false` when the billing service declines or
fails to perform the switch, in which case nothing is charged and the portal stays on DocsCloud.
Only the DocsCloud to DocsCloudDevPack direction is supported: to change the number of users of a
subscription the portal already has, or to schedule a reversion from DocsCloudDevPack back to
DocsCloud at the next billing period, use `PUT api/2.0/portal/payment/updatewallet` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docs_cloud_dev_pack_request_dto** | [**DocsCloudDevPackRequestDto**](DocsCloudDevPackRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.docs_cloud_dev_pack_request_dto import DocsCloudDevPackRequestDto
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    docs_cloud_dev_pack_request_dto = docspace_api_sdk.DocsCloudDevPackRequestDto() # DocsCloudDevPackRequestDto |  (optional)

    try:
        # Switch DocsCloud to DocsCloudDevPack
        api_response = api_instance.switch_to_dev_pack(docs_cloud_dev_pack_request_dto=docs_cloud_dev_pack_request_dto)
        print("The response of DocsCloudApi->switch_to_dev_pack:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->switch_to_dev_pack: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the subscription is switched to DocsCloudDevPack, false if the billing service declines it |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The quantity is below the allowed minimum, the portal has no active DocsCloud subscription, or it already has a DocsCloudDevPack subscription |  -  |
**402** | The portal tariff is delayed or not paid, so the subscription cannot be switched |  -  |
**403** | The caller is not a DocSpace administrator, or the billing service is not configured |  -  |
**404** | The portal is not registered as a billing customer, or the DocsCloud and DocsCloudDevPack wallet products are not configured on this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_tenant_quota_report**
> terminate_tenant_quota_report()

Cancels the DocsCloud user quota report that the current user started with
`POST api/2.0/settings/docscloud/tenant/quota/report` and removes its job, so that a new report can be started
right away. There is no precondition: the call is accepted even when this user has no report job at all, and
it affects the caller's own job only, never one started by another administrator. The caller must be a portal
administrator allowed to edit the portal settings. The cancellation is asynchronous and idempotent: 200 means
the request has been queued for the report worker, not that the job has already stopped, so poll
`GET api/2.0/settings/docscloud/tenant/quota/report` until it returns an empty result. Nothing is returned in
the body. A report file that has already been saved in the My documents folder of the caller is left there
and has to be deleted through the file operations if it is no longer wanted.

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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)

    try:
        # Terminate the DocsCloud quota report
        api_instance.terminate_tenant_quota_report()
    except Exception as e:
        print("Exception when calling DocsCloudApi->terminate_tenant_quota_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The termination request has been queued for the report worker; the response has no body |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_tenant_config**
> DocsCloudConfigWrapper update_tenant_config(docs_cloud_config=docs_cloud_config)

Replaces the configuration of the DocsCloud tenant of the current portal: its name, the security secret and
header name, the file size limit and anonymous access switch of the server, the WOPI switch and the IP filter
rules; it returns the configuration as DocsCloud stored it. The portal must have an activated DocsCloud tenant,
granted by `POST api/2.0/settings/docscloud/trial` or by a DocsCloud purchase: an empty result from
`GET api/2.0/settings/docscloud/tenant` means there is none and this call fails with 400. Read the current
values with `GET api/2.0/settings/docscloud/tenant/config` first and send back whole sections: the sections
left out of the request are not sent to DocsCloud at all, while a section that is present is sent with all of
its fields, so a field left unset inside it goes out as `0`, `false` or empty. The caller must be a portal
administrator allowed to edit the portal settings, on an installation where the DocsCloud service is
configured. The call is mutating,
synchronous and idempotent, it is recorded in the portal audit trail, and it drops the cached configuration
itself, so the next read returns the new values without `refresh=true`. The `tenantName`, `security.secret`,
`security.header` and every `ipFilter.rules` address are capped at 255 characters and `server.fileSizeLimit`
at 209715200 bytes (200 MB); a value outside those bounds is rejected with 400 before anything reaches
DocsCloud. It changes these settings only, never the subscription, the user quota or the license.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **docs_cloud_config** | [**DocsCloudConfig**](DocsCloudConfig.md)|  | [optional] 

### Return type

[**DocsCloudConfigWrapper**](DocsCloudConfigWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.docs_cloud_config import DocsCloudConfig
from docspace_api_sdk.models.docs_cloud_config_wrapper import DocsCloudConfigWrapper
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
    api_instance = docspace_api_sdk.DocsCloudApi(api_client)
    docs_cloud_config = docspace_api_sdk.DocsCloudConfig() # DocsCloudConfig |  (optional)

    try:
        # Update the DocsCloud tenant configuration
        api_response = api_instance.update_tenant_config(docs_cloud_config=docs_cloud_config)
        print("The response of DocsCloudApi->update_tenant_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocsCloudApi->update_tenant_config: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The configuration of the DocsCloud tenant as DocsCloud stored it after the update |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | A text field is longer than 255 characters, the file size limit is outside 0-209715200 bytes, or the portal has no activated DocsCloud tenant |  -  |
**403** | The caller is not allowed to edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

