# docspace.GroupRoomsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups_with_shared**](GroupRoomsApi.md#get_groups_with_shared) | **GET** /api/2.0/group/room/{id} | Gets groups with shared


# **get_groups_with_shared**
> GroupArrayWrapper get_groups_with_shared(id, exclude_shared=exclude_shared)

Gets groups with shared

Gets groups with shared

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.group_array_wrapper import GroupArrayWrapper
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
    api_instance = docspace.GroupRoomsApi(api_client)
    id = 9846 # int | ID
    exclude_shared = true # bool | Exclude shared (optional)

    try:
        # Gets groups with shared
        api_response = api_instance.get_groups_with_shared(id, exclude_shared=exclude_shared)
        print("The response of GroupRoomsApi->get_groups_with_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRoomsApi->get_groups_with_shared: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| ID | 
 **exclude_shared** | **bool**| Exclude shared | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ok |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

