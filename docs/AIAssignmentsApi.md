# docspace_api_sdk.AssignmentsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_assignments_assign**](#ai_assignments_assign) | **PUT** /api/2.0/ai/assignments/assign | Assign
[**ai_assignments_bulk_assign**](#ai_assignments_bulk_assign) | **PUT** /api/2.0/ai/assignments/bulk-assign | Bulk assign
[**ai_assignments_cascade_profile_delete**](#ai_assignments_cascade_profile_delete) | **DELETE** /api/2.0/ai/assignments/cascade-profile-delete | Cascade profile delete
[**ai_assignments_get_all_assignments**](#ai_assignments_get_all_assignments) | **GET** /api/2.0/ai/assignments/get-all-assignments | Get all assignments
[**ai_assignments_get_assignment**](#ai_assignments_get_assignment) | **GET** /api/2.0/ai/assignments/get-assignment | Get assignment
[**ai_assignments_resolve_for_action**](#ai_assignments_resolve_for_action) | **GET** /api/2.0/ai/assignments/resolve-for-action | Resolve for action
[**ai_assignments_try_resolve_for_action**](#ai_assignments_try_resolve_for_action) | **GET** /api/2.0/ai/assignments/try-resolve-for-action | Try resolve for action
[**ai_assignments_unassign**](#ai_assignments_unassign) | **DELETE** /api/2.0/ai/assignments/unassign | Unassign


# **ai_assignments_assign**
> AiAssignmentMutationResult ai_assignments_assign(ai_assignments_assign_request)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_assignments_assign_request** | [**AiAssignmentsAssignRequest**](AiAssignmentsAssignRequest.md)|  | 

### Return type

[**AiAssignmentMutationResult**](AiAssignmentMutationResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_assignment_mutation_result import AiAssignmentMutationResult
from docspace_api_sdk.models.ai_assignments_assign_request import AiAssignmentsAssignRequest
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    ai_assignments_assign_request = docspace_api_sdk.AiAssignmentsAssignRequest() # AiAssignmentsAssignRequest | 

    try:
        # Assign
        api_response = api_instance.ai_assignments_assign(ai_assignments_assign_request)
        print("The response of AssignmentsApi->ai_assignments_assign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_assign: %s\n" % e)
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

# **ai_assignments_bulk_assign**
> AiBulkAssignmentResult ai_assignments_bulk_assign(request_body)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, str]**](str.md)|  | 

### Return type

[**AiBulkAssignmentResult**](AiBulkAssignmentResult.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_bulk_assignment_result import AiBulkAssignmentResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    request_body = {'key': 'request_body_example'} # Dict[str, str] | 

    try:
        # Bulk assign
        api_response = api_instance.ai_assignments_bulk_assign(request_body)
        print("The response of AssignmentsApi->ai_assignments_bulk_assign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_bulk_assign: %s\n" % e)
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

# **ai_assignments_cascade_profile_delete**
> AiSuccessResponse ai_assignments_cascade_profile_delete(body)



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
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Cascade profile delete
        api_response = api_instance.ai_assignments_cascade_profile_delete(body)
        print("The response of AssignmentsApi->ai_assignments_cascade_profile_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_cascade_profile_delete: %s\n" % e)
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

# **ai_assignments_get_all_assignments**
> Dict[str, str] ai_assignments_get_all_assignments(entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**|  | 

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    entity_id = 'entity_id_example' # str | 

    try:
        # Get all assignments
        api_response = api_instance.ai_assignments_get_all_assignments(entity_id)
        print("The response of AssignmentsApi->ai_assignments_get_all_assignments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_get_all_assignments: %s\n" % e)
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

# **ai_assignments_get_assignment**
> str ai_assignments_get_assignment(action_type)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    action_type = 'action_type_example' # str | 

    try:
        # Get assignment
        api_response = api_instance.ai_assignments_get_assignment(action_type)
        print("The response of AssignmentsApi->ai_assignments_get_assignment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_get_assignment: %s\n" % e)
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

# **ai_assignments_resolve_for_action**
> AiResolvedAssignment ai_assignments_resolve_for_action(action_type, entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**|  | 
 **entity_id** | **str**|  | 

### Return type

[**AiResolvedAssignment**](AiResolvedAssignment.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_resolved_assignment import AiResolvedAssignment
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    action_type = 'action_type_example' # str | 
    entity_id = 'entity_id_example' # str | 

    try:
        # Resolve for action
        api_response = api_instance.ai_assignments_resolve_for_action(action_type, entity_id)
        print("The response of AssignmentsApi->ai_assignments_resolve_for_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_resolve_for_action: %s\n" % e)
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

# **ai_assignments_try_resolve_for_action**
> AiResolvedAssignment ai_assignments_try_resolve_for_action(action_type, entity_id)



For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**|  | 
 **entity_id** | **str**|  | 

### Return type

[**AiResolvedAssignment**](AiResolvedAssignment.md)

### Authorization

No authorization required

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_resolved_assignment import AiResolvedAssignment
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    action_type = 'action_type_example' # str | 
    entity_id = 'entity_id_example' # str | 

    try:
        # Try resolve for action
        api_response = api_instance.ai_assignments_try_resolve_for_action(action_type, entity_id)
        print("The response of AssignmentsApi->ai_assignments_try_resolve_for_action:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_try_resolve_for_action: %s\n" % e)
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

# **ai_assignments_unassign**
> AiSuccessResponse ai_assignments_unassign(body)



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
from docspace_api_sdk.models.ai_action_type import AiActionType
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Unassign
        api_response = api_instance.ai_assignments_unassign(body)
        print("The response of AssignmentsApi->ai_assignments_unassign:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssignmentsApi->ai_assignments_unassign: %s\n" % e)
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

