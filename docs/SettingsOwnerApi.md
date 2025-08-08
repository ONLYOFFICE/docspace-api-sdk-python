# docspace_api_sdk.OwnerApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**send_owner_change_instructions**](#send_owner_change_instructions) | **POST** /api/2.0/settings/owner | Send the owner change instructions
[**update_portal_owner**](#update_portal_owner) | **PUT** /api/2.0/settings/owner | Update the portal owner


# **send_owner_change_instructions**
> OwnerChangeInstructionsWrapper send_owner_change_instructions(owner_id_settings_request_dto=owner_id_settings_request_dto)

Sends the instructions to change the DocSpace owner.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id_settings_request_dto** | [**OwnerIdSettingsRequestDto**](OwnerIdSettingsRequestDto.md)|  | [optional] 

### Return type

[**OwnerChangeInstructionsWrapper**](OwnerChangeInstructionsWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.owner_change_instructions_wrapper import OwnerChangeInstructionsWrapper
from docspace_api_sdk.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OwnerApi(api_client)
    owner_id_settings_request_dto = docspace_api_sdk.OwnerIdSettingsRequestDto() # OwnerIdSettingsRequestDto |  (optional)

    try:
        # Send the owner change instructions
        api_response = api_instance.send_owner_change_instructions(owner_id_settings_request_dto=owner_id_settings_request_dto)
        print("The response of OwnerApi->send_owner_change_instructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OwnerApi->send_owner_change_instructions: %s\n" % e)
```



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

Updates the current portal owner with a new one specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner_id_settings_request_dto** | [**OwnerIdSettingsRequestDto**](OwnerIdSettingsRequestDto.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.owner_id_settings_request_dto import OwnerIdSettingsRequestDto
from docspace_api_sdk.rest import ApiException
from pprint import pprint

configuration = docspace_api_sdk.Configuration(
    host = "https://your-docspace.onlyoffice.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = docspace_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with docspace_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace_api_sdk.OwnerApi(api_client)
    owner_id_settings_request_dto = docspace_api_sdk.OwnerIdSettingsRequestDto() # OwnerIdSettingsRequestDto |  (optional)

    try:
        # Update the portal owner
        api_instance.update_portal_owner(owner_id_settings_request_dto=owner_id_settings_request_dto)
    except Exception as e:
        print("Exception when calling OwnerApi->update_portal_owner: %s\n" % e)
```



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

