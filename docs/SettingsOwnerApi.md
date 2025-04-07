# docspace.SettingsOwnerApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**owner**](SettingsOwnerApi.md#owner) | **PUT** /api/2.0/settings/owner | Update the portal owner
[**send_owner_change_instructions**](SettingsOwnerApi.md#send_owner_change_instructions) | **POST** /api/2.0/settings/owner | Send the owner change instructions


# **owner**
> owner(owner_id_settings_request_dto=owner_id_settings_request_dto)

Update the portal owner

Updates the current portal owner with a new one specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto
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
    api_instance = docspace.SettingsOwnerApi(api_client)
    owner_id_settings_request_dto = docspace.OwnerIdSettingsRequestDto() # OwnerIdSettingsRequestDto |  (optional)

    try:
        # Update the portal owner
        api_instance.owner(owner_id_settings_request_dto=owner_id_settings_request_dto)
    except Exception as e:
        print("Exception when calling SettingsOwnerApi->owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id_settings_request_dto** | [**OwnerIdSettingsRequestDto**](OwnerIdSettingsRequestDto.md)|  | [optional] 

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
**200** | Ok |  -  |
**400** | The user could not be found |  -  |
**401** | Unauthorized |  -  |
**409** |  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_owner_change_instructions**
> OwnerChangeInstructionsWrapper send_owner_change_instructions(owner_id_settings_request_dto=owner_id_settings_request_dto)

Send the owner change instructions

Sends the instructions to change the DocSpace owner.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.owner_change_instructions_wrapper import OwnerChangeInstructionsWrapper
from docspace.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto
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
    api_instance = docspace.SettingsOwnerApi(api_client)
    owner_id_settings_request_dto = docspace.OwnerIdSettingsRequestDto() # OwnerIdSettingsRequestDto |  (optional)

    try:
        # Send the owner change instructions
        api_response = api_instance.send_owner_change_instructions(owner_id_settings_request_dto=owner_id_settings_request_dto)
        print("The response of SettingsOwnerApi->send_owner_change_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsOwnerApi->send_owner_change_instructions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id_settings_request_dto** | [**OwnerIdSettingsRequestDto**](OwnerIdSettingsRequestDto.md)|  | [optional] 

### Return type

[**OwnerChangeInstructionsWrapper**](OwnerChangeInstructionsWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about changing the portal owner |  -  |
**401** | Unauthorized |  -  |
**403** | Collaborator can not be an owner |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

