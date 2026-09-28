# docspace_api_sdk.AssignmentsApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ai_assignments_assign**](#ai_assignments_assign) | **PUT** /api/2.0/ai/assignments/assign | Bind a profile to an action
[**ai_assignments_bulk_assign**](#ai_assignments_bulk_assign) | **PUT** /api/2.0/ai/assignments/bulk-assign | Bulk assign
[**ai_assignments_cascade_profile_delete**](#ai_assignments_cascade_profile_delete) | **DELETE** /api/2.0/ai/assignments/cascade-profile-delete | Cascade profile delete
[**ai_assignments_get_all_assignments**](#ai_assignments_get_all_assignments) | **GET** /api/2.0/ai/assignments/get-all-assignments | Get all assignments
[**ai_assignments_get_assignment**](#ai_assignments_get_assignment) | **GET** /api/2.0/ai/assignments/get-assignment | Get assignment
[**ai_assignments_resolve_for_action**](#ai_assignments_resolve_for_action) | **GET** /api/2.0/ai/assignments/resolve-for-action | Resolve for action
[**ai_assignments_try_resolve_for_action**](#ai_assignments_try_resolve_for_action) | **GET** /api/2.0/ai/assignments/try-resolve-for-action | Try resolve for action
[**ai_assignments_unassign**](#ai_assignments_unassign) | **DELETE** /api/2.0/ai/assignments/unassign | Clear an action's profile


# **ai_assignments_assign**
> AiAssignmentMutationResult ai_assignments_assign(ai_assignments_assign_request)

Binds a profile to one AI action portal-wide, creating the assignment or replacing it in place, and returns the result. Both `actionType` and `profileId` are required. The profile's declared capabilities are checked against the action, so a model that cannot generate images cannot be bound to `ImageGeneration` - the `Default` slot is exempt, because it stands in for every action. There is no room-scoped form of this write: a room's own binding is created by the agent that owns it, while reads accept an `entityId`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_assignments_assign_request** | [**AiAssignmentsAssignRequest**](AiAssignmentsAssignRequest.md)|  | 

### Return type

[**AiAssignmentMutationResult**](AiAssignmentMutationResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    ai_assignments_assign_request = docspace_api_sdk.AiAssignmentsAssignRequest() # AiAssignmentsAssignRequest | 

    try:
        # Bind a profile to an action
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
**200** | Whether the binding was stored. A failure is reported in `error` rather than as a status. |  -  |
**400** | `actionType` or `profileId` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_bulk_assign**
> AiBulkAssignmentResult ai_assignments_bulk_assign(request_body)

Applies many action-to-profile bindings in one write, which is how a settings screen saves the whole set. The body is a plain map of action type to profile ID, and every entry is validated before anything is written: one unknown action or one non-string profile ID rejects the request whole, so the set is never left half-applied. Each entry behaves as the single assign operation does, capability checks included. The answer carries the resulting assignment set.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, str]**](str.md)| A map of action type to profile ID. Every key has to be a known action type and every value a profile ID; one bad entry rejects the whole map. | 

### Return type

[**AiBulkAssignmentResult**](AiBulkAssignmentResult.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_bulk_assignment_result import AiBulkAssignmentResult
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    request_body = {'key': 'request_body_example'} # Dict[str, str] | A map of action type to profile ID. Every key has to be a known action type and every value a profile ID; one bad entry rejects the whole map.

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
**200** | Whether the set was stored, with `errors` listing the entries that were refused. |  -  |
**400** | The body is not a map of action type to profile ID, or one of its keys is not a known action type. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_cascade_profile_delete**
> AiSuccessResponse ai_assignments_cascade_profile_delete(ai_assignments_cascade_profile_delete_request)

Detaches a profile from every assignment that points at it, which is the cleanup step before the profile itself is removed. The `Default` slot is promoted to the first remaining profile, or dropped when none is left, and every other slot holding the profile is cleared. `profileId` is required and may be sent in the body or as a query parameter. `DELETE api/2.0/ai/profiles/delete` already does this, so call it directly only when the profile is being removed by some other means.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ai_assignments_cascade_profile_delete_request** | [**AiAssignmentsCascadeProfileDeleteRequest**](AiAssignmentsCascadeProfileDeleteRequest.md)| The profile to detach from every assignment. May be sent as the `profileId` query parameter instead of in the body. | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_assignments_cascade_profile_delete_request import AiAssignmentsCascadeProfileDeleteRequest
from docspace_api_sdk.models.ai_success_response import AiSuccessResponse
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    ai_assignments_cascade_profile_delete_request = docspace_api_sdk.AiAssignmentsCascadeProfileDeleteRequest() # AiAssignmentsCascadeProfileDeleteRequest | The profile to detach from every assignment. May be sent as the `profileId` query parameter instead of in the body.

    try:
        # Cascade profile delete
        api_response = api_instance.ai_assignments_cascade_profile_delete(ai_assignments_cascade_profile_delete_request)
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
**200** | Confirms no assignment points at the profile any more. |  -  |
**400** | `profileId` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_get_all_assignments**
> Dict[str, str] ai_assignments_get_all_assignments(entity_id=entity_id)

Returns every action-to-profile binding of a scope as one map, which is what a settings screen loads. `entityId` narrows it to a room and has to name one the caller can open; a room that is not an agent room degrades to the portal-wide set rather than answering empty, and omitting the parameter reads the portal-wide set directly. Actions with no binding are simply absent from the map. The `Default` slot is reported as an entry of its own rather than being folded into the others.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

**Dict[str, str]**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Get all assignments
        api_response = api_instance.ai_assignments_get_all_assignments(entity_id=entity_id)
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
**200** | The scope's bindings as a map of action type to profile ID. An action with no binding is absent. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**404** | The referenced object does not exist, or the caller cannot access it - the two are deliberately indistinguishable, so a room the caller may not open answers 404 rather than 403. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_get_assignment**
> str ai_assignments_get_assignment(action_type)

Returns the profile bound to one AI action, without applying the `Default` fallback - an empty answer means this action has no profile of its own, not that nothing is configured. `actionType` is required and is read from the query. Use `GET api/2.0/ai/assignments/resolve-for-action` to learn which profile would actually serve the action. This reads the portal-wide binding and accepts no `entityId`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**| The AI action the request applies to - one of Default, Chat, Code, Summarization, Translation, TextAnalyze, ImageGeneration, OCR, Vision, FormAnalysis. | 

### Return type

**str**

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    action_type = 'Chat' # str | The AI action the request applies to - one of Default, Chat, Code, Summarization, Translation, TextAnalyze, ImageGeneration, OCR, Vision, FormAnalysis.

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
**200** | The profile bound to the action, or an empty result when it has none of its own. |  -  |
**400** | `actionType` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_resolve_for_action**
> AiResolvedAssignment ai_assignments_resolve_for_action(action_type, entity_id=entity_id)

Returns the profile that will serve one AI action, falling back to the `Default` slot when the action has no profile of its own. `actionType` is required and has to be one of the known actions - an unknown or misspelled value is rejected rather than resolved to the default. `entityId` narrows the lookup to a room, and a room with no assignment of its own degrades to the portal-wide one. This fails when neither slot is set or the bound profile is gone, so use `GET api/2.0/ai/assignments/try-resolve-for-action` when an unconfigured portal should answer empty instead.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**| The AI action the request applies to - one of Default, Chat, Code, Summarization, Translation, TextAnalyze, ImageGeneration, OCR, Vision, FormAnalysis. | 
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

[**AiResolvedAssignment**](AiResolvedAssignment.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_resolved_assignment import AiResolvedAssignment
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    action_type = 'Chat' # str | The AI action the request applies to - one of Default, Chat, Code, Summarization, Translation, TextAnalyze, ImageGeneration, OCR, Vision, FormAnalysis.
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Resolve for action
        api_response = api_instance.ai_assignments_resolve_for_action(action_type, entity_id=entity_id)
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
**200** | The profile that will serve the action. |  -  |
**400** | `actionType` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_try_resolve_for_action**
> AiResolvedAssignment ai_assignments_try_resolve_for_action(action_type, entity_id=entity_id)

Returns the profile that will serve one AI action, exactly as `GET api/2.0/ai/assignments/resolve-for-action` does, but answers with an empty result rather than failing when nothing is configured. `actionType` is required and is validated the same way, and `entityId` narrows the lookup to a room. This is the operation to call when the absence of a profile is a normal state to render - a settings screen, or a feature that hides itself. Both operations are read-only.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action_type** | **str**| The AI action the request applies to - one of Default, Chat, Code, Summarization, Translation, TextAnalyze, ImageGeneration, OCR, Vision, FormAnalysis. | 
 **entity_id** | **str**| The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. | [optional] 

### Return type

[**AiResolvedAssignment**](AiResolvedAssignment.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.ai_resolved_assignment import AiResolvedAssignment
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    action_type = 'Chat' # str | The AI action the request applies to - one of Default, Chat, Code, Summarization, Translation, TextAnalyze, ImageGeneration, OCR, Vision, FormAnalysis.
    entity_id = '1234' # str | The DocSpace entity the request is scoped to - the room, folder or agent workspace the chat is invoked from. Omit for the portal-wide scope. (optional)

    try:
        # Try resolve for action
        api_response = api_instance.ai_assignments_try_resolve_for_action(action_type, entity_id=entity_id)
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
**200** | The profile that will serve the action, or an empty result when none is configured. |  -  |
**400** | `actionType` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **ai_assignments_unassign**
> AiSuccessResponse ai_assignments_unassign(body)

Clears the portal-wide binding of one AI action, after which the action falls back to the `Default` slot. `actionType` is required and may be sent in the body or as a query parameter. An action whose slot is already empty is not reported as an error - the call answers success either way, so it is safe to repeat. Clearing `Default` itself leaves the actions that relied on it unresolvable.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **str**|  | 

### Return type

[**AiSuccessResponse**](AiSuccessResponse.md)

### Authorization

[cookieAuth](../README.md#cookieAuth), [bearerAuth](../README.md#bearerAuth)

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

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: bearerAuth
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)
# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.AssignmentsApi(api_client)
    body = 'body_example' # str | 

    try:
        # Clear an action's profile
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
**200** | Confirms the action now has no profile of its own. |  -  |
**400** | `actionType` is missing. |  -  |
**401** | Missing `asc_auth_key` cookie or `Authorization` header. |  -  |
**403** | AI is disabled for this portal, or the caller is a guest. Relayed from the DocSpace AI service. |  -  |
**413** | The request body is larger than 100 KB, the JSON parser's limit on this route. |  -  |
**500** | Unhandled failure. The reason is logged server-side and never echoed back. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

