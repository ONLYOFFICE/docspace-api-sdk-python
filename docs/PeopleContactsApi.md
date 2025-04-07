# docspace.PeopleContactsApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_member_contacts**](PeopleContactsApi.md#delete_member_contacts) | **DELETE** /api/2.0/people/{userid}/contacts | Delete user contacts
[**set_member_contacts**](PeopleContactsApi.md#set_member_contacts) | **POST** /api/2.0/people/{userid}/contacts | Set user contacts
[**update_member_contacts**](PeopleContactsApi.md#update_member_contacts) | **PUT** /api/2.0/people/{userid}/contacts | Update user contacts


# **delete_member_contacts**
> EmployeeFullWrapper delete_member_contacts(userid, contacts_request=contacts_request)

Delete user contacts

Deletes the contacts of the user with the ID specified in the request from the portal.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.contacts_request import ContactsRequest
from docspace.models.employee_full_wrapper import EmployeeFullWrapper
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
    api_instance = docspace.PeopleContactsApi(api_client)
    userid = '9846' # str | User ID
    contacts_request = docspace.ContactsRequest() # ContactsRequest | Contacts (optional)

    try:
        # Delete user contacts
        api_response = api_instance.delete_member_contacts(userid, contacts_request=contacts_request)
        print("The response of PeopleContactsApi->delete_member_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleContactsApi->delete_member_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **contacts_request** | [**ContactsRequest**](ContactsRequest.md)| Contacts | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Deleted user profile with the detailed information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_member_contacts**
> EmployeeFullWrapper set_member_contacts(userid, contacts_request=contacts_request)

Set user contacts

Sets the contacts of the user with the ID specified in the request replacing the current portal data with the new data.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.contacts_request import ContactsRequest
from docspace.models.employee_full_wrapper import EmployeeFullWrapper
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
    api_instance = docspace.PeopleContactsApi(api_client)
    userid = '9846' # str | User ID
    contacts_request = docspace.ContactsRequest() # ContactsRequest | Contacts (optional)

    try:
        # Set user contacts
        api_response = api_instance.set_member_contacts(userid, contacts_request=contacts_request)
        print("The response of PeopleContactsApi->set_member_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleContactsApi->set_member_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **contacts_request** | [**ContactsRequest**](ContactsRequest.md)| Contacts | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user profile with the detailed information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_contacts**
> EmployeeFullWrapper update_member_contacts(userid, contacts_request=contacts_request)

Update user contacts

Updates the contact information of the user with the ID specified in the request merging the new data into the current portal data.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.contacts_request import ContactsRequest
from docspace.models.employee_full_wrapper import EmployeeFullWrapper
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
    api_instance = docspace.PeopleContactsApi(api_client)
    userid = '9846' # str | User ID
    contacts_request = docspace.ContactsRequest() # ContactsRequest | Contacts (optional)

    try:
        # Update user contacts
        api_response = api_instance.update_member_contacts(userid, contacts_request=contacts_request)
        print("The response of PeopleContactsApi->update_member_contacts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeopleContactsApi->update_member_contacts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **contacts_request** | [**ContactsRequest**](ContactsRequest.md)| Contacts | [optional] 

### Return type

[**EmployeeFullWrapper**](EmployeeFullWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user profile with the detailed information |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

