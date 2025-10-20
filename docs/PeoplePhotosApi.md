# docspace_api_sdk.PhotosApi

All URIs are relative to *https://your-docspace.onlyoffice.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_member_photo_thumbnails**](#create_member_photo_thumbnails) | **POST** /api/2.0/people/{userid}/photo/thumbnails | Create photo thumbnails
[**delete_member_photo**](#delete_member_photo) | **DELETE** /api/2.0/people/{userid}/photo | Delete a user photo
[**get_member_photo**](#get_member_photo) | **GET** /api/2.0/people/{userid}/photo | Get a user photo
[**update_member_photo**](#update_member_photo) | **PUT** /api/2.0/people/{userid}/photo | Update a user photo
[**upload_member_photo**](#upload_member_photo) | **POST** /api/2.0/people/{userid}/photo | Upload a user photo


# **create_member_photo_thumbnails**
> ThumbnailsDataWrapper create_member_photo_thumbnails(userid, thumbnails_request)

Creates the user photo thumbnails by coordinates of the original image specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 
 **thumbnails_request** | [**ThumbnailsRequest**](ThumbnailsRequest.md)| The thumbnail request. | 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
from docspace_api_sdk.models.thumbnails_request import ThumbnailsRequest
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
    api_instance = docspace_api_sdk.PhotosApi(api_client)
    userid = '9846' # str | The user ID.
    thumbnails_request = docspace_api_sdk.ThumbnailsRequest() # ThumbnailsRequest | The thumbnail request.

    try:
        # Create photo thumbnails
        api_response = api_instance.create_member_photo_thumbnails(userid, thumbnails_request)
        print("The response of PhotosApi->create_member_photo_thumbnails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->create_member_photo_thumbnails: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail parameters |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member_photo**
> ThumbnailsDataWrapper delete_member_photo(userid)

Deletes a photo of the user with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
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
    api_instance = docspace_api_sdk.PhotosApi(api_client)
    userid = '9846' # str | The user ID.

    try:
        # Delete a user photo
        api_response = api_instance.delete_member_photo(userid)
        print("The response of PhotosApi->delete_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->delete_member_photo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail parameters: original photo, retina, maximum size photo, big, medium, small |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_photo**
> ThumbnailsDataWrapper get_member_photo(userid)

Returns a photo of the user with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
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
    api_instance = docspace_api_sdk.PhotosApi(api_client)
    userid = '9846' # str | The user ID.

    try:
        # Get a user photo
        api_response = api_instance.get_member_photo(userid)
        print("The response of PhotosApi->get_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->get_member_photo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Thumbnail parameters: original photo, retina, maximum size photo, big, medium, small |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_photo**
> ThumbnailsDataWrapper update_member_photo(userid, update_photo_member_request)

Updates a photo of the user with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 
 **update_photo_member_request** | [**UpdatePhotoMemberRequest**](UpdatePhotoMemberRequest.md)| The request parameters for updating a photo. | 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
from docspace_api_sdk.models.update_photo_member_request import UpdatePhotoMemberRequest
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
    api_instance = docspace_api_sdk.PhotosApi(api_client)
    userid = '9846' # str | The user ID.
    update_photo_member_request = docspace_api_sdk.UpdatePhotoMemberRequest() # UpdatePhotoMemberRequest | The request parameters for updating a photo.

    try:
        # Update a user photo
        api_response = api_instance.update_member_photo(userid, update_photo_member_request)
        print("The response of PhotosApi->update_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->update_member_photo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated thumbnail parameters: original photo, retina, maximum size photo, big, medium, small |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**404** | User not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_member_photo**
> FileUploadResultWrapper upload_member_photo(userid, form_collection)

Uploads a photo of the user with the ID specified in the request.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The user ID. | 
 **form_collection** | [**List[KeyValuePairStringStringValues]**](KeyValuePairStringStringValues.md)| The image data. | 

### Return type

[**FileUploadResultWrapper**](FileUploadResultWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_upload_result_wrapper import FileUploadResultWrapper
from docspace_api_sdk.models.key_value_pair_string_string_values import KeyValuePairStringStringValues
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
    api_instance = docspace_api_sdk.PhotosApi(api_client)
    userid = '9846' # str | The user ID.
    form_collection = [docspace_api_sdk.KeyValuePairStringStringValues()] # List[KeyValuePairStringStringValues] | The image data.

    try:
        # Upload a user photo
        api_response = api_instance.upload_member_photo(userid, form_collection)
        print("The response of PhotosApi->upload_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PhotosApi->upload_member_photo: %s\n" % e)
```



### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of file uploading |  -  |
**400** | The uploaded file could not be found |  -  |
**401** | Unauthorized |  -  |
**403** | No permissions to perform this action |  -  |
**413** | Image size is too large |  -  |
**415** | Unknown image file type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

