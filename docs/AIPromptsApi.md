# docspace_api_sdk.PromptsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_prompts_create**](#ai_prompts_create) | **POST** /api/2.0/ai/prompts/create | Create
[**ai_prompts_create_folder**](#ai_prompts_create_folder) | **POST** /api/2.0/ai/prompts/create-folder | Create folder
[**ai_prompts_delete**](#ai_prompts_delete) | **DELETE** /api/2.0/ai/prompts/delete | Delete
[**ai_prompts_delete_folder**](#ai_prompts_delete_folder) | **DELETE** /api/2.0/ai/prompts/delete-folder | Delete folder
[**ai_prompts_export**](#ai_prompts_export) | **GET** /api/2.0/ai/prompts/export | Export
[**ai_prompts_get_by_id**](#ai_prompts_get_by_id) | **GET** /api/2.0/ai/prompts/get-by-id | Get by id
[**ai_prompts_get_folder_by_id**](#ai_prompts_get_folder_by_id) | **GET** /api/2.0/ai/prompts/get-folder-by-id | Get folder by id
[**ai_prompts_import_bundle**](#ai_prompts_import_bundle) | **POST** /api/2.0/ai/prompts/import-bundle | Import bundle
[**ai_prompts_list**](#ai_prompts_list) | **GET** /api/2.0/ai/prompts/list | List
[**ai_prompts_list_folders**](#ai_prompts_list_folders) | **GET** /api/2.0/ai/prompts/list-folders | List folders
[**ai_prompts_move**](#ai_prompts_move) | **PUT** /api/2.0/ai/prompts/move | Move
[**ai_prompts_rename_folder**](#ai_prompts_rename_folder) | **PUT** /api/2.0/ai/prompts/rename-folder | Rename folder
[**ai_prompts_update**](#ai_prompts_update) | **PUT** /api/2.0/ai/prompts/update | Update


# **ai_prompts_create**
> AiPromptMutationResult ai_prompts_create(ai_create_prompt_input)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_create_prompt_input** | [**AiCreatePromptInput**](AiCreatePromptInput.md)|  | 

### Return type

[**AiPromptMutationResult**](AiPromptMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_create_prompt_input import AiCreatePromptInput
from docspace_api_sdk.models.ai_prompt_mutation_result import AiPromptMutationResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    ai_create_prompt_input = docspace_api_sdk.AiCreatePromptInput() # AiCreatePromptInput | 

    try:
        # Create
        api_response = api_instance.ai_prompts_create(ai_create_prompt_input)
        print("The response of PromptsApi->ai_prompts_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_create: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_create_folder**
> AiFolderMutationResult ai_prompts_create_folder(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiFolderMutationResult**](AiFolderMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_folder_mutation_result import AiFolderMutationResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Create folder
        api_response = api_instance.ai_prompts_create_folder(body)
        print("The response of PromptsApi->ai_prompts_create_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_create_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_delete**
> AiSuccessResponse ai_prompts_delete(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Delete
        api_response = api_instance.ai_prompts_delete(body)
        print("The response of PromptsApi->ai_prompts_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_delete: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_delete_folder**
> AiSuccessResponse ai_prompts_delete_folder(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Delete folder
        api_response = api_instance.ai_prompts_delete_folder(body)
        print("The response of PromptsApi->ai_prompts_delete_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_delete_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_export**
> AiPromptBundle ai_prompts_export()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**AiPromptBundle**](AiPromptBundle.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt_bundle import AiPromptBundle
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)

    try:
        # Export
        api_response = api_instance.ai_prompts_export()
        print("The response of PromptsApi->ai_prompts_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_export: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_get_by_id**
> AiPrompt ai_prompts_get_by_id(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AiPrompt**](AiPrompt.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt import AiPrompt
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get by id
        api_response = api_instance.ai_prompts_get_by_id(id)
        print("The response of PromptsApi->ai_prompts_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_get_by_id: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_get_folder_by_id**
> AiPromptFolder ai_prompts_get_folder_by_id(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AiPromptFolder**](AiPromptFolder.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt_folder import AiPromptFolder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get folder by id
        api_response = api_instance.ai_prompts_get_folder_by_id(id)
        print("The response of PromptsApi->ai_prompts_get_folder_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_get_folder_by_id: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_import_bundle**
> AiImportResult ai_prompts_import_bundle(ai_prompts_import_bundle_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_prompts_import_bundle_request** | [**AiPromptsImportBundleRequest**](AiPromptsImportBundleRequest.md)|  | 

### Return type

[**AiImportResult**](AiImportResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_import_result import AiImportResult
from docspace_api_sdk.models.ai_prompts_import_bundle_request import AiPromptsImportBundleRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    ai_prompts_import_bundle_request = docspace_api_sdk.AiPromptsImportBundleRequest() # AiPromptsImportBundleRequest | 

    try:
        # Import bundle
        api_response = api_instance.ai_prompts_import_bundle(ai_prompts_import_bundle_request)
        print("The response of PromptsApi->ai_prompts_import_bundle:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_import_bundle: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_list**
> List[AiPrompt] ai_prompts_list(folder_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

### Return type

[**List[AiPrompt]**](AiPrompt.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt import AiPrompt
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    folder_id = 'folder_id_example' # str | 

    try:
        # List
        api_response = api_instance.ai_prompts_list(folder_id)
        print("The response of PromptsApi->ai_prompts_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_list: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_list_folders**
> List[AiPromptFolder] ai_prompts_list_folders()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AiPromptFolder]**](AiPromptFolder.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt_folder import AiPromptFolder
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)

    try:
        # List folders
        api_response = api_instance.ai_prompts_list_folders()
        print("The response of PromptsApi->ai_prompts_list_folders:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_list_folders: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_move**
> AiPromptMutationResult ai_prompts_move(ai_prompts_move_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_prompts_move_request** | [**AiPromptsMoveRequest**](AiPromptsMoveRequest.md)|  | 

### Return type

[**AiPromptMutationResult**](AiPromptMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt_mutation_result import AiPromptMutationResult
from docspace_api_sdk.models.ai_prompts_move_request import AiPromptsMoveRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    ai_prompts_move_request = docspace_api_sdk.AiPromptsMoveRequest() # AiPromptsMoveRequest | 

    try:
        # Move
        api_response = api_instance.ai_prompts_move(ai_prompts_move_request)
        print("The response of PromptsApi->ai_prompts_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_move: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_rename_folder**
> AiFolderMutationResult ai_prompts_rename_folder(ai_prompts_rename_folder_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_prompts_rename_folder_request** | [**AiPromptsRenameFolderRequest**](AiPromptsRenameFolderRequest.md)|  | 

### Return type

[**AiFolderMutationResult**](AiFolderMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_folder_mutation_result import AiFolderMutationResult
from docspace_api_sdk.models.ai_prompts_rename_folder_request import AiPromptsRenameFolderRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    ai_prompts_rename_folder_request = docspace_api_sdk.AiPromptsRenameFolderRequest() # AiPromptsRenameFolderRequest | 

    try:
        # Rename folder
        api_response = api_instance.ai_prompts_rename_folder(ai_prompts_rename_folder_request)
        print("The response of PromptsApi->ai_prompts_rename_folder:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_rename_folder: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_prompts_update**
> AiPromptMutationResult ai_prompts_update(ai_prompts_update_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_prompts_update_request** | [**AiPromptsUpdateRequest**](AiPromptsUpdateRequest.md)|  | 

### Return type

[**AiPromptMutationResult**](AiPromptMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_prompt_mutation_result import AiPromptMutationResult
from docspace_api_sdk.models.ai_prompts_update_request import AiPromptsUpdateRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.PromptsApi(api_client)
    ai_prompts_update_request = docspace_api_sdk.AiPromptsUpdateRequest() # AiPromptsUpdateRequest | 

    try:
        # Update
        api_response = api_instance.ai_prompts_update(ai_prompts_update_request)
        print("The response of PromptsApi->ai_prompts_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PromptsApi->ai_prompts_update: %s\n" % e)
```


### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

