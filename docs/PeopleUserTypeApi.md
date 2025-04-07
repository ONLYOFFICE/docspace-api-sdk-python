# docspace.PeopleUserTypeApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**update_user_type**](PeopleUserTypeApi.md#update_user_type) | **PUT** /api/2.0/people/type/{type} | Change a user type


# **update_user_type**
> EmployeeFullArrayWrapper update_user_type(type, update_members_request_dto=update_members_request_dto)

Change a user type

Changes a type for the users with the IDs specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.employee_full_array_wrapper import EmployeeFullArrayWrapper
from docspace.models.employee_type import EmployeeType
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
    api_instance = docspace.PeopleUserTypeApi(api_client)
    type = docspace.EmployeeType() # EmployeeType | New user type
    update_members_request_dto = docspace.UpdateMembersRequestDto() # UpdateMembersRequestDto | Update members (optional)

    try:
        # Change a user type
        api_response = api_instance.update_user_type(type, update_members_request_dto=update_members_request_dto)
        print("The response of PeopleUserTypeApi->update_user_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleUserTypeApi->update_user_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | [**EmployeeType**](.md)| New user type | 
 **update_members_request_dto** | [**UpdateMembersRequestDto**](UpdateMembersRequestDto.md)| Update members | [optional] 

### Return type

[**EmployeeFullArrayWrapper**](EmployeeFullArrayWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with the detailed information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

