# docspace-api-python.FilesSharingApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_external_share_password**](#apply_external_share_password) | **POST** /api/2.0/files/share/{key}/password | Apply external data password
[**change_file_owner**](#change_file_owner) | **POST** /api/2.0/files/owner | Change the file owner
[**get_external_share_data**](#get_external_share_data) | **GET** /api/2.0/files/share/{key} | Get the external data
[**get_shared_users**](#get_shared_users) | **GET** /api/2.0/files/file/{fileId}/sharedusers | Get user access rights by file ID
[**send_editor_notify**](#send_editor_notify) | **POST** /api/2.0/files/file/{fileId}/sendeditornotify | Send the mention message


# **apply_external_share_password**
> ExternalShareWrapper apply_external_share_password(key, external_share_request_param=external_share_request_param)

Applies a password specified in the request to get the external data.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The unique document identifier. | 
 **external_share_request_param** | [**ExternalShareRequestParam**](ExternalShareRequestParam.md)| The external data share request parameters. | [optional] 

### Return type

[**ExternalShareWrapper**](ExternalShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.external_share_request_param import ExternalShareRequestParam
from docspace-api-python.models.external_share_wrapper import ExternalShareWrapper
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
    api_instance = docspace-api-python.FilesSharingApi(api_client)
    key = 'some text' # str | The unique document identifier.
    external_share_request_param = docspace-api-python.ExternalShareRequestParam() # ExternalShareRequestParam | The external data share request parameters. (optional)

    try:
        # Apply external data password
        api_response = api_instance.apply_external_share_password(key, external_share_request_param=external_share_request_param)
        print("The response of FilesSharingApi->apply_external_share_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSharingApi->apply_external_share_password: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External data |  -  |
**429** | Too many requests |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **change_file_owner**
> FileEntryArrayWrapper change_file_owner(change_owner_request_dto=change_owner_request_dto)

Changes the owner of the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **change_owner_request_dto** | [**ChangeOwnerRequestDto**](ChangeOwnerRequestDto.md)|  | [optional] 

### Return type

[**FileEntryArrayWrapper**](FileEntryArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.change_owner_request_dto import ChangeOwnerRequestDto
from docspace-api-python.models.file_entry_array_wrapper import FileEntryArrayWrapper
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
    api_instance = docspace-api-python.FilesSharingApi(api_client)
    change_owner_request_dto = docspace-api-python.ChangeOwnerRequestDto() # ChangeOwnerRequestDto |  (optional)

    try:
        # Change the file owner
        api_response = api_instance.change_file_owner(change_owner_request_dto=change_owner_request_dto)
        print("The response of FilesSharingApi->change_file_owner:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSharingApi->change_file_owner: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | File entry information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_share_data**
> ExternalShareWrapper get_external_share_data(key, file_id=file_id)

Returns the external data by the key specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key** | **str**| The unique key of the external shared data. | 
 **file_id** | **str**| The unique document identifier. | [optional] 

### Return type

[**ExternalShareWrapper**](ExternalShareWrapper.md)

### Authorization

No authorization required

### Example


```python
import docspace-api-python
from docspace-api-python.models.external_share_wrapper import ExternalShareWrapper
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
    api_instance = docspace-api-python.FilesSharingApi(api_client)
    key = 'some text' # str | The unique key of the external shared data.
    file_id = '9846' # str | The unique document identifier. (optional)

    try:
        # Get the external data
        api_response = api_instance.get_external_share_data(key, file_id=file_id)
        print("The response of FilesSharingApi->get_external_share_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSharingApi->get_external_share_data: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | External data |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_shared_users**
> MentionWrapperArrayWrapper get_shared_users(file_id)

Returns a list of users with their access rights to the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the request. | 

### Return type

[**MentionWrapperArrayWrapper**](MentionWrapperArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.mention_wrapper_array_wrapper import MentionWrapperArrayWrapper
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
    api_instance = docspace-api-python.FilesSharingApi(api_client)
    file_id = 9846 # int | The file ID of the request.

    try:
        # Get user access rights by file ID
        api_response = api_instance.get_shared_users(file_id)
        print("The response of FilesSharingApi->get_shared_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSharingApi->get_shared_users: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of users with their access rights to the file |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_editor_notify**
> AceShortWrapperArrayWrapper send_editor_notify(file_id, mention_message_wrapper=mention_message_wrapper)

Sends a message to the users who are mentioned in the file with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_id** | **int**| The file ID of the mention message. | 
 **mention_message_wrapper** | [**MentionMessageWrapper**](MentionMessageWrapper.md)| The mention message. | [optional] 

### Return type

[**AceShortWrapperArrayWrapper**](AceShortWrapperArrayWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace-api-python
from docspace-api-python.models.ace_short_wrapper_array_wrapper import AceShortWrapperArrayWrapper
from docspace-api-python.models.mention_message_wrapper import MentionMessageWrapper
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
    api_instance = docspace-api-python.FilesSharingApi(api_client)
    file_id = 9846 # int | The file ID of the mention message.
    mention_message_wrapper = docspace-api-python.MentionMessageWrapper() # MentionMessageWrapper | The mention message. (optional)

    try:
        # Send the mention message
        api_response = api_instance.send_editor_notify(file_id, mention_message_wrapper=mention_message_wrapper)
        print("The response of FilesSharingApi->send_editor_notify:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FilesSharingApi->send_editor_notify: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of access rights information |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

