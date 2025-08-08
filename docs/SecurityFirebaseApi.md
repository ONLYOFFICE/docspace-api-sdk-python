# docspace_api_sdk.FirebaseApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**doc_register_pusn_notification_device**](#doc_register_pusn_notification_device) | **POST** /api/2.0/settings/push/docregisterdevice | Save the Documents Firebase device token
[**subscribe_documents_push_notification**](#subscribe_documents_push_notification) | **PUT** /api/2.0/settings/push/docsubscribe | Subscribe to Documents push notification


# **doc_register_pusn_notification_device**
> FireBaseUserWrapper doc_register_pusn_notification_device(firebase_requests_dto=firebase_requests_dto)

Saves the Firebase device token specified in the request for the Documents application.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firebase_requests_dto** | [**FirebaseRequestsDto**](FirebaseRequestsDto.md)|  | [optional] 

### Return type

[**FireBaseUserWrapper**](FireBaseUserWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.fire_base_user_wrapper import FireBaseUserWrapper
from docspace_api_sdk.models.firebase_requests_dto import FirebaseRequestsDto
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
    api_instance = docspace_api_sdk.FirebaseApi(api_client)
    firebase_requests_dto = docspace_api_sdk.FirebaseRequestsDto() # FirebaseRequestsDto |  (optional)

    try:
        # Save the Documents Firebase device token
        api_response = api_instance.doc_register_pusn_notification_device(firebase_requests_dto=firebase_requests_dto)
        print("The response of FirebaseApi->doc_register_pusn_notification_device:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirebaseApi->doc_register_pusn_notification_device: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FireBase user |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **subscribe_documents_push_notification**
> FireBaseUserWrapper subscribe_documents_push_notification(firebase_requests_dto=firebase_requests_dto)

Subscribes to the Documents push notification.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **firebase_requests_dto** | [**FirebaseRequestsDto**](FirebaseRequestsDto.md)|  | [optional] 

### Return type

[**FireBaseUserWrapper**](FireBaseUserWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.fire_base_user_wrapper import FireBaseUserWrapper
from docspace_api_sdk.models.firebase_requests_dto import FirebaseRequestsDto
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
    api_instance = docspace_api_sdk.FirebaseApi(api_client)
    firebase_requests_dto = docspace_api_sdk.FirebaseRequestsDto() # FirebaseRequestsDto |  (optional)

    try:
        # Subscribe to Documents push notification
        api_response = api_instance.subscribe_documents_push_notification(firebase_requests_dto=firebase_requests_dto)
        print("The response of FirebaseApi->subscribe_documents_push_notification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FirebaseApi->subscribe_documents_push_notification: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | FireBase user |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

