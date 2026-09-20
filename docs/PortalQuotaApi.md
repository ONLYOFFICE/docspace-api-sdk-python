# docspace_api_sdk.QuotaApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_portal_quota**](#get_portal_quota) | **GET** /api/2.0/portal/quota | Get the portal quota
[**get_portal_tariff**](#get_portal_tariff) | **GET** /api/2.0/portal/tariff | Get the portal tariff
[**get_portal_used_space**](#get_portal_used_space) | **GET** /api/2.0/portal/usedspace | Get the portal used space
[**get_right_quota**](#get_right_quota) | **GET** /api/2.0/portal/quota/right | Get the recommended quota
[**get_upcoming_payments**](#get_upcoming_payments) | **GET** /api/2.0/portal/tariff/upcoming | Get upcoming payments


# **get_portal_quota**
> TenantQuotaWrapper get_portal_quota()

Returns the quota this portal runs on - the allowance its tariff grants: how many users and paid users it may
have, how many rooms, the largest total and single-file size, the price of the quota and the feature flags
that go with it. The caller needs the portal-settings right and gets 403 without it; the call is read-only and
idempotent. Sizes are in bytes, and `maxTotalSize` comes back as `0` when the calling account's own role is
user, rather than as the real allowance. This is what the portal is allowed, not what it consumes: the
consumption is reported by `GET api/2.0/portal/usedspace` in gigabytes and by `GET api/2.0/portal/userscount`.
The quotas the portal could move to are listed by `GET api/2.0/portal/payment/quotas`, and
`GET api/2.0/portal/quota/right` picks the smallest of them that would still fit. A free or trial quota
carries no price, and the billing state that goes with the quota - paid, in grace period or not paid - is read
from `GET api/2.0/portal/tariff`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantQuotaWrapper**](TenantQuotaWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_quota_wrapper import TenantQuotaWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)

    try:
        # Get the portal quota
        api_response = api_instance.get_portal_quota()
        print("The response of QuotaApi->get_portal_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_portal_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The allowance the current tariff grants this portal, with sizes in bytes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller has no portal-settings right |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_tariff**
> TariffWrapper get_portal_tariff(refresh=refresh)

Returns the tariff this portal runs on: its state, the end of the current period and the quotas - the plan and
its add-ons - it is made of. Nothing has to be called first, the call is read-only and idempotent, and it
keeps answering while the portal's payment has lapsed, which is what a client needs in order to show a payment
warning. How much of it is filled depends on the caller: every user gets `state`, which is `Trial`, `Paid`,
`Delay` for the grace period after the due date, or `NotPaid`; a room or DocSpace administrator also gets
`dueDate` and `delayDueDate`; and a caller with the portal-settings right additionally gets `id`,
`customerId`, `licenseDate`, the `openSource`, `enterprise` and `developer` flags and `quotas`, each entry
naming the quota, its quantity, its own due date and the quota it switches to next period. Dates are in the
portal time zone. Pass `refresh=true` to re-read the tariff from the billing system instead of the portal
cache - it is slower, so use it after a payment, not on every page. What the next period will cost is listed
by `GET api/2.0/portal/tariff/upcoming`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Whether the tariff is re-read from the billing system instead of the portal cache. The remote read is slower,  so ask for it right after a payment and leave it off for ordinary page loads. | [optional] 

### Return type

[**TariffWrapper**](TariffWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tariff_wrapper import TariffWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    refresh = true # bool | Whether the tariff is re-read from the billing system instead of the portal cache. The remote read is slower,  so ask for it right after a payment and leave it off for ordinary page loads. (optional)

    try:
        # Get the portal tariff
        api_response = api_instance.get_portal_tariff(refresh=refresh)
        print("The response of QuotaApi->get_portal_tariff:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_portal_tariff: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The tariff of this portal, filled as far as the rights of the caller allow |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_used_space**
> DoubleWrapper get_portal_used_space()

Returns how much space the content of this portal occupies, in gigabytes rounded to two decimals, so a client
can show the storage bar next to the allowance. The caller needs the portal-settings right and is refused
without it; the call is read-only and idempotent. The number is added up from the storage counters the portal
keeps per owner, which means content that belongs to no account - system data - is not part of it, and it is a
plain number, not an object. The counters are maintained as files are written and removed, so the value is
current but may lag a large operation that is still running. The allowance to compare it with is
`maxTotalSize` from `GET api/2.0/portal/quota`, in bytes rather than gigabytes, and the smallest quota that
would still fit the portal is suggested by `GET api/2.0/portal/quota/right`. This operation says nothing about
which room or user the space belongs to - the per-user figures come from the People API.

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
    api_instance = docspace_api_sdk.QuotaApi(api_client)

    try:
        # Get the portal used space
        api_response = api_instance.get_portal_used_space()
        print("The response of QuotaApi->get_portal_used_space:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_portal_used_space: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The space the portal content occupies, in gigabytes rounded to two decimals |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_right_quota**
> TenantQuotaWrapper get_right_quota()

Recommends the cheapest quota this portal could run on and still fit: the lowest-priced quota that is not
billed yearly, whose user allowance is above the number of active accounts and whose storage allowance is
above the space already used. The caller needs the portal-settings right and gets 403 without it. The call is
read-only, idempotent and buys nothing - it only picks one quota out of those the portal may switch to,
comparing them with the figures that `GET api/2.0/portal/userscount` and `GET api/2.0/portal/usedspace`
report. The answer is a single quota in the same shape as `GET api/2.0/portal/quota`, with sizes in bytes;
when no quota is large enough the answer is an empty body with 200 and not an error, so handle the empty
result as nothing to recommend. Yearly quotas are left out by design, so the recommendation is always a
monthly one - the full list to choose from comes from `GET api/2.0/portal/payment/quotas`, and the purchase
itself is started with `PUT api/2.0/portal/payment/url`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantQuotaWrapper**](TenantQuotaWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_quota_wrapper import TenantQuotaWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)

    try:
        # Get the recommended quota
        api_response = api_instance.get_right_quota()
        print("The response of QuotaApi->get_right_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_right_quota: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The cheapest monthly quota that would still fit this portal, or an empty body when none does |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller has no portal-settings right |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_upcoming_payments**
> UpcomingPaymentArrayWrapper get_upcoming_payments(refresh=refresh)

Lists what this portal will be charged next for the quotas of its current tariff - one entry per quota that is
going to be billed, with the amount, the currency and the due date. The caller needs the portal-settings right
and gets 403 without it; the call is read-only and idempotent and keeps answering while the portal's payment
has lapsed. Only quotas that are really charged appear: an overdue quota is skipped, and so is a quota that
has no price of its own, such as a trial or a free plan - which is why the list can come back empty on a
portal that does have a tariff. When a switch to another quota is scheduled for the next period, the entry
describes that next quota and its quantity, so `id` and `name` may differ from what
`GET api/2.0/portal/tariff` reports for today. `amount` is the unit price multiplied by `quantity`, in the
currency named by `currency` as an ISO 4217 code, `dueDate` is in the portal time zone, and `wallet` marks a
service paid from the portal wallet instead of the subscription.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Whether the tariff is re-read from the billing system instead of the portal cache. The remote read is slower,  so ask for it right after a payment and leave it off for ordinary page loads. | [optional] 

### Return type

[**UpcomingPaymentArrayWrapper**](UpcomingPaymentArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.upcoming_payment_array_wrapper import UpcomingPaymentArrayWrapper
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
    api_instance = docspace_api_sdk.QuotaApi(api_client)
    refresh = true # bool | Whether the tariff is re-read from the billing system instead of the portal cache. The remote read is slower,  so ask for it right after a payment and leave it off for ordinary page loads. (optional)

    try:
        # Get upcoming payments
        api_response = api_instance.get_upcoming_payments(refresh=refresh)
        print("The response of QuotaApi->get_upcoming_payments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling QuotaApi->get_upcoming_payments: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The charges the portal is going to be billed next, one entry per quota, empty when nothing is due |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller has no portal-settings right |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

