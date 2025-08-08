# docspace_api_sdk.ThirdPartyIntegrationApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_third_party**](#delete_third_party) | **DELETE** /api/2.0/files/thirdparty/{providerId} | 
[**get_all_providers**](#get_all_providers) | **GET** /api/2.0/files/thirdparty/providers | 
[**get_backup_third_party_account**](#get_backup_third_party_account) | **GET** /api/2.0/files/thirdparty/backup | 
[**get_capabilities**](#get_capabilities) | **GET** /api/2.0/files/thirdparty/capabilities | 
[**get_common_third_party_folders**](#get_common_third_party_folders) | **GET** /api/2.0/files/thirdparty/common | 
[**get_third_party_accounts**](#get_third_party_accounts) | **GET** /api/2.0/files/thirdparty | 
[**save_third_party**](#save_third_party) | **POST** /api/2.0/files/thirdparty | 
[**save_third_party_backup**](#save_third_party_backup) | **POST** /api/2.0/files/thirdparty/backup | 


# **delete_third_party**
> StringWrapper delete_third_party(provider_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider_id** | **int**| The provider ID. | 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.string_wrapper import StringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)
    provider_id = 1234 # int | The provider ID.

    try:
        api_response = api_instance.delete_third_party(provider_id)
        print("The response of ThirdPartyIntegrationApi->delete_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->delete_third_party: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Third-party folder ID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_providers**
> ProviderArrayWrapper get_all_providers()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ProviderArrayWrapper**](ProviderArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.provider_array_wrapper import ProviderArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)

    try:
        api_response = api_instance.get_all_providers()
        print("The response of ThirdPartyIntegrationApi->get_all_providers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->get_all_providers: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of provider |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_backup_third_party_account**
> FolderStringWrapper get_backup_third_party_account()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**FolderStringWrapper**](FolderStringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_string_wrapper import FolderStringWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)

    try:
        api_response = api_instance.get_backup_third_party_account()
        print("The response of ThirdPartyIntegrationApi->get_backup_third_party_account:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->get_backup_third_party_account: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder for the third-party account backup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_capabilities**
> ArrayArrayWrapper get_capabilities()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ArrayArrayWrapper**](ArrayArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.array_array_wrapper import ArrayArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)

    try:
        api_response = api_instance.get_capabilities()
        print("The response of ThirdPartyIntegrationApi->get_capabilities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->get_capabilities: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of provider keys |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_common_third_party_folders**
> FolderStringArrayWrapper get_common_third_party_folders()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**FolderStringArrayWrapper**](FolderStringArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_string_array_wrapper import FolderStringArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)

    try:
        api_response = api_instance.get_common_third_party_folders()
        print("The response of ThirdPartyIntegrationApi->get_common_third_party_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->get_common_third_party_folders: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of common third-party folderst |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_third_party_accounts**
> ThirdPartyParamsArrayWrapper get_third_party_accounts()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**ThirdPartyParamsArrayWrapper**](ThirdPartyParamsArrayWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.third_party_params_array_wrapper import ThirdPartyParamsArrayWrapper
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)

    try:
        api_response = api_instance.get_third_party_accounts()
        print("The response of ThirdPartyIntegrationApi->get_third_party_accounts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->get_third_party_accounts: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of connected providers information |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_third_party**
> FolderStringWrapper save_third_party(third_party_request_dto=third_party_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_request_dto** | [**ThirdPartyRequestDto**](ThirdPartyRequestDto.md)|  | [optional] 

### Return type

[**FolderStringWrapper**](FolderStringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_string_wrapper import FolderStringWrapper
from docspace_api_sdk.models.third_party_request_dto import ThirdPartyRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)
    third_party_request_dto = docspace_api_sdk.ThirdPartyRequestDto() # ThirdPartyRequestDto |  (optional)

    try:
        api_response = api_instance.save_third_party(third_party_request_dto=third_party_request_dto)
        print("The response of ThirdPartyIntegrationApi->save_third_party:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->save_third_party: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Connected provider folder |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_third_party_backup**
> FolderStringWrapper save_third_party_backup(third_party_backup_request_dto=third_party_backup_request_dto)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **third_party_backup_request_dto** | [**ThirdPartyBackupRequestDto**](ThirdPartyBackupRequestDto.md)|  | [optional] 

### Return type

[**FolderStringWrapper**](FolderStringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.folder_string_wrapper import FolderStringWrapper
from docspace_api_sdk.models.third_party_backup_request_dto import ThirdPartyBackupRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)


# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ThirdPartyIntegrationApi(api_client)
    third_party_backup_request_dto = docspace_api_sdk.ThirdPartyBackupRequestDto() # ThirdPartyBackupRequestDto |  (optional)

    try:
        api_response = api_instance.save_third_party_backup(third_party_backup_request_dto=third_party_backup_request_dto)
        print("The response of ThirdPartyIntegrationApi->save_third_party_backup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ThirdPartyIntegrationApi->save_third_party_backup: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Folder for the third-party account backup |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

