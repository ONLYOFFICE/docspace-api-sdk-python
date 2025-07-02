# docspace-api-python.GroupRoomsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_groups_with_shared**](#get_groups_with_shared) | **GET** /api/2.0/group/room/{id} | Get groups with sharing settings


# **get_groups_with_shared**
> GroupArrayWrapper get_groups_with_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)

Returns groups with their sharing settings.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The group ID. | 
 **exclude_shared** | **bool**| Specifies whether to exclude the group sharing settings from the response. | [optional] 
 **count** | **int**| The number of groups to retrieve in the request. | [optional] 
 **start_index** | **int**| The starting index from which to begin retrieving groups with their sharing settings. | [optional] 
 **filter_value** | **str**| The text used as a filter for retrieving groups with their sharing settings. | [optional] 

### Return type

[**GroupArrayWrapper**](GroupArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.group_array_wrapper import GroupArrayWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace-api-python.Configuration(
    username = os.environ["USERNAME"],
    password = os.environ["PASSWORD"]
)

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure API key authorization: ApiKeyBearer
configuration.api_key['ApiKeyBearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyBearer'] = 'Bearer'

# Configure API key authorization: asc_auth_key
configuration.api_key['asc_auth_key'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['asc_auth_key'] = 'Bearer'

# Configure Bearer authorization (JWT): Bearer
configuration = docspace-api-python.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.GroupRoomsApi(api_client)
    id = 9846 # int | The group ID.
    exclude_shared = true # bool | Specifies whether to exclude the group sharing settings from the response. (optional)
    count = 1234 # int | The number of groups to retrieve in the request. (optional)
    start_index = 1234 # int | The starting index from which to begin retrieving groups with their sharing settings. (optional)
    filter_value = 'some text' # str | The text used as a filter for retrieving groups with their sharing settings. (optional)

    try:
        # Get groups with sharing settings
        api_response = api_instance.get_groups_with_shared(id, exclude_shared=exclude_shared, count=count, start_index=start_index, filter_value=filter_value)
        print("The response of GroupRoomsApi->get_groups_with_shared:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupRoomsApi->get_groups_with_shared: %s\n" % e)
```



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

