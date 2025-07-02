# docspace-api-python.SettingsMessagesApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**enable_admin_message_settings**](#enable_admin_message_settings) | **POST** /api/2.0/settings/messagesettings | Enable the administrator message settings
[**send_admin_mail**](#send_admin_mail) | **POST** /api/2.0/settings/sendadmmail | Send a message to the administrator
[**send_join_invite_mail**](#send_join_invite_mail) | **POST** /api/2.0/settings/sendjoininvite | Sends an invitation email


# **enable_admin_message_settings**
> StringWrapper enable_admin_message_settings(turn_on_admin_message_settings_request_dto=turn_on_admin_message_settings_request_dto)

Displays the contact form on the "Sign In" page, allowing users to send a message to the DocSpace administrator in case they encounter any issues while accessing DocSpace.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **turn_on_admin_message_settings_request_dto** | [**TurnOnAdminMessageSettingsRequestDto**](TurnOnAdminMessageSettingsRequestDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.string_wrapper import StringWrapper
from docspace-api-python.models.turn_on_admin_message_settings_request_dto import TurnOnAdminMessageSettingsRequestDto
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
    api_instance = docspace-api-python.SettingsMessagesApi(api_client)
    turn_on_admin_message_settings_request_dto = docspace-api-python.TurnOnAdminMessageSettingsRequestDto() # TurnOnAdminMessageSettingsRequestDto |  (optional)

    try:
        # Enable the administrator message settings
        api_response = api_instance.enable_admin_message_settings(turn_on_admin_message_settings_request_dto=turn_on_admin_message_settings_request_dto)
        print("The response of SettingsMessagesApi->enable_admin_message_settings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsMessagesApi->enable_admin_message_settings: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Message about the result of saving new settings |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_admin_mail**
> StringWrapper send_admin_mail(admin_message_settings_requests_dto=admin_message_settings_requests_dto)

Sends a message to the administrator email when unauthorized users encounter issues accessing DocSpace.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_message_settings_requests_dto** | [**AdminMessageSettingsRequestsDto**](AdminMessageSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.admin_message_settings_requests_dto import AdminMessageSettingsRequestsDto
from docspace-api-python.models.string_wrapper import StringWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsMessagesApi(api_client)
    admin_message_settings_requests_dto = docspace-api-python.AdminMessageSettingsRequestsDto() # AdminMessageSettingsRequestsDto |  (optional)

    try:
        # Send a message to the administrator
        api_response = api_instance.send_admin_mail(admin_message_settings_requests_dto=admin_message_settings_requests_dto)
        print("The response of SettingsMessagesApi->send_admin_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsMessagesApi->send_admin_mail: %s\n" % e)
```



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

Sends an invitation email with a link to the DocSpace.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **admin_message_base_settings_requests_dto** | [**AdminMessageBaseSettingsRequestsDto**](AdminMessageBaseSettingsRequestsDto.md)|  | [optional] 

### Return type

[**StringWrapper**](StringWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.admin_message_base_settings_requests_dto import AdminMessageBaseSettingsRequestsDto
from docspace-api-python.models.string_wrapper import StringWrapper
from docspace-api-python.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:8092
# See configuration.py for a list of all supported configuration parameters.
configuration = docspace-api-python.Configuration(
    host = "http://localhost:8092"
)


# Enter a context with an instance of the API client
with docspace-api-python.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = docspace-api-python.SettingsMessagesApi(api_client)
    admin_message_base_settings_requests_dto = docspace-api-python.AdminMessageBaseSettingsRequestsDto() # AdminMessageBaseSettingsRequestsDto |  (optional)

    try:
        # Sends an invitation email
        api_response = api_instance.send_join_invite_mail(admin_message_base_settings_requests_dto=admin_message_base_settings_requests_dto)
        print("The response of SettingsMessagesApi->send_join_invite_mail:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SettingsMessagesApi->send_join_invite_mail: %s\n" % e)
```



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

