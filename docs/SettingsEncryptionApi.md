# docspace.SettingsEncryptionApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_storage_encryption_progress**](SettingsEncryptionApi.md#get_storage_encryption_progress) | **GET** /api/2.0/settings/encryption/progress | Get the storage encryption progress
[**start_storage_encryption**](SettingsEncryptionApi.md#start_storage_encryption) | **POST** /api/2.0/settings/encryption/start | Start the storage encryption process


# **get_storage_encryption_progress**
> DoubleWrapper get_storage_encryption_progress()

Get the storage encryption progress

Returns the storage encryption progress.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.double_wrapper import DoubleWrapper
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
    api_instance = docspace.SettingsEncryptionApi(api_client)

    try:
        # Get the storage encryption progress
        api_response = api_instance.get_storage_encryption_progress()
        print("The response of SettingsEncryptionApi->get_storage_encryption_progress:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsEncryptionApi->get_storage_encryption_progress: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**DoubleWrapper**](DoubleWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Storage encryption progress |  -  |
**401** | Unauthorized |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_storage_encryption**
> BooleanWrapper start_storage_encryption(storage_encryption_requests_dto=storage_encryption_requests_dto)

Start the storage encryption process

Starts the storage encryption process.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.boolean_wrapper import BooleanWrapper
from docspace.models.storage_encryption_requests_dto import StorageEncryptionRequestsDto
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
    api_instance = docspace.SettingsEncryptionApi(api_client)
    storage_encryption_requests_dto = docspace.StorageEncryptionRequestsDto() # StorageEncryptionRequestsDto |  (optional)

    try:
        # Start the storage encryption process
        api_response = api_instance.start_storage_encryption(storage_encryption_requests_dto=storage_encryption_requests_dto)
        print("The response of SettingsEncryptionApi->start_storage_encryption:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsEncryptionApi->start_storage_encryption: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **storage_encryption_requests_dto** | [**StorageEncryptionRequestsDto**](StorageEncryptionRequestsDto.md)|  | [optional] 

### Return type

[**BooleanWrapper**](BooleanWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Boolean value: true if the operation is successful |  -  |
**401** | Unauthorized |  -  |
**402** | Your pricing plan does not support this option |  -  |
**403** | No permissions to perform this action |  -  |
**405** | Method not allowed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

