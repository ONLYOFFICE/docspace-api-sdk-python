# docspace.SettingsMessagesApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_admin_message_settings**](SettingsMessagesApi.md#enable_admin_message_settings) | **POST** /api/2.0/settings/messagesettings | Enable the administrator message settings
[**send_adm_mail**](SettingsMessagesApi.md#send_adm_mail) | **POST** /api/2.0/settings/sendadmmail | Send a message to the administrator
[**send_join_invite_mail**](SettingsMessagesApi.md#send_join_invite_mail) | **POST** /api/2.0/settings/sendjoininvite | Sends an invitation email


# **enable_admin_message_settings**
> StringWrapper enable_admin_message_settings(turn_on_admin_message_settings_request_dto=turn_on_admin_message_settings_request_dto)

Enable the administrator message settings

Displays the contact form on the \"Sign In\" page, allowing users to send a message to the DocSpace administrator in case they encounter any issues while accessing DocSpace.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.string_wrapper import StringWrapper
from docspace.models.turn_on_admin_message_settings_request_dto import TurnOnAdminMessageSettingsRequestDto
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
    api_instance = docspace.SettingsMessagesApi(api_client)
    turn_on_admin_message_settings_request_dto = docspace.TurnOnAdminMessageSettingsRequestDto() # TurnOnAdminMessageSettingsRequestDto |  (optional)

    try:
        # Enable the administrator message settings
        api_response = api_instance.enable_admin_message_settings(turn_on_admin_message_settings_request_dto=turn_on_admin_message_settings_request_dto)
        print("The response of SettingsMessagesApi->enable_admin_message_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsMessagesApi->enable_admin_message_settings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **turn_on_admin_message_settings_request_dto** | [**TurnOnAdminMessageSettingsRequestDto**](TurnOnAdminMessageSettingsRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about the result of saving new settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_adm_mail**
> StringWrapper send_adm_mail(admin_message_settings_requests_dto=admin_message_settings_requests_dto)

Send a message to the administrator

Sends a message to the administrator email when unauthorized users encounter issues accessing DocSpace.

### Example


```python
import docspace
from docspace.models.admin_message_settings_requests_dto import AdminMessageSettingsRequestsDto
from docspace.models.string_wrapper import StringWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsMessagesApi(api_client)
    admin_message_settings_requests_dto = docspace.AdminMessageSettingsRequestsDto() # AdminMessageSettingsRequestsDto |  (optional)

    try:
        # Send a message to the administrator
        api_response = api_instance.send_adm_mail(admin_message_settings_requests_dto=admin_message_settings_requests_dto)
        print("The response of SettingsMessagesApi->send_adm_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsMessagesApi->send_adm_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_message_settings_requests_dto** | [**AdminMessageSettingsRequestsDto**](AdminMessageSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about the result of sending a message |  -  |
**400** | Incorrect email or message text is empty |  -  |
**429** | Request limit is exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_join_invite_mail**
> StringWrapper send_join_invite_mail(admin_message_base_settings_requests_dto=admin_message_base_settings_requests_dto)

Sends an invitation email

Sends an invitation email with a link to the DocSpace.

### Example


```python
import docspace
from docspace.models.admin_message_base_settings_requests_dto import AdminMessageBaseSettingsRequestsDto
from docspace.models.string_wrapper import StringWrapper
from docspace.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace.SettingsMessagesApi(api_client)
    admin_message_base_settings_requests_dto = docspace.AdminMessageBaseSettingsRequestsDto() # AdminMessageBaseSettingsRequestsDto |  (optional)

    try:
        # Sends an invitation email
        api_response = api_instance.send_join_invite_mail(admin_message_base_settings_requests_dto=admin_message_base_settings_requests_dto)
        print("The response of SettingsMessagesApi->send_join_invite_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsMessagesApi->send_join_invite_mail: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_message_base_settings_requests_dto** | [**AdminMessageBaseSettingsRequestsDto**](AdminMessageBaseSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about sending a link to confirm joining the DocSpace |  -  |
**400** | Incorrect email or email already exists |  -  |
**403** | No permissions to perform this action |  -  |
**429** | Request limit is exceeded |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

