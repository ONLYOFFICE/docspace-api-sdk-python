# docspace.SettingsOwnerApi

All URIs are relative to *http://http:*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_owner_change_instructions**](SettingsOwnerApi.md#send_owner_change_instructions) | **POST** /api/2.0/settings/owner | Send the owner change instructions
[**update_portal_owner**](SettingsOwnerApi.md#update_portal_owner) | **PUT** /api/2.0/settings/owner | Update the portal owner


# **send_owner_change_instructions**
> OwnerChangeInstructionsWrapper send_owner_change_instructions(owner_id_settings_request_dto=owner_id_settings_request_dto)

Send the owner change instructions

Sends the instructions to change the DocSpace owner.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.owner_change_instructions_wrapper import OwnerChangeInstructionsWrapper
from docspace.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

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

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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

# **update_portal_owner**
> update_portal_owner(owner_id_settings_request_dto=owner_id_settings_request_dto)

Update the portal owner

Updates the current portal owner with a new one specified in the request.

### Example

* Basic Authentication (Basic):
* OAuth Authentication (OAuth2):
* Api Key Authentication (ApiKeyBearer):
* Api Key Authentication (asc_auth_key):
* Bearer (JWT) Authentication (Bearer):

```python
import docspace
from docspace.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://http:
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://http:"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: Basic
configuration = docspace.Configuration(
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
configuration = docspace.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsOwnerApi(api_client)
    owner_id_settings_request_dto = docspace.OwnerIdSettingsRequestDto() # OwnerIdSettingsRequestDto |  (optional)

    try:
        # Update the portal owner
        api_instance.update_portal_owner(owner_id_settings_request_dto=owner_id_settings_request_dto)
    except Exception as e:
        print("Exception when calling SettingsOwnerApi->update_portal_owner: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id_settings_request_dto** | [**OwnerIdSettingsRequestDto**](OwnerIdSettingsRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

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

