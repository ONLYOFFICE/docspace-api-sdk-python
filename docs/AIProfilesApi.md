# docspace_api_sdk.ProfilesApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_profiles_create**](#ai_profiles_create) | **POST** /api/2.0/ai/profiles/create | Create
[**ai_profiles_delete**](#ai_profiles_delete) | **DELETE** /api/2.0/ai/profiles/delete | Delete
[**ai_profiles_get_by_id**](#ai_profiles_get_by_id) | **GET** /api/2.0/ai/profiles/get-by-id | Get by id
[**ai_profiles_list**](#ai_profiles_list) | **GET** /api/2.0/ai/profiles/list | List
[**ai_profiles_list_models**](#ai_profiles_list_models) | **GET** /api/2.0/ai/profiles/list-models | List models
[**ai_profiles_list_provider_models**](#ai_profiles_list_provider_models) | **POST** /api/2.0/ai/profiles/list-provider-models | List provider models
[**ai_profiles_test_connection**](#ai_profiles_test_connection) | **POST** /api/2.0/ai/profiles/test-connection | Test connection
[**ai_profiles_update**](#ai_profiles_update) | **PUT** /api/2.0/ai/profiles/update | Update


# **ai_profiles_create**
> AiProfileMutationResult ai_profiles_create(ai_create_profile_input)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_create_profile_input** | [**AiCreateProfileInput**](AiCreateProfileInput.md)|  | 

### Return type

[**AiProfileMutationResult**](AiProfileMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_create_profile_input import AiCreateProfileInput
from docspace_api_sdk.models.ai_profile_mutation_result import AiProfileMutationResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    ai_create_profile_input = docspace_api_sdk.AiCreateProfileInput() # AiCreateProfileInput | 

    try:
        # Create
        api_response = api_instance.ai_profiles_create(ai_create_profile_input)
        print("The response of ProfilesApi->ai_profiles_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_create: %s\n" % e)
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

# **ai_profiles_delete**
> AiSuccessResponse ai_profiles_delete(body)



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
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    body = 'body_example' # str | 

    try:
        # Delete
        api_response = api_instance.ai_profiles_delete(body)
        print("The response of ProfilesApi->ai_profiles_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_delete: %s\n" % e)
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

# **ai_profiles_get_by_id**
> AiProfilesGetById200Response ai_profiles_get_by_id(id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**AiProfilesGetById200Response**](AiProfilesGetById200Response.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_profiles_get_by_id200_response import AiProfilesGetById200Response
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get by id
        api_response = api_instance.ai_profiles_get_by_id(id)
        print("The response of ProfilesApi->ai_profiles_get_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_get_by_id: %s\n" % e)
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

# **ai_profiles_list**
> List[AiProfile] ai_profiles_list()



For more information, see [api.onlyoffice.com]().

### Parameters

This endpoint does not need any parameter.

### Return type

[**List[AiProfile]**](AiProfile.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_profile import AiProfile
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)

    try:
        # List
        api_response = api_instance.ai_profiles_list()
        print("The response of ProfilesApi->ai_profiles_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_list: %s\n" % e)
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

# **ai_profiles_list_models**
> List[AiModel] ai_profiles_list_models(profile_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**List[AiModel]**](AiModel.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_model import AiModel
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # List models
        api_response = api_instance.ai_profiles_list_models(profile_id)
        print("The response of ProfilesApi->ai_profiles_list_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_list_models: %s\n" % e)
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

# **ai_profiles_list_provider_models**
> List[AiModel] ai_profiles_list_provider_models(ai_profiles_list_provider_models_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_profiles_list_provider_models_request** | [**AiProfilesListProviderModelsRequest**](AiProfilesListProviderModelsRequest.md)|  | 

### Return type

[**List[AiModel]**](AiModel.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_model import AiModel
from docspace_api_sdk.models.ai_profiles_list_provider_models_request import AiProfilesListProviderModelsRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    ai_profiles_list_provider_models_request = docspace_api_sdk.AiProfilesListProviderModelsRequest() # AiProfilesListProviderModelsRequest | 

    try:
        # List provider models
        api_response = api_instance.ai_profiles_list_provider_models(ai_profiles_list_provider_models_request)
        print("The response of ProfilesApi->ai_profiles_list_provider_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_list_provider_models: %s\n" % e)
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

# **ai_profiles_test_connection**
> AiProfilesTestConnection200Response ai_profiles_test_connection(body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiProfilesTestConnection200Response**](AiProfilesTestConnection200Response.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_profiles_test_connection200_response import AiProfilesTestConnection200Response
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    body = 'body_example' # str | 

    try:
        # Test connection
        api_response = api_instance.ai_profiles_test_connection(body)
        print("The response of ProfilesApi->ai_profiles_test_connection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_test_connection: %s\n" % e)
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

# **ai_profiles_update**
> AiProfileMutationResult ai_profiles_update(ai_profile)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_profile** | [**AiProfile**](AiProfile.md)|  | 

### Return type

[**AiProfileMutationResult**](AiProfileMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_profile import AiProfile
from docspace_api_sdk.models.ai_profile_mutation_result import AiProfileMutationResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.ProfilesApi(api_client)
    ai_profile = docspace_api_sdk.AiProfile() # AiProfile | 

    try:
        # Update
        api_response = api_instance.ai_profiles_update(ai_profile)
        print("The response of ProfilesApi->ai_profiles_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfilesApi->ai_profiles_update: %s\n" % e)
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

