# docspace.PeopleGuestsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_guests**](PeopleGuestsApi.md#delete_guests) | **DELETE** /api/2.0/people/guests | Removes guests from the list and from rooms


# **delete_guests**
> delete_guests(update_members_request_dto=update_members_request_dto)

Removes guests from the list and from rooms

Removes guests from the list and excludes them from rooms to which you have invited them

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.update_members_request_dto import UpdateMembersRequestDto
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
    api_instance = docspace.PeopleGuestsApi(api_client)
    update_members_request_dto = docspace.UpdateMembersRequestDto() # UpdateMembersRequestDto |  (optional)

    try:
        # Removes guests from the list and from rooms
        api_instance.delete_guests(update_members_request_dto=update_members_request_dto)
    except Exception as e:
        print("Exception when calling PeopleGuestsApi->delete_guests: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request parameters for deleting guests |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

