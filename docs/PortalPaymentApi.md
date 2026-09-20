# docspace_api_sdk.PaymentApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate_wallet_payment**](#calculate_wallet_payment) | **PUT** /api/2.0/portal/payment/calculatewallet | Calculate the wallet payment amount
[**change_tenant_wallet_service_state**](#change_tenant_wallet_service_state) | **POST** /api/2.0/portal/payment/servicestate | Switch a wallet service
[**create_customer_monthly_usage_report**](#create_customer_monthly_usage_report) | **POST** /api/2.0/portal/payment/customer/usage/monthly/report | Start the monthly usage report
[**create_customer_operations_report**](#create_customer_operations_report) | **POST** /api/2.0/portal/payment/customer/operationsreport | Start the operations report
[**create_customer_service_usage_report**](#create_customer_service_usage_report) | **POST** /api/2.0/portal/payment/customer/usage/report | Start the service usage report
[**get_accounting_service_prices**](#get_accounting_service_prices) | **GET** /api/2.0/portal/payment/accounting/prices/{serviceName} | Get the service prices from the accounting service
[**get_active_services**](#get_active_services) | **GET** /api/2.0/portal/payment/activeservices | Get the active wallet services
[**get_ai_prices**](#get_ai_prices) | **GET** /api/2.0/portal/payment/ai-prices | Get AI model prices
[**get_checkout_setup_url**](#get_checkout_setup_url) | **GET** /api/2.0/portal/payment/checkoutsetupurl | Get the checkout setup page URL
[**get_customer_balance**](#get_customer_balance) | **GET** /api/2.0/portal/payment/customer/balance | Get the customer balance
[**get_customer_info**](#get_customer_info) | **GET** /api/2.0/portal/payment/customerinfo | Get the customer information
[**get_customer_monthly_usage**](#get_customer_monthly_usage) | **GET** /api/2.0/portal/payment/customer/usage/monthly | Get the customer monthly usage
[**get_customer_monthly_usage_report**](#get_customer_monthly_usage_report) | **GET** /api/2.0/portal/payment/customer/usage/monthly/report | Get the monthly usage report status
[**get_customer_operations**](#get_customer_operations) | **GET** /api/2.0/portal/payment/customer/operations | Get the wallet operations
[**get_customer_operations_report**](#get_customer_operations_report) | **GET** /api/2.0/portal/payment/customer/operationsreport | Get the operations report status
[**get_customer_service_usage**](#get_customer_service_usage) | **GET** /api/2.0/portal/payment/customer/usage | Get the customer service usage
[**get_customer_service_usage_report**](#get_customer_service_usage_report) | **GET** /api/2.0/portal/payment/customer/usage/report | Get the service usage report status
[**get_payment_account**](#get_payment_account) | **GET** /api/2.0/portal/payment/account | Get the billing account page
[**get_payment_currencies**](#get_payment_currencies) | **GET** /api/2.0/portal/payment/currencies | Get the billing currencies
[**get_payment_quotas**](#get_payment_quotas) | **GET** /api/2.0/portal/payment/quotas | Get the purchasable quotas
[**get_payment_url**](#get_payment_url) | **PUT** /api/2.0/portal/payment/url | Get the payment page URL
[**get_portal_prices**](#get_portal_prices) | **GET** /api/2.0/portal/payment/prices | Get the product prices
[**get_quota_payment_information**](#get_quota_payment_information) | **GET** /api/2.0/portal/payment/quota | Get the current plan and limits
[**get_restricted_ai_models**](#get_restricted_ai_models) | **GET** /api/2.0/portal/payment/ai-model/restrictions | Get restricted AI models
[**get_subscription_balance_info**](#get_subscription_balance_info) | **GET** /api/2.0/portal/payment/subscription/balance | Get the subscription balance information
[**get_tenant_wallet_service_settings**](#get_tenant_wallet_service_settings) | **GET** /api/2.0/portal/payment/servicessettings | Get the wallet service settings
[**get_tenant_wallet_settings**](#get_tenant_wallet_settings) | **GET** /api/2.0/portal/payment/topupsettings | Get the auto top-up settings
[**get_wallet_service**](#get_wallet_service) | **GET** /api/2.0/portal/payment/walletservice | Get a wallet service
[**get_wallet_services**](#get_wallet_services) | **GET** /api/2.0/portal/payment/walletservices | Get wallet services
[**move_subscription_to_wallet**](#move_subscription_to_wallet) | **POST** /api/2.0/portal/payment/subscription/movetowallet | Move the subscription to the wallet
[**send_payment_request**](#send_payment_request) | **POST** /api/2.0/portal/payment/request | Contact the sales team
[**set_restricted_ai_models**](#set_restricted_ai_models) | **PUT** /api/2.0/portal/payment/ai-model/restrictions | Set restricted AI models
[**set_tenant_wallet_settings**](#set_tenant_wallet_settings) | **POST** /api/2.0/portal/payment/topupsettings | Set the auto top-up settings
[**terminate_customer_monthly_usage_report**](#terminate_customer_monthly_usage_report) | **DELETE** /api/2.0/portal/payment/customer/usage/monthly/report | Terminate the monthly usage report
[**terminate_customer_operations_report**](#terminate_customer_operations_report) | **DELETE** /api/2.0/portal/payment/customer/operationsreport | Terminate the operations report
[**terminate_customer_service_usage_report**](#terminate_customer_service_usage_report) | **DELETE** /api/2.0/portal/payment/customer/usage/report | Terminate the service usage report
[**top_up_deposit**](#top_up_deposit) | **POST** /api/2.0/portal/payment/deposit | Top up the wallet
[**update_payment**](#update_payment) | **PUT** /api/2.0/portal/payment/update | Change the subscription quantity
[**update_wallet_payment**](#update_wallet_payment) | **PUT** /api/2.0/portal/payment/updatewallet | Change a wallet service quantity


# **calculate_wallet_payment**
> PaymentCalculationWrapper calculate_wallet_payment(wallet_quantity_request_dto=wallet_quantity_request_dto)

Prices a wallet-service purchase without making it: it returns what buying the requested number of units would
cost right now, so a client can show the amount before asking for a confirmation. Only `productQuantityType`
`Add` (1) is accepted, the quantity must be greater than zero, and the portal needs a billing customer whose
wallet has a sub-account in the accounting currency. The caller has to be a DocSpace administrator. Nothing is
bought, charged or written down - the call is read-only and may be repeated - and the purchase itself is
`PUT api/2.0/portal/payment/updatewallet`. The answer carries the amount with its currency, the quantity it
was computed for and the identifier of the calculation. It is the price of this moment and is not held: it can
differ by the time the purchase is made.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_quantity_request_dto** | [**WalletQuantityRequestDto**](WalletQuantityRequestDto.md)|  | [optional] 

### Return type

[**PaymentCalculationWrapper**](PaymentCalculationWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.payment_calculation_wrapper import PaymentCalculationWrapper
from docspace_api_sdk.models.wallet_quantity_request_dto import WalletQuantityRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    wallet_quantity_request_dto = docspace_api_sdk.WalletQuantityRequestDto() # WalletQuantityRequestDto |  (optional)

    try:
        # Calculate the wallet payment amount
        api_response = api_instance.calculate_wallet_payment(wallet_quantity_request_dto=wallet_quantity_request_dto)
        print("The response of PaymentApi->calculate_wallet_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->calculate_wallet_payment: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The amount the purchase would cost, its currency and the quantity it was calculated for |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The quantity type is not `Add`, the quantity is not greater than zero, or the product is not a wallet service |  -  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer, or its wallet has no sub-account in the accounting currency |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_tenant_wallet_service_state**
> TenantWalletServiceSettingsWrapper change_tenant_wallet_service_state(change_wallet_service_state_request_dto=change_wallet_service_state_request_dto)

Switches one wallet service on or off for the portal: `service` names it and `enabled` says which way. The
portal needs a billing customer, and the caller needs both the permission to edit the portal settings and
DocSpace administrator rights. Order matters between the two AI services - AI tools has to be on before AI
search may be switched on, and switching AI tools off switches AI search off with it - so a request that
breaks that order is refused with 403. The call is mutating and idempotent: switching on a service that is
already on changes nothing. It is written to the portal audit trail, and switching AI tools notifies the
portal clients so the AI features appear or disappear for them without a reload. The whole updated set of
switched-on services comes back. Switching a service on does not buy it - its units are still bought with
`PUT api/2.0/portal/payment/updatewallet`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_wallet_service_state_request_dto** | [**ChangeWalletServiceStateRequestDto**](ChangeWalletServiceStateRequestDto.md)|  | [optional] 

### Return type

[**TenantWalletServiceSettingsWrapper**](TenantWalletServiceSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.change_wallet_service_state_request_dto import ChangeWalletServiceStateRequestDto
from docspace_api_sdk.models.tenant_wallet_service_settings_wrapper import TenantWalletServiceSettingsWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    change_wallet_service_state_request_dto = docspace_api_sdk.ChangeWalletServiceStateRequestDto() # ChangeWalletServiceStateRequestDto |  (optional)

    try:
        # Switch a wallet service
        api_response = api_instance.change_tenant_wallet_service_state(change_wallet_service_state_request_dto=change_wallet_service_state_request_dto)
        print("The response of PaymentApi->change_tenant_wallet_service_state:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->change_tenant_wallet_service_state: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The whole set of wallet services switched on for the portal after the change |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings or is not a DocSpace administrator, the portal has no billing service configured, or AI search was switched on while AI tools is off |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_monthly_usage_report**
> DocumentBuilderTaskWrapper create_customer_monthly_usage_report(customer_monthly_usage_report_request_dto=customer_monthly_usage_report_request_dto)

Queues the wallet spending added up per calendar month as an `xlsx` file and returns the task that will build
it; the file is not ready when the response arrives. The portal needs a billing customer and the caller has to
be a DocSpace administrator. The body takes only the period - `startDate` and `endDate`, both inclusive - and
an empty body covers everything from the portal creation date to now; the months are cut in the portal time
zone, exactly as in `GET api/2.0/portal/payment/customer/usage/monthly`. Poll
`GET api/2.0/portal/payment/customer/usage/monthly/report` until `isCompleted` is true, then take the file
from `resultFileUrl` or open `resultFileId`: the finished file is saved into the caller's own My documents
section, where it counts against the portal storage like any other file. One monthly usage report per user is
tracked at a time - a call made while the previous one is still running answers with that task - and
`DELETE api/2.0/portal/payment/customer/usage/monthly/report` stops it. There is no service filter here: for a
report per service use `POST api/2.0/portal/payment/customer/usage/report`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_monthly_usage_report_request_dto** | [**CustomerMonthlyUsageReportRequestDto**](CustomerMonthlyUsageReportRequestDto.md)|  | [optional] 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.customer_monthly_usage_report_request_dto import CustomerMonthlyUsageReportRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    customer_monthly_usage_report_request_dto = docspace_api_sdk.CustomerMonthlyUsageReportRequestDto() # CustomerMonthlyUsageReportRequestDto |  (optional)

    try:
        # Start the monthly usage report
        api_response = api_instance.create_customer_monthly_usage_report(customer_monthly_usage_report_request_dto=customer_monthly_usage_report_request_dto)
        print("The response of PaymentApi->create_customer_monthly_usage_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_customer_monthly_usage_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queued task, to be polled until `isCompleted` is true |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_operations_report**
> DocumentBuilderTaskWrapper create_customer_operations_report(customer_operations_report_request_dto=customer_operations_report_request_dto)

Queues the history of the wallet movements as an `xlsx` file and returns the task that will build it; the file
is not ready when the response arrives. The portal needs a billing customer and the caller has to be a
DocSpace administrator. The body takes the same filters as `GET api/2.0/portal/payment/customer/operations` -
the service names, the date range, the participant, the operation type and status, the credit and debit
directions and the ordering - and an empty body reports everything from the portal creation date to now; a
service name this installation does not sell fails with 404. Poll
`GET api/2.0/portal/payment/customer/operationsreport` until `isCompleted` is true, then take the file from
`resultFileUrl` or open `resultFileId`: the finished file is saved into the caller's own My documents section,
where it counts against the portal storage like any other file. One operations report per user is tracked at a
time - a call made while the previous one is still running answers with that task - and
`DELETE api/2.0/portal/payment/customer/operationsreport` stops it. A build that fails ends the task with
`error` filled in rather than failing this call.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_operations_report_request_dto** | [**CustomerOperationsReportRequestDto**](CustomerOperationsReportRequestDto.md)|  | [optional] 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.customer_operations_report_request_dto import CustomerOperationsReportRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    customer_operations_report_request_dto = docspace_api_sdk.CustomerOperationsReportRequestDto() # CustomerOperationsReportRequestDto |  (optional)

    try:
        # Start the operations report
        api_response = api_instance.create_customer_operations_report(customer_operations_report_request_dto=customer_operations_report_request_dto)
        print("The response of PaymentApi->create_customer_operations_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_customer_operations_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queued task, to be polled until `isCompleted` is true |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer, or one of the names in `serviceName` is not a wallet service of this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_customer_service_usage_report**
> DocumentBuilderTaskWrapper create_customer_service_usage_report(customer_service_usage_report_request_dto=customer_service_usage_report_request_dto)

Queues the usage of the wallet services as an `xlsx` file and returns the task that will build it; the file is
not ready when the response arrives. The portal needs a billing customer and the caller has to be a DocSpace
administrator. The body takes the same filters as `GET api/2.0/portal/payment/customer/usage` - the service
names, the date range, the participant, the operation status, the usage metadata and the ordering - and an
empty body reports every service from the portal creation date to now; a service name this installation does
not sell fails with 404. Poll `GET api/2.0/portal/payment/customer/usage/report` until `isCompleted` is true,
then take the file from `resultFileUrl` or open `resultFileId`: the finished file is saved into the caller's
own My documents section, where it counts against the portal storage like any other file. One service usage
report per user is tracked at a time - a call made while the previous one is still running answers with that
task - and `DELETE api/2.0/portal/payment/customer/usage/report` stops it. It is a different report from the
operations one and does not interfere with it: per-movement history is
`POST api/2.0/portal/payment/customer/operationsreport`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **customer_service_usage_report_request_dto** | [**CustomerServiceUsageReportRequestDto**](CustomerServiceUsageReportRequestDto.md)|  | [optional] 

### Return type

[**DocumentBuilderTaskWrapper**](DocumentBuilderTaskWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.customer_service_usage_report_request_dto import CustomerServiceUsageReportRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    customer_service_usage_report_request_dto = docspace_api_sdk.CustomerServiceUsageReportRequestDto() # CustomerServiceUsageReportRequestDto |  (optional)

    try:
        # Start the service usage report
        api_response = api_instance.create_customer_service_usage_report(customer_service_usage_report_request_dto=customer_service_usage_report_request_dto)
        print("The response of PaymentApi->create_customer_service_usage_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->create_customer_service_usage_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The queued task, to be polled until `isCompleted` is true |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer, or one of the names in `serviceName` is not a wallet service of this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_accounting_service_prices**
> ServicePriceInfoArrayWrapper get_accounting_service_prices(service_name, active=active)

Returns the portal's automatic wallet top-up settings: whether it is switched on, the balance that triggers
it, the balance it tops the wallet up to and the currency it charges in. Only a DocSpace administrator may
read it, no billing customer is needed, and the call is read-only. A portal that has never configured it gets
the defaults rather than an empty result, so `enabled` is the field that says whether anything happens at all.
Two of the values are kept by the portal itself and cannot be set through this API: `lowBalanceThreshold` is
the balance below which the portal warns its administrators by mail, and `lowBalanceNotified` says whether
that warning has already gone out for the current dip. Change the rest with
`POST api/2.0/portal/payment/topupsettings`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The service whose price list is read, named the way the billing catalogue names it, such as `ai-tools` or  `backup`. Take the value from the `serviceName` field of `GET api/2.0/portal/payment/walletservices`; a name  the accounting service does not price yields an empty list rather than an error. | 
 **active** | **bool**| Whether the answer is narrowed to the prices in force at the moment of the call. Leaving it false also  returns the retired and the not yet started ones, which is what pricing a movement recorded in the past  needs. | [optional] 

### Return type

[**ServicePriceInfoArrayWrapper**](ServicePriceInfoArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.service_price_info_array_wrapper import ServicePriceInfoArrayWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    service_name = 'ai-tools' # str | The service whose price list is read, named the way the billing catalogue names it, such as `ai-tools` or  `backup`. Take the value from the `serviceName` field of `GET api/2.0/portal/payment/walletservices`; a name  the accounting service does not price yields an empty list rather than an error.
    active = false # bool | Whether the answer is narrowed to the prices in force at the moment of the call. Leaving it false also  returns the retired and the not yet started ones, which is what pricing a movement recorded in the past  needs. (optional)

    try:
        # Get the service prices from the accounting service
        api_response = api_instance.get_accounting_service_prices(service_name, active=active)
        print("The response of PaymentApi->get_accounting_service_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_accounting_service_prices: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of the service prices |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | No permissions to perform this action |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_active_services**
> ActiveServiceArrayWrapper get_active_services()

Lists the wallet services the portal is running right now: the add-ons its plan pays for that are in the
active state, plus the ones an administrator switched on by hand in the wallet service settings; the DocsCloud
trial is listed as well, although it is not paid from the wallet. Only a DocSpace administrator may call it,
no billing customer is needed for it, and the call is read-only. Every item names the service, its title and
the unit it is measured in, and says whether it is a subscription; a subscribed service also carries the limit
it grants and how much of it is used where that number is known - the editor seats and the editors currently
active for DocsCloud, the purchased units and the units already consumed for disk storage. A service listed
with no limit is one whose usage is not counted this way, not one without a limit. The catalogue of what could
be switched on is `GET api/2.0/portal/payment/walletservices`, and switching one is
`POST api/2.0/portal/payment/servicestate`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ActiveServiceArrayWrapper**](ActiveServiceArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.active_service_array_wrapper import ActiveServiceArrayWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the active wallet services
        api_response = api_instance.get_active_services()
        print("The response of PaymentApi->get_active_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_active_services: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wallet services active on the portal, with their limits and usage where those are known |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ai_prices**
> AiPricesWrapper get_ai_prices()

Returns the price list of the AI features the portal pays for out of its wallet: the chat models with the
price of their prompt and completion tokens, the embedding models, the image models with their per-image
price, and the web search providers with the price of one search. The installation needs both a billing
service and the AI gateway configured, otherwise the answer is 403, and only a DocSpace administrator may read
it; the call is read-only. Token prices are normalised per million tokens, and every price is in the single
`currency` the answer names. Each entry carries the model identifier to use when talking to the AI operations,
its display alias, its provider with the provider icon, and a link to the model's own page. It is a list of
what the models cost and not of what the portal spent - that is `GET api/2.0/portal/payment/customer/usage` -
and it says nothing about which of them are allowed here, which is
`GET api/2.0/portal/payment/ai-model/restrictions`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiPricesWrapper**](AiPricesWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prices_wrapper import AiPricesWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get AI model prices
        api_response = api_instance.get_ai_prices()
        print("The response of PaymentApi->get_ai_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_ai_prices: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The prices of the chat, embedding and image models and of the web search providers, with the currency they are in |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the installation has no billing service or no AI gateway configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_checkout_setup_url**
> StringWrapper get_checkout_setup_url(back_url, success_url)

Hands back the hosted page on which a payment method is attached to the portal's billing account, for the case
where money has to be taken later - a wallet top-up or an automatic one - rather than a plan bought now. A
portal that already has a payment method on file answers with an empty result; a DocSpace administrator may
ask for the page, but once the portal has a billing customer with an e-mail, only its payer may. The call
itself changes nothing and may be repeated: the payment method is stored by the payment provider when the
returned page is completed, after which `GET api/2.0/portal/payment/customerinfo` reports it as set. The URL
is absolute, carries the caller's e-mail, the language of the request and the currency of the region, and
redirects to `successUrl` or `backUrl` when the user finishes or cancels. It buys nothing - a plan is bought
with `PUT api/2.0/portal/payment/url`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **back_url** | **str**| The absolute address the setup page sends the user back to when attaching a payment method is abandoned. It  has to be a well-formed URL and must be reachable by that user rather than by the portal. | 
 **success_url** | **str**| The absolute address the setup page sends the user to once the payment provider has stored the payment  method. Reaching it means a method is now on file, which `GET api/2.0/portal/payment/customerinfo` confirms;  nothing has been charged. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    back_url = 'https://example.com/payment/back' # str | The absolute address the setup page sends the user back to when attaching a payment method is abandoned. It  has to be a well-formed URL and must be reachable by that user rather than by the portal.
    success_url = 'https://example.com/payment/success' # str | The absolute address the setup page sends the user to once the payment provider has stored the payment  method. Reaching it means a method is now on file, which `GET api/2.0/portal/payment/customerinfo` confirms;  nothing has been charged.

    try:
        # Get the checkout setup page URL
        api_response = api_instance.get_checkout_setup_url(back_url, success_url)
        print("The response of PaymentApi->get_checkout_setup_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_checkout_setup_url: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The absolute URL of the payment method setup page, or an empty result when the portal already has a payment method |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator or, once a billing customer exists, not its payer; or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_balance**
> BalanceWrapper get_customer_balance(refresh=refresh)

Returns the money the portal has in its wallet as the accounting service holds it: the account with its own
currency, one sub-account per currency with the amount on it, and the most recent credit movement. Only a
DocSpace administrator may read it, an installation without a billing service answers 403, and a portal that
has never been a customer gets an empty result. The call is read-only. This balance is what the wallet
services are charged against, so it falls as they are used and rises with
`POST api/2.0/portal/payment/deposit`; the movements behind a change are listed by
`GET api/2.0/portal/payment/customer/operations`. Pass `refresh=true` to re-read it from the accounting
service rather than the cache - right after a top-up the cached figure is still the old one.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Whether the answer is fetched from the billing service instead of the portal cache. The cached copy is what a  start-up needs and costs nothing; asking for a fresh one makes a remote call, so use it right after a  purchase or a top-up and not on every read. | [optional] 

### Return type

[**BalanceWrapper**](BalanceWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.balance_wrapper import BalanceWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    refresh = true # bool | Whether the answer is fetched from the billing service instead of the portal cache. The cached copy is what a  start-up needs and costs nothing; asking for a fresh one makes a remote call, so use it right after a  purchase or a top-up and not on every read. (optional)

    try:
        # Get the customer balance
        api_response = api_instance.get_customer_balance(refresh=refresh)
        print("The response of PaymentApi->get_customer_balance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_balance: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wallet account with its sub-account per currency, or an empty result when the portal has no billing customer |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_info**
> CustomerInfoWrapper get_customer_info(refresh=refresh)

Returns the billing customer behind the portal: the e-mail its billing account is registered to, whether a
payment method is stored for it, and the portal user who is the payer of that account. Only a DocSpace
administrator may read it, and the call is read-only. The answer is empty in two ordinary cases - the
installation has no billing service configured at all, and the portal has never been a customer - so an empty
body is not an error. `payer` is filled in only when the billing e-mail belongs to a portal user; when it does
not, the e-mail is still shown but the field stays empty, and that is what makes every payer-only operation of
this group unreachable for everybody. `refresh=true` re-reads the customer from the billing provider instead
of the cache, which is worth doing right after a payment method has been attached.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Whether the answer is fetched from the billing service instead of the portal cache. The cached copy is what a  start-up needs and costs nothing; asking for a fresh one makes a remote call, so use it right after a  purchase or a top-up and not on every read. | [optional] 

### Return type

[**CustomerInfoWrapper**](CustomerInfoWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.customer_info_wrapper import CustomerInfoWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    refresh = true # bool | Whether the answer is fetched from the billing service instead of the portal cache. The cached copy is what a  start-up needs and costs nothing; asking for a fresh one makes a remote call, so use it right after a  purchase or a top-up and not on every read. (optional)

    try:
        # Get the customer information
        api_response = api_instance.get_customer_info(refresh=refresh)
        print("The response of PaymentApi->get_customer_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The billing customer with its payer, or an empty result when the portal has no customer or billing is not configured |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_monthly_usage**
> CustomerMonthlyUsageArrayWrapper get_customer_monthly_usage(start_date=start_date, end_date=end_date)

Returns what the portal spent from its wallet added up per calendar month, so a client can draw a spending
chart without paging through every movement. Only a DocSpace administrator may read it, a portal with no
billing customer answers with an empty result, and the call is read-only. `startDate` and `endDate` bound the
period, both inclusive, and default to the portal creation date and the present moment; the months are cut in
the portal time zone, so a movement at the edge of a month falls where the portal sees it and not where UTC
does. Each item names its year and month, the total charged in it with the currency, and how many operations
that total came from. The movements behind a month are in `GET api/2.0/portal/payment/customer/operations`,
and the same figures as a file come from `POST api/2.0/portal/payment/customer/usage/monthly/report`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **start_date** | **datetime**| The beginning of the reported period, inclusive. The months are cut in the portal time zone rather than in  UTC, so spending at the turn of a month falls where the portal sees it; defaults to the portal creation date. | [optional] 
 **end_date** | **datetime**| The end of the reported period, inclusive. Cut in the portal time zone in the same way as `startDate`, and  defaults to the moment the call is made. | [optional] 

### Return type

[**CustomerMonthlyUsageArrayWrapper**](CustomerMonthlyUsageArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.customer_monthly_usage_array_wrapper import CustomerMonthlyUsageArrayWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    start_date = '2025-01-01T00:00:00Z' # datetime | The beginning of the reported period, inclusive. The months are cut in the portal time zone rather than in  UTC, so spending at the turn of a month falls where the portal sees it; defaults to the portal creation date. (optional)
    end_date = '2025-12-31T23:59:59Z' # datetime | The end of the reported period, inclusive. Cut in the portal time zone in the same way as `startDate`, and  defaults to the moment the call is made. (optional)

    try:
        # Get the customer monthly usage
        api_response = api_instance.get_customer_monthly_usage(start_date=start_date, end_date=end_date)
        print("The response of PaymentApi->get_customer_monthly_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_monthly_usage: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | One item per calendar month that had spending, or an empty result when the portal has no billing customer |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_monthly_usage_report**
> DocumentBuilderTaskWrapper get_customer_monthly_usage_report()

Returns the state of the `xlsx` monthly usage report this user started with
`POST api/2.0/portal/payment/customer/usage/monthly/report`: `percentage` while it is being built,
`isCompleted` when it is done, `resultFileId`, `resultFileName` and `resultFileUrl` pointing at the file in
the caller's My documents, and `error` when the build failed. The portal needs a billing customer and the
caller has to be a DocSpace administrator; the call is read-only and is the one to poll. The task is kept per
user and per report kind, so it reports neither another administrator's report nor the operations and service
usage ones, which have their own status operations. An empty result means this user has no monthly usage
report at all - none was started, or the finished one was already picked up or terminated. A completed task is
dropped as soon as the next report is started, so read the file link out of the same answer that first reports
`isCompleted`.

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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the monthly usage report status
        api_response = api_instance.get_customer_monthly_usage_report()
        print("The response of PaymentApi->get_customer_monthly_usage_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_monthly_usage_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of this user's monthly usage report, or an empty result when there is none |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_operations**
> ReportWrapper get_customer_operations(offset=offset, limit=limit, service_name=service_name, start_date=start_date, end_date=end_date, participant_name=participant_name, credit=credit, debit=debit, type=type, status=status, order_by=order_by, order_type=order_type)

Lists the money movements on the portal's wallet - top-ups, the charges of the wallet services, refunds and
corrections - one page at a time, which is what a billing history is built from. Only a DocSpace administrator
may read it, a portal with no billing customer answers with an empty result, and the call is read-only. Every
filter is optional: `startDate` and `endDate` are read in the portal time zone and default to the portal
creation date and the present moment, `serviceName` narrows to particular wallet services and fails with 404
on a name this installation does not sell, `participantName`, `type` and `status` narrow to who caused a
movement and how it ended, and `credit` and `debit` include or exclude the two directions. `offset` and
`limit` page through the result and default to 0 and 25, `orderBy` and `orderType` sort it, and the answer
repeats them next to `totalQuantity`, `totalPage` and `currentPage` so a client can page without counting. The
same data as a downloadable file is `POST api/2.0/portal/payment/customer/operationsreport`, and the figures
added up per service are `GET api/2.0/portal/payment/customer/usage`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The number of movements to skip before the first one returned, for walking through a long history page by  page. Counted after the filters and the ordering are applied, and starts at 0 when omitted. | [optional] 
 **limit** | **int**| The maximum number of movements returned in one page. Defaults to 25 when omitted; the answer echoes the  window back next to `totalQuantity`, `totalPage` and `currentPage`, so the next `offset` can be computed  without counting the items. | [optional] 
 **service_name** | [**List[str]**](str.md)| The wallet services whose movements are kept, named the way the billing catalogue names them - `backup`,  `ai-tools`, `ai-search`, `disk-storage`, `docscloud`. Take the values from the `serviceName` field of  `GET api/2.0/portal/payment/walletservices`; the match ignores case, a name this installation does not sell  fails the call with 404, and an omitted list keeps every service. A bare string is accepted in place of an  array for backward compatibility. | [optional] 
 **start_date** | **datetime**| The beginning of the reported period, inclusive. Read in the portal time zone rather than in UTC, so a  movement at the edge of the period falls where the portal sees it; defaults to the portal creation date. | [optional] 
 **end_date** | **datetime**| The end of the reported period, inclusive. Read in the portal time zone rather than in UTC, and defaults to  the moment the call is made. | [optional] 
 **participant_name** | **str**| The participant whose movements are kept - the account the accounting service records as the cause of a  movement. A movement caused by a portal user carries that user ID here, and one caused by the portal itself  carries the customer name; surrounding whitespace is trimmed, and an omitted value keeps every participant. | [optional] 
 **credit** | **bool**| Whether movements that add money to the wallet - top-ups, refunds and corrections in the portal's favour -  are kept. Both directions are reported when neither this nor `debit` is given. | [optional] 
 **debit** | **bool**| Whether movements that take money out of the wallet - the charges of the wallet services - are kept. Both  directions are reported when neither this nor `credit` is given. | [optional] 
 **type** | [**OperationType**](.md)| The kind of movement to keep, which says what caused the money to move rather than how it ended. Every kind  is reported when it is omitted. | [optional] 
 **status** | [**OperationStatus**](.md)| The outcome to keep. A movement that is still being settled is reported as pending and may change later,  while the other outcomes are final; every outcome is reported when this is omitted. | [optional] 
 **order_by** | **str**| The name of the field the movements are sorted by, spelled as the accounting service names it, such as  `StartDate` or `ServiceName`. Surrounding whitespace is trimmed, and the accounting service applies its own  ordering when this is omitted. | [optional] 
 **order_type** | [**OperationOrderType**](.md)| The direction the field named in `orderBy` is sorted in. Newest or largest first is what the accounting  service does by default, so leaving this out sorts the same way as asking for descending explicitly. | [optional] 

### Return type

[**ReportWrapper**](ReportWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.operation_order_type import OperationOrderType
from docspace_api_sdk.models.operation_status import OperationStatus
from docspace_api_sdk.models.operation_type import OperationType
from docspace_api_sdk.models.report_wrapper import ReportWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    offset = 0 # int | The number of movements to skip before the first one returned, for walking through a long history page by  page. Counted after the filters and the ordering are applied, and starts at 0 when omitted. (optional)
    limit = 25 # int | The maximum number of movements returned in one page. Defaults to 25 when omitted; the answer echoes the  window back next to `totalQuantity`, `totalPage` and `currentPage`, so the next `offset` can be computed  without counting the items. (optional)
    service_name = ['[backup]'] # List[str] | The wallet services whose movements are kept, named the way the billing catalogue names them - `backup`,  `ai-tools`, `ai-search`, `disk-storage`, `docscloud`. Take the values from the `serviceName` field of  `GET api/2.0/portal/payment/walletservices`; the match ignores case, a name this installation does not sell  fails the call with 404, and an omitted list keeps every service. A bare string is accepted in place of an  array for backward compatibility. (optional)
    start_date = '2024-01-01T00:00:00Z' # datetime | The beginning of the reported period, inclusive. Read in the portal time zone rather than in UTC, so a  movement at the edge of the period falls where the portal sees it; defaults to the portal creation date. (optional)
    end_date = '2024-01-31T23:59:59Z' # datetime | The end of the reported period, inclusive. Read in the portal time zone rather than in UTC, and defaults to  the moment the call is made. (optional)
    participant_name = 'My Own Corporation' # str | The participant whose movements are kept - the account the accounting service records as the cause of a  movement. A movement caused by a portal user carries that user ID here, and one caused by the portal itself  carries the customer name; surrounding whitespace is trimmed, and an omitted value keeps every participant. (optional)
    credit = true # bool | Whether movements that add money to the wallet - top-ups, refunds and corrections in the portal's favour -  are kept. Both directions are reported when neither this nor `debit` is given. (optional)
    debit = false # bool | Whether movements that take money out of the wallet - the charges of the wallet services - are kept. Both  directions are reported when neither this nor `credit` is given. (optional)
    type = docspace_api_sdk.OperationType() # OperationType | The kind of movement to keep, which says what caused the money to move rather than how it ended. Every kind  is reported when it is omitted. (optional)
    status = docspace_api_sdk.OperationStatus() # OperationStatus | The outcome to keep. A movement that is still being settled is reported as pending and may change later,  while the other outcomes are final; every outcome is reported when this is omitted. (optional)
    order_by = 'StartDate' # str | The name of the field the movements are sorted by, spelled as the accounting service names it, such as  `StartDate` or `ServiceName`. Surrounding whitespace is trimmed, and the accounting service applies its own  ordering when this is omitted. (optional)
    order_type = docspace_api_sdk.OperationOrderType() # OperationOrderType | The direction the field named in `orderBy` is sorted in. Newest or largest first is what the accounting  service does by default, so leaving this out sorts the same way as asking for descending explicitly. (optional)

    try:
        # Get the wallet operations
        api_response = api_instance.get_customer_operations(offset=offset, limit=limit, service_name=service_name, start_date=start_date, end_date=end_date, participant_name=participant_name, credit=credit, debit=debit, type=type, status=status, order_by=order_by, order_type=order_type)
        print("The response of PaymentApi->get_customer_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_operations: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A page of wallet movements with its paging information, or an empty result when the portal has no billing customer |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | One of the names in `serviceName` is not a wallet service of this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_operations_report**
> DocumentBuilderTaskWrapper get_customer_operations_report()

Returns the state of the `xlsx` wallet operations report this user started with
`POST api/2.0/portal/payment/customer/operationsreport`: `percentage` while it is being built, `isCompleted`
when it is done, `resultFileId`, `resultFileName` and `resultFileUrl` pointing at the file in the caller's My
documents, and `error` when the build failed. The portal needs a billing customer and the caller has to be a
DocSpace administrator; the call is read-only and is the one to poll. The task is kept per user and per report
kind, so it never reports another administrator's report, nor the service usage and monthly usage ones, which
have their own status operations. An empty result means this user has no operations report at all - none was
started, or the finished one was already picked up or terminated. A completed task is dropped as soon as the
next report is started, so read the file link out of the same answer that first reports `isCompleted`.

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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the operations report status
        api_response = api_instance.get_customer_operations_report()
        print("The response of PaymentApi->get_customer_operations_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_operations_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of this user's operations report, or an empty result when there is none |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_service_usage**
> CustomerServiceUsageReportWrapper get_customer_service_usage(service_name=service_name, participant_name=participant_name, status=status, start_date=start_date, end_date=end_date, metadata=metadata, offset=offset, limit=limit, order_by=order_by, order_type=order_type)

Returns how much of each wallet service the portal consumed and what that cost, added up per service instead
of listed per movement. Only a DocSpace administrator may read it, a portal with no billing customer answers
with an empty result, and the call is read-only. The filters are optional: `serviceName` narrows to particular
services and fails with 404 on a name this installation does not sell, `participantName` and `status` narrow
to who consumed and how the operation ended, `startDate` and `endDate` bound the period in the portal time
zone, `metadata` matches the key and value pairs a service records with its usage, and `offset`, `limit`,
`orderBy` and `orderType` page and sort the result. Amounts come with the unit the service is sold in, except
AI tools, whose consumption is reported in tokens rather than in AI credits. The individual charges behind
these totals are `GET api/2.0/portal/payment/customer/operations`, and the same figures as a downloadable file
are `POST api/2.0/portal/payment/customer/usage/report`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | [**List[str]**](str.md)| The wallet services whose consumption is added up, named the way the billing catalogue names them -  `backup`, `ai-tools`, `ai-search`, `disk-storage`, `docscloud`. Take the values from the `serviceName` field  of `GET api/2.0/portal/payment/walletservices`; the match ignores case, a name this installation does not  sell fails the call with 404, and an omitted list covers every service. | [optional] 
 **participant_name** | **str**| The participant whose consumption is added up - the account the accounting service records as the consumer.  Consumption caused by a portal user carries that user ID here; surrounding whitespace is trimmed, and an  omitted value covers every participant. | [optional] 
 **status** | [**OperationStatus**](.md)| The outcome to keep. Consumption that is still being settled is reported as pending and may change later,  while the other outcomes are final; every outcome is counted when this is omitted. | [optional] 
 **start_date** | **datetime**| The beginning of the reported period, inclusive. Read in the portal time zone rather than in UTC, and  defaults to the portal creation date. | [optional] 
 **end_date** | **datetime**| The end of the reported period, inclusive. Read in the portal time zone rather than in UTC, and defaults to  the moment the call is made. | [optional] 
 **metadata** | [**Dict[str, Optional[str]]**](str.md)| The usage annotations a wallet service records alongside its consumption, as the key and value pairs that  must all match for a record to be counted. The keys are chosen by the service that writes them, so read them  off the `metadata` of the records already returned rather than guessing; an omitted map counts every record. | [optional] 
 **offset** | **int**| The number of per-service totals to skip before the first one returned. Counted after the filters and the  ordering are applied, and starts at 0 when omitted. | [optional] 
 **limit** | **int**| The maximum number of per-service totals returned in one page. Defaults to 25 when omitted; the answer echoes  the window back with its paging information, so the next `offset` can be computed without counting the items. | [optional] 
 **order_by** | **str**| The name of the field the per-service totals are sorted by, spelled as the accounting service names it, such  as `ServiceName` or `StartDate`. Surrounding whitespace is trimmed, and the accounting service applies its  own ordering when this is omitted. | [optional] 
 **order_type** | [**OperationOrderType**](.md)| The direction the field named in `orderBy` is sorted in. Newest or largest first is what the accounting  service does by default, so leaving this out sorts the same way as asking for descending explicitly. | [optional] 

### Return type

[**CustomerServiceUsageReportWrapper**](CustomerServiceUsageReportWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.customer_service_usage_report_wrapper import CustomerServiceUsageReportWrapper
from docspace_api_sdk.models.operation_order_type import OperationOrderType
from docspace_api_sdk.models.operation_status import OperationStatus
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    service_name = ['[backup]'] # List[str] | The wallet services whose consumption is added up, named the way the billing catalogue names them -  `backup`, `ai-tools`, `ai-search`, `disk-storage`, `docscloud`. Take the values from the `serviceName` field  of `GET api/2.0/portal/payment/walletservices`; the match ignores case, a name this installation does not  sell fails the call with 404, and an omitted list covers every service. (optional)
    participant_name = 'My Own Corporation' # str | The participant whose consumption is added up - the account the accounting service records as the consumer.  Consumption caused by a portal user carries that user ID here; surrounding whitespace is trimmed, and an  omitted value covers every participant. (optional)
    status = docspace_api_sdk.OperationStatus() # OperationStatus | The outcome to keep. Consumption that is still being settled is reported as pending and may change later,  while the other outcomes are final; every outcome is counted when this is omitted. (optional)
    start_date = '2025-01-01T00:00:00Z' # datetime | The beginning of the reported period, inclusive. Read in the portal time zone rather than in UTC, and  defaults to the portal creation date. (optional)
    end_date = '2025-12-31T23:59:59Z' # datetime | The end of the reported period, inclusive. Read in the portal time zone rather than in UTC, and defaults to  the moment the call is made. (optional)
    metadata = {'key': '{\"key1\":\"value1\",\"key2\":\"value2\"}'} # Dict[str, Optional[str]] | The usage annotations a wallet service records alongside its consumption, as the key and value pairs that  must all match for a record to be counted. The keys are chosen by the service that writes them, so read them  off the `metadata` of the records already returned rather than guessing; an omitted map counts every record. (optional)
    offset = 0 # int | The number of per-service totals to skip before the first one returned. Counted after the filters and the  ordering are applied, and starts at 0 when omitted. (optional)
    limit = 25 # int | The maximum number of per-service totals returned in one page. Defaults to 25 when omitted; the answer echoes  the window back with its paging information, so the next `offset` can be computed without counting the items. (optional)
    order_by = 'ServiceName' # str | The name of the field the per-service totals are sorted by, spelled as the accounting service names it, such  as `ServiceName` or `StartDate`. Surrounding whitespace is trimmed, and the accounting service applies its  own ordering when this is omitted. (optional)
    order_type = docspace_api_sdk.OperationOrderType() # OperationOrderType | The direction the field named in `orderBy` is sorted in. Newest or largest first is what the accounting  service does by default, so leaving this out sorts the same way as asking for descending explicitly. (optional)

    try:
        # Get the customer service usage
        api_response = api_instance.get_customer_service_usage(service_name=service_name, participant_name=participant_name, status=status, start_date=start_date, end_date=end_date, metadata=metadata, offset=offset, limit=limit, order_by=order_by, order_type=order_type)
        print("The response of PaymentApi->get_customer_service_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_service_usage: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The usage and cost per wallet service with its paging information, or an empty result when the portal has no billing customer |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | One of the names in `serviceName` is not a wallet service of this installation |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_customer_service_usage_report**
> DocumentBuilderTaskWrapper get_customer_service_usage_report()

Returns the state of the `xlsx` service usage report this user started with
`POST api/2.0/portal/payment/customer/usage/report`: `percentage` while it is being built, `isCompleted` when
it is done, `resultFileId`, `resultFileName` and `resultFileUrl` pointing at the file in the caller's My
documents, and `error` when the build failed. The portal needs a billing customer and the caller has to be a
DocSpace administrator; the call is read-only and is the one to poll. The task is kept per user and per report
kind, so it reports neither another administrator's report nor the operations and monthly usage ones, which
have their own status operations. An empty result means this user has no service usage report at all - none
was started, or the finished one was already picked up or terminated. A completed task is dropped as soon as
the next report is started, so read the file link out of the same answer that first reports `isCompleted`.

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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the service usage report status
        api_response = api_instance.get_customer_service_usage_report()
        print("The response of PaymentApi->get_customer_service_usage_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_customer_service_usage_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The state of this user's service usage report, or an empty result when there is none |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_account**
> StringWrapper get_payment_account(back_url=back_url)

Hands back the address of the portal page on which the billing account is managed - the payment method on
file, the invoices and the receipts - so a client can link to it instead of assembling the address itself. The
portal must already have a billing customer: one that has never had it gets an empty result, and an
installation without a billing service answers 403. Only the payer or the portal owner may read it, and the
call changes nothing. The value is relative to the portal root (`payment.ashx`), and the optional `backUrl` is
appended to it as a query parameter so the page can send the user back where they came from. It is not a
checkout page: a plan is bought with `PUT api/2.0/portal/payment/url` and a payment method is attached with
`GET api/2.0/portal/payment/checkoutsetupurl`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **back_url** | **str**| The absolute address the billing account page should offer as its way back. It is appended to the returned  portal-relative address as a query parameter rather than followed here, and omitting it yields the bare  address of the page. | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    back_url = 'https://example.com' # str | The absolute address the billing account page should offer as its way back. It is appended to the returned  portal-relative address as a query parameter rather than followed here, and omitting it yields the bare  address of the page. (optional)

    try:
        # Get the billing account page
        api_response = api_instance.get_payment_account(back_url=back_url)
        print("The response of PaymentApi->get_payment_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_account: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The portal-relative address of the billing account page, or an empty result when the portal has no billing customer |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is neither the payer nor the portal owner, or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_currencies**
> CurrenciesArrayWrapper get_payment_currencies()

Tells a client which currency the portal is billed in: the default currency of the portal region always comes
first, followed by the currency resolved for the current request when that one differs, so the answer holds
one or two items. Nothing has to be called first, the caller needs the permission to edit the portal settings,
and the call is read-only. Each item carries the country code of the region, the currency symbol and the
native name of the currency; the first item is the currency the amounts from
`GET api/2.0/portal/payment/prices` are expressed in. These are the currencies of the subscription prices, and
they are not the accounting currencies the wallet is topped up in - those come with the balance in
`GET api/2.0/portal/payment/customer/balance`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**CurrenciesArrayWrapper**](CurrenciesArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.currencies_array_wrapper import CurrenciesArrayWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the billing currencies
        api_response = api_instance.get_payment_currencies()
        print("The response of PaymentApi->get_payment_currencies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_currencies: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The default currency of the portal region first, followed by the currency of the current request when it differs |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_quotas**
> QuotaArrayWrapper get_payment_quotas(wallet=wallet, additional=additional)

Lists the quotas the portal can be put on - the paid plans and the wallet services - each with its price, its
features and the limits it grants, which is what a pricing page is built from. Nothing has to be called first,
the caller needs the permission to edit the portal settings, and the call is read-only. Only quotas marked
visible are listed, newest first, and the two optional filters narrow that: `wallet` selects the wallet
services (`true`) or the subscription plans (`false`), `additional` selects the add-ons to a plan (`true`) or
the plans themselves (`false`), and an omitted filter keeps both kinds. A portal on a non-profit quota is a
special case - asking for `additional=false` returns that single quota and nothing else, because no other plan
may be bought for it. The quota the portal is actually on is not marked here; read it from
`GET api/2.0/portal/payment/quota`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet** | **bool**| Which side of the catalogue is listed: `true` keeps the services paid out of the portal wallet, `false` keeps  the subscription plans, and omitting it keeps both. | [optional] 
 **additional** | **bool**| Which layer of the catalogue is listed: `true` keeps the add-ons that extend a plan, `false` keeps the plans  themselves, and omitting it keeps both. | [optional] 

### Return type

[**QuotaArrayWrapper**](QuotaArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.quota_array_wrapper import QuotaArrayWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    wallet = true # bool | Which side of the catalogue is listed: `true` keeps the services paid out of the portal wallet, `false` keeps  the subscription plans, and omitting it keeps both. (optional)
    additional = true # bool | Which layer of the catalogue is listed: `true` keeps the add-ons that extend a plan, `false` keeps the plans  themselves, and omitting it keeps both. (optional)

    try:
        # Get the purchasable quotas
        api_response = api_instance.get_payment_quotas(wallet=wallet, additional=additional)
        print("The response of PaymentApi->get_payment_quotas:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_quotas: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The visible quotas matching the filters, newest first, each with its price, features and limits |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_payment_url**
> StringWrapper get_payment_url(payment_url_request_dto=payment_url_request_dto)

Starts the purchase of a monthly paid plan for this portal by handing back the hosted checkout page the buyer
has to open; nothing is bought until that page is completed. The portal must have no paid plan yet - a portal
whose plan is already paid gets an empty result and changes its subscription through
`PUT api/2.0/portal/payment/update` instead - and the product name in `quantity` must be one of the monthly,
non-wallet plans listed by `GET api/2.0/portal/payment/quotas`. Only a DocSpace administrator may call it. The
call itself changes nothing on the portal and may be repeated: the money is taken by the payment provider on
the checkout page, and the plan becomes active once the provider confirms it. The returned URL is absolute and
single-purpose - it carries the caller's e-mail, the language of the request and the currency of the request
region, and it redirects to `successUrl` or `backUrl` when the buyer finishes or cancels. Exactly one product
per call is accepted and its quantity has to be greater than zero; yearly and wallet products are refused, and
wallet services are bought with `PUT api/2.0/portal/payment/updatewallet` instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **payment_url_request_dto** | [**PaymentUrlRequestDto**](PaymentUrlRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.payment_url_request_dto import PaymentUrlRequestDto
from docspace_api_sdk.models.string_wrapper import StringWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    payment_url_request_dto = docspace_api_sdk.PaymentUrlRequestDto() # PaymentUrlRequestDto |  (optional)

    try:
        # Get the payment page URL
        api_response = api_instance.get_payment_url(payment_url_request_dto=payment_url_request_dto)
        print("The response of PaymentApi->get_payment_url:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_payment_url: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The absolute URL of the checkout page to open, or an empty result when the portal already has a paid plan |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | `quantity` holds more than one product, a quantity that is not greater than zero, or a product that is not a monthly plan |  -  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_portal_prices**
> GetPortalPrices200Response get_portal_prices()

Lists what one unit of every purchasable product costs, keyed by the product name that `quantity` takes in the
purchase operations, so a client can price a plan or a wallet service without reading the whole quota list.
Nothing has to be called first, and the caller needs the permission to edit the portal settings, which portal
administrators and the owner have. The call is read-only. Prices are given in the one currency resolved for
this request from the portal region, which `GET api/2.0/portal/payment/currencies` reports; a product with no
price in that currency comes back as `0` rather than being left out, so a zero means unpriced and not free.
The list covers the products on offer, not the portal's own plan - the plan in force, with its limits and its
usage, is `GET api/2.0/portal/payment/quota`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**GetPortalPrices200Response**](GetPortalPrices200Response.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.get_portal_prices200_response import GetPortalPrices200Response
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the product prices
        api_response = api_instance.get_portal_prices()
        print("The response of PaymentApi->get_portal_prices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_portal_prices: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Product name to the price of one unit in the currency of the request, `0` where the product has no price in it |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_quota_payment_information**
> QuotaWrapper get_quota_payment_information(refresh=refresh)

Returns the quota the portal is on right now - its paid plan or the free one - with everything a client needs
to render itself: the price, the features that are switched on, the limits they grant (rooms, storage in
bytes, users, administrators, AI) and how much of each is already used. Every signed-in member of the portal
reads it, so it is not restricted to administrators; only guests are refused with 403. The call is read-only.
The plan is served from the cache by default, which is what a start-up needs; `refresh=true` fetches it from
the billing service instead, so use that right after a purchase and not routinely, because it is a remote
call. The catalogue of the quotas that could be bought instead is `GET api/2.0/portal/payment/quotas`, and the
money side of the same portal - customer, wallet and balance - starts at
`GET api/2.0/portal/payment/customerinfo`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refresh** | **bool**| Whether the answer is fetched from the billing service instead of the portal cache. The cached copy is what a  start-up needs and costs nothing; asking for a fresh one makes a remote call, so use it right after a  purchase or a top-up and not on every read. | [optional] 

### Return type

[**QuotaWrapper**](QuotaWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.quota_wrapper import QuotaWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    refresh = true # bool | Whether the answer is fetched from the billing service instead of the portal cache. The cached copy is what a  start-up needs and costs nothing; asking for a fresh one makes a remote call, so use it right after a  purchase or a top-up and not on every read. (optional)

    try:
        # Get the current plan and limits
        api_response = api_instance.get_quota_payment_information(refresh=refresh)
        print("The response of PaymentApi->get_quota_payment_information:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_quota_payment_information: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The quota the portal is on, with its price, features, limits and current usage |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is a guest of this portal |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_restricted_ai_models**
> RestrictedModelsResponseWrapper get_restricted_ai_models()

Returns the AI chat models that are barred on this portal - the ones no user of it may pick for a
conversation, whatever the price list offers. Only a DocSpace administrator may read it, and the call is
read-only. When the installation has no billing service or AI is not enabled for the portal, the answer is an
empty set instead of an error, which is indistinguishable from a portal that restricts nothing. An empty
`models` therefore means every model in `GET api/2.0/portal/payment/ai-prices` may be used. The set names the
barred models and not the allowed ones; replace it with `PUT api/2.0/portal/payment/ai-model/restrictions`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**RestrictedModelsResponseWrapper**](RestrictedModelsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.restricted_models_response_wrapper import RestrictedModelsResponseWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get restricted AI models
        api_response = api_instance.get_restricted_ai_models()
        print("The response of PaymentApi->get_restricted_ai_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_restricted_ai_models: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The identifiers of the AI chat models barred on this portal, empty when none is |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_subscription_balance_info**
> SubscriptionBalanceInfoWrapper get_subscription_balance_info()

Reports in money how much of the portal's paid subscription period is still unused - the credit that
`POST api/2.0/portal/payment/subscription/movetowallet` would carry over to the wallet if the subscription
were ended now. The portal must have a billing customer and a plan in the paid state; a plan that is not paid
answers 402, and a paid plan without a subscription row gives 404. Only the payer - the portal user whose
e-mail is the billing customer's e-mail - may read it, and the call is read-only. The answer states the total
cost of the current period with its currency, the start and the end of that period in UTC, the moment the
unused part is measured up to, the days already elapsed, and the remaining balance both in the subscription
currency and converted to the wallet currency. Every figure is computed for the instant of the request, so it
changes between calls.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionBalanceInfoWrapper**](SubscriptionBalanceInfoWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.subscription_balance_info_wrapper import SubscriptionBalanceInfoWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the subscription balance information
        api_response = api_instance.get_subscription_balance_info()
        print("The response of PaymentApi->get_subscription_balance_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_subscription_balance_info: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The unused balance of the current subscription period with its period boundaries and currencies |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The plan currently paid is a wallet product or has no product identifier |  -  |
**402** | The plan of the portal is not in the paid state |  -  |
**403** | The caller is not the payer of this portal, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer, or its paid plan has no subscription |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_wallet_service_settings**
> TenantWalletServiceSettingsWrapper get_tenant_wallet_service_settings()

Returns which wallet services an administrator has switched on for this portal by hand, as opposed to the ones
its plan pays for. Only a DocSpace administrator may read it, an installation without a billing service
answers 403, no billing customer is needed, and the call is read-only. `enabledServices` holds the names of
those services and is empty when none was switched on. This is the stored setting and not the state of the
portal: a service the plan brings with it is active without appearing here, so the honest answer to what is
running is `GET api/2.0/portal/payment/activeservices`. One entry is changed with
`POST api/2.0/portal/payment/servicestate`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantWalletServiceSettingsWrapper**](TenantWalletServiceSettingsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_wallet_service_settings_wrapper import TenantWalletServiceSettingsWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the wallet service settings
        api_response = api_instance.get_tenant_wallet_service_settings()
        print("The response of PaymentApi->get_tenant_wallet_service_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_tenant_wallet_service_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wallet services switched on by hand for this portal |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tenant_wallet_settings**
> TenantWalletSettingsResponseWrapper get_tenant_wallet_settings()

Returns the portal's automatic wallet top-up settings - whether it is on, the balance that triggers a
charge, the balance it is topped up to, and the currency both are expressed in. Any DocSpace
administrator may read them, and unlike the operation that changes them this one needs neither a
billing customer nor a configured billing service, so it answers on a portal that has never paid for
anything. It is read-only and changes nothing.
A portal that has never configured top-up gets the defaults rather than an empty result: `enabled` is
false, `currency` is null, and `minBalance` and `upToBalance` are 0. Those two zeros are outside the
ranges `POST api/2.0/portal/payment/topupsettings` accepts - 5 to 1000 and 6 to 5000 - so the answer
cannot be sent straight back to it; supply real values instead. `lastModified` is
`0001-01-01T00:00:00` until the settings are stored for the first time.
`lowBalanceThreshold` and `lowBalanceNotified` are maintained by the portal itself: they are reported
here, but ignored when the settings are written.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**TenantWalletSettingsResponseWrapper**](TenantWalletSettingsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_wallet_settings_response_wrapper import TenantWalletSettingsResponseWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get the auto top-up settings
        api_response = api_instance.get_tenant_wallet_settings()
        print("The response of PaymentApi->get_tenant_wallet_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_tenant_wallet_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The automatic top-up settings of the portal, or their defaults when it has never configured them |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_service**
> WalletServiceWrapper get_wallet_service(service)

Returns one wallet service by name, for a client that already knows which service it needs and does not want
the whole catalogue. `service` is the name of the service - `Storage`, `Backup`, `AITools`, `Admin`,
`DocsCloud`, `DocsCloudDevPack` or `AISearch` - and a name this installation does not sell answers 404.
Nothing has to be called first, the caller needs the permission to edit the portal settings, and the call is
read-only. The answer has the same shape as one item of `GET api/2.0/portal/payment/walletservices` - the
price of a unit, the unit, the limits the service grants and its service name - except that the variants of a
service are not grouped into `innerServices` here, because a single service is looked up directly. The price
is in the currency resolved for the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**TenantWalletService**](.md)| The service to look up, given by its catalogue name. A service this installation does not sell answers 404,  and the whole catalogue is `GET api/2.0/portal/payment/walletservices`. | 

### Return type

[**WalletServiceWrapper**](WalletServiceWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_wallet_service import TenantWalletService
from docspace_api_sdk.models.wallet_service_wrapper import WalletServiceWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    service = docspace_api_sdk.TenantWalletService() # TenantWalletService | The service to look up, given by its catalogue name. A service this installation does not sell answers 404,  and the whole catalogue is `GET api/2.0/portal/payment/walletservices`.

    try:
        # Get a wallet service
        api_response = api_instance.get_wallet_service(service)
        print("The response of PaymentApi->get_wallet_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_wallet_service: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wallet service with its price, unit and the limits it grants |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings |  -  |
**404** | This installation does not sell a wallet service under that name |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wallet_services**
> WalletServiceArrayWrapper get_wallet_services()

Lists every service the portal may pay for out of its wallet - extra administrators, disk storage, backup, AI
tools, AI search and DocsCloud - with the price of a unit, the unit it is sold in and whether the portal has
it switched on. Nothing has to be called first, the caller needs the permission to edit the portal settings,
and the call is read-only. Services that are variants of one another are folded together: the visible one
carries the rest in its `innerServices`, so a client renders one card per group. The AI services are left out
entirely when AI is not enabled for the portal. This is the catalogue and not the state of the portal - what
is actually running is `GET api/2.0/portal/payment/activeservices`, one service on its own is
`GET api/2.0/portal/payment/walletservice`, and switching one on or off is
`POST api/2.0/portal/payment/servicestate`.

For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**WalletServiceArrayWrapper**](WalletServiceArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.wallet_service_array_wrapper import WalletServiceArrayWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Get wallet services
        api_response = api_instance.get_wallet_services()
        print("The response of PaymentApi->get_wallet_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->get_wallet_services: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The wallet services on offer, with their prices, units and grouped variants |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_subscription_to_wallet**
> BooleanWrapper move_subscription_to_wallet(quantity_request_dto=quantity_request_dto)

Ends the portal's paid subscription and moves it onto the wallet: the unused balance of the running period is
credited to the wallet, the wallet is topped up from the payment method on file if that credit does not cover
the purchase, and the requested number of administrators is then bought as a wallet service. The portal needs
a billing customer with a payment method set and a plan in the paid state, `quantity` has to name the
administrators wallet product, and the number asked for may not be below the administrators the portal already
has - read the credit that will be carried over from `GET api/2.0/portal/payment/subscription/balance` first.
Only the payer may call it. The call is mutating, spends money and cannot be undone: the subscription is ended
before the purchase is attempted, so a failure in the second half leaves the portal on the wallet with the
money credited but the administrators unbought, and a repeat would then buy them a second time. It is limited
to ten requests a minute per user by default. The result is `true` when the administrators were bought.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity_request_dto** | [**QuantityRequestDto**](QuantityRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.quantity_request_dto import QuantityRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    quantity_request_dto = docspace_api_sdk.QuantityRequestDto() # QuantityRequestDto |  (optional)

    try:
        # Move the subscription to the wallet
        api_response = api_instance.move_subscription_to_wallet(quantity_request_dto=quantity_request_dto)
        print("The response of PaymentApi->move_subscription_to_wallet:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->move_subscription_to_wallet: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | `true` when the balance was moved to the wallet and the administrators were bought |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 1-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | `quantity` does not name the administrators wallet product, or the number asked for is below the administrators the portal already has |  -  |
**402** | The plan of the portal is not paid, the balance could not be moved, or the wallet is still short of the price after the top-up |  -  |
**403** | The caller is not the payer of this portal, the portal has no billing service configured, or the customer has no payment method set |  -  |
**404** | This portal has no billing customer, its paid plan has no subscription, or the price of the administrators product is unknown |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (10 req / 1 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_payment_request**
> send_payment_request(sales_requests_dto=sales_requests_dto)

Sends the portal's message to the ONLYOFFICE sales team - the contact-sales form behind a request for a quote,
an invoice or a plan that cannot be bought online. `email` has to be a well-formed address and is where the
answer will go, while `userName` and `message` say who is asking and what for; all three are required and none
may be empty. Only a DocSpace administrator may call it. Nothing on the portal changes: no plan, no quota and
no payment is touched, a message is mailed out and the request is written to the portal audit trail. There is
no response body - status 200 means the message was handed to the mail service - and the call is not
idempotent, so a repeat sends a second message. It is limited to ten requests a minute per user by default and
answers 429 above that.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sales_requests_dto** | [**SalesRequestsDto**](SalesRequestsDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.sales_requests_dto import SalesRequestsDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    sales_requests_dto = docspace_api_sdk.SalesRequestsDto() # SalesRequestsDto |  (optional)

    try:
        # Contact the sales team
        api_instance.send_payment_request(sales_requests_dto=sales_requests_dto)
    except Exception as e:
        print("Exception when calling PaymentApi->send_payment_request: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The message has been handed to the mail service; the response carries no content |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 1-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | `email` is not a well-formed address, or one of the required fields is empty |  -  |
**403** | The caller is not a DocSpace administrator |  -  |
**429** | This user has made more than ten requests in a minute |  * Retry-After - Seconds to wait before retrying (10 req / 1 min limit per user/IP). <br>  |
**401** | Unauthorized |  -  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_restricted_ai_models**
> RestrictedModelsResponseWrapper set_restricted_ai_models(set_restricted_ai_models_request_dto=set_restricted_ai_models_request_dto)

Replaces the whole set of AI chat models barred on this portal: the body is the complete set that is to hold,
so adding one restriction means sending the new model together with the ones already restricted, lifting one
means leaving it out, and an empty set lifts them all. Read the current set from
`GET api/2.0/portal/payment/ai-model/restrictions` and the model identifiers from
`GET api/2.0/portal/payment/ai-prices` before calling. The installation needs a billing service and the AI
gateway configured, the portal needs a billing customer, and the caller needs the permission to edit the
portal settings as well as DocSpace administrator rights. The call is mutating and idempotent - sending the
same set twice leaves the same state - and it is written to the portal audit trail. It takes effect on the
next AI request, so a conversation already open on a model that has just been barred cannot go on with it. The
stored set comes back in the answer.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **set_restricted_ai_models_request_dto** | [**SetRestrictedAiModelsRequestDto**](SetRestrictedAiModelsRequestDto.md)|  | [optional] 

### Return type

[**RestrictedModelsResponseWrapper**](RestrictedModelsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.restricted_models_response_wrapper import RestrictedModelsResponseWrapper
from docspace_api_sdk.models.set_restricted_ai_models_request_dto import SetRestrictedAiModelsRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    set_restricted_ai_models_request_dto = docspace_api_sdk.SetRestrictedAiModelsRequestDto() # SetRestrictedAiModelsRequestDto |  (optional)

    try:
        # Set restricted AI models
        api_response = api_instance.set_restricted_ai_models(set_restricted_ai_models_request_dto=set_restricted_ai_models_request_dto)
        print("The response of PaymentApi->set_restricted_ai_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->set_restricted_ai_models: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The set of barred AI chat models as it was stored |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller may not edit the portal settings or is not a DocSpace administrator, or the installation has no billing service or no AI gateway configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tenant_wallet_settings**
> TenantWalletSettingsResponseWrapper set_tenant_wallet_settings(tenant_wallet_settings_wrapper=tenant_wallet_settings_wrapper)

Switches the portal's automatic wallet top-up on or off and sets its thresholds: while it is on, the payment
method on file is charged whenever the wallet balance falls below `minBalance`, enough to bring it up to
`upToBalance`, in `currency`. The portal needs a billing customer whose wallet balance exists - a portal that
has never had one answers 404, so top the wallet up once with `POST api/2.0/portal/payment/deposit` first -
and only the payer may change the settings. The body replaces the stored settings as a whole and an omitted
body resets them to the defaults; `minBalance` is accepted between 5 and 1000 and `upToBalance` between 6 and
5000, while `lowBalanceThreshold` and `lowBalanceNotified` are ignored on the way in and kept as the portal
had them. The call is mutating and idempotent, it charges nothing by itself, it is written to the portal audit
trail, and switching the top-up on also re-arms the low-balance warning. The settings as they were stored come
back in the answer.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_wallet_settings_wrapper** | [**TenantWalletSettingsWrapper**](TenantWalletSettingsWrapper.md)|  | [optional] 

### Return type

[**TenantWalletSettingsResponseWrapper**](TenantWalletSettingsResponseWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.tenant_wallet_settings_response_wrapper import TenantWalletSettingsResponseWrapper
from docspace_api_sdk.models.tenant_wallet_settings_wrapper import TenantWalletSettingsWrapper
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    tenant_wallet_settings_wrapper = docspace_api_sdk.TenantWalletSettingsWrapper() # TenantWalletSettingsWrapper |  (optional)

    try:
        # Set the auto top-up settings
        api_response = api_instance.set_tenant_wallet_settings(tenant_wallet_settings_wrapper=tenant_wallet_settings_wrapper)
        print("The response of PaymentApi->set_tenant_wallet_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->set_tenant_wallet_settings: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The automatic top-up settings as they were stored |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not the payer of this portal, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer, or its wallet has no balance yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_customer_monthly_usage_report**
> terminate_customer_monthly_usage_report()

Stops the `xlsx` monthly usage report this user has running and drops its task, for a report that was started
for the wrong period or is no longer wanted. The portal needs a billing customer and the caller has to be a
DocSpace administrator. The stop is asked of the worker that builds the file rather than done here, so
`GET api/2.0/portal/payment/customer/usage/monthly/report` can still answer for a moment afterwards. The call
is safe to repeat and does nothing at all when this user has no such report running: there is no response
body, and status 200 says the stop was requested, not that a report was really stopped. It leaves the
operations and service usage reports alone, and a report that had already finished keeps its file in My
documents.

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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Terminate the monthly usage report
        api_instance.terminate_customer_monthly_usage_report()
    except Exception as e:
        print("Exception when calling PaymentApi->terminate_customer_monthly_usage_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stop has been requested; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_customer_operations_report**
> terminate_customer_operations_report()

Stops the `xlsx` wallet operations report this user has running and drops its task, for a report that was
started with the wrong filters or is no longer wanted. The portal needs a billing customer and the caller has
to be a DocSpace administrator. The stop is asked of the worker that builds the file rather than done here, so
`GET api/2.0/portal/payment/customer/operationsreport` can still answer for a moment afterwards. The call is
safe to repeat and does nothing at all when this user has no report running: there is no response body, and
status 200 says the stop was requested, not that a report was really stopped. A report that had already
finished keeps its file in My documents - nothing is deleted from there.

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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Terminate the operations report
        api_instance.terminate_customer_operations_report()
    except Exception as e:
        print("Exception when calling PaymentApi->terminate_customer_operations_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stop has been requested; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **terminate_customer_service_usage_report**
> terminate_customer_service_usage_report()

Stops the `xlsx` service usage report this user has running and drops its task, for a report that was started
with the wrong filters or is no longer wanted. The portal needs a billing customer and the caller has to be a
DocSpace administrator. The stop is asked of the worker that builds the file rather than done here, so
`GET api/2.0/portal/payment/customer/usage/report` can still answer for a moment afterwards. The call is safe
to repeat and does nothing at all when this user has no such report running: there is no response body, and
status 200 says the stop was requested, not that a report was really stopped. It leaves the operations and
monthly usage reports alone, and a report that had already finished keeps its file in My documents.

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
    api_instance = docspace_api_sdk.PaymentApi(api_client)

    try:
        # Terminate the service usage report
        api_instance.terminate_customer_service_usage_report()
    except Exception as e:
        print("Exception when calling PaymentApi->terminate_customer_service_usage_report: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The stop has been requested; the response carries no content |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **top_up_deposit**
> BooleanWrapper top_up_deposit(top_up_deposit_request_dto=top_up_deposit_request_dto)

Charges the payment method on file and adds the amount to the portal's wallet, the balance every wallet
service is paid from. The portal needs a billing customer with a payment method set - attach one with
`GET api/2.0/portal/payment/checkoutsetupurl` - `currency` has to be one of the accounting currencies this
installation supports, and `amount` is a whole number of currency units between 1 and 999999. Only the payer
may call it. The call takes money and is not idempotent in any way: two identical requests charge twice, so a
client must not retry it blindly after a timeout, and it is limited to ten requests a minute per user by
default. A successful top-up pushes the new balance to the portal clients over their socket connection and
re-arms the low-balance notification. The result is `true` when the payment provider accepted the charge; read
the resulting balance back from `GET api/2.0/portal/payment/customer/balance`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **top_up_deposit_request_dto** | [**TopUpDepositRequestDto**](TopUpDepositRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.top_up_deposit_request_dto import TopUpDepositRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    top_up_deposit_request_dto = docspace_api_sdk.TopUpDepositRequestDto() # TopUpDepositRequestDto |  (optional)

    try:
        # Top up the wallet
        api_response = api_instance.top_up_deposit(top_up_deposit_request_dto=top_up_deposit_request_dto)
        print("The response of PaymentApi->top_up_deposit:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->top_up_deposit: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | `true` when the payment provider accepted the charge and the wallet was credited |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 1-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | `currency` is not one of the supported accounting currencies, or `amount` is outside 1 to 999999 |  -  |
**403** | The caller is not the payer of this portal, the portal has no billing service configured, or the customer has no payment method set |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (10 req / 1 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_payment**
> BooleanWrapper update_payment(quantity_request_dto=quantity_request_dto)

Changes how many units of the plan the portal is paying for - the number of administrators it covers - and
lets the payment provider bill the difference against the payment method already on file. The portal must have
a billing customer and a plan bought through `PUT api/2.0/portal/payment/url`, and while the portal is on a
priced plan the product name in `quantity` has to be that same plan, which `GET api/2.0/portal/payment/quota`
reports, because a subscription is changed here and not swapped. Only the payer - the portal user whose e-mail
is the billing customer's e-mail - may call it. The call is mutating and charges money, and it is guarded
against a double submission: once the new quantity is in effect, repeating the same request fails with 400
because that quantity is already set. The result is `true` when the provider accepted the change and `false`
when it declined it without an error. Exactly one product per call is accepted, the operation is limited to
ten requests a minute per user by default and answers 429 above that, and wallet services are not bought here
- use `PUT api/2.0/portal/payment/updatewallet` for those.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **quantity_request_dto** | [**QuantityRequestDto**](QuantityRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.quantity_request_dto import QuantityRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    quantity_request_dto = docspace_api_sdk.QuantityRequestDto() # QuantityRequestDto |  (optional)

    try:
        # Change the subscription quantity
        api_response = api_instance.update_payment(quantity_request_dto=quantity_request_dto)
        print("The response of PaymentApi->update_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_payment: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | `true` when the provider accepted the new quantity, `false` when it declined it |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 1-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The product is not the plan currently paid, or the quantity is already the one in effect |  -  |
**403** | The caller is not the payer of this portal, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer yet |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (10 req / 1 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wallet_payment**
> BooleanWrapper update_wallet_payment(wallet_quantity_request_dto=wallet_quantity_request_dto)

Buys more units of a wallet service - extra administrators, disk storage, backup, AI tools, AI search or
DocsCloud - or writes down the quantity that service will have after the next renewal, depending on
`productQuantityType`. With `Add` (1) the units are bought at once and paid out of the portal wallet, so the
wallet needs a sub-account in the accounting currency and enough money on it; with `Set` (0) nothing is
charged now and the quantity only takes effect in the next period, where an empty or zero quantity cancels a
change scheduled earlier. `Renew` and `Sub` are not accepted here. The portal needs a billing customer and the
caller has to be a DocSpace administrator; a service that is an add-on to the plan also needs the plan itself
to be paid, otherwise the answer is 402. Minimum quantities apply - disk storage starts at 100 units, the
DocsCloud developer pack at 10, and the administrators may not be fewer than the portal already has - and in
the `Add` form they are checked only while the portal does not hold that service yet. Asking for the DocsCloud
plan in the `Set` form while the developer pack is active schedules the reversion to it at the next period,
while the upgrade in the other direction is not done here at all: use
`POST api/2.0/settings/docscloud/switchtodevpack`. The result is `true` when the change was accepted; the call
is mutating, spends money in its `Add` form and is limited to ten requests a minute per user by default. Price
the same purchase without paying for it with `PUT api/2.0/portal/payment/calculatewallet`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wallet_quantity_request_dto** | [**WalletQuantityRequestDto**](WalletQuantityRequestDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.boolean_wrapper import BooleanWrapper
from docspace_api_sdk.models.wallet_quantity_request_dto import WalletQuantityRequestDto
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
    api_instance = docspace_api_sdk.PaymentApi(api_client)
    wallet_quantity_request_dto = docspace_api_sdk.WalletQuantityRequestDto() # WalletQuantityRequestDto |  (optional)

    try:
        # Change a wallet service quantity
        api_response = api_instance.update_wallet_payment(wallet_quantity_request_dto=wallet_quantity_request_dto)
        print("The response of PaymentApi->update_wallet_payment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PaymentApi->update_wallet_payment: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | `true` when the purchase or the scheduled change was accepted, `false` when the provider declined it |  * X-RateLimit-Limit - Rate limit: 10 requests per 1 minutes per user/IP. <br>  * X-RateLimit-Remaining - Requests remaining in the current 1-minute window. <br>  * X-RateLimit-Reset -  <br>  |
**400** | The quantity type is not `Set` or `Add`, the product is not a wallet service, the quantity is below the minimum for it, or that service is already set |  -  |
**402** | The plan of the portal is not paid and the requested service is an add-on to it |  -  |
**403** | The caller is not a DocSpace administrator, or the portal has no billing service configured |  -  |
**404** | This portal has no billing customer, or its wallet has no sub-account in the accounting currency |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After - Seconds to wait before retrying (10 req / 1 min limit per user/IP). <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

