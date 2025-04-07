# docspace.PeoplePhotosApi

All URIs are relative to *http://localhost:8092*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_member_photo_thumbnails**](PeoplePhotosApi.md#create_member_photo_thumbnails) | **POST** /api/2.0/people/{userid}/photo/thumbnails | Create photo thumbnails
[**delete_member_photo**](PeoplePhotosApi.md#delete_member_photo) | **DELETE** /api/2.0/people/{userid}/photo | Delete a user photo
[**get_member_photo**](PeoplePhotosApi.md#get_member_photo) | **GET** /api/2.0/people/{userid}/photo | Get a user photo
[**update_member_photo**](PeoplePhotosApi.md#update_member_photo) | **PUT** /api/2.0/people/{userid}/photo | Update a user photo
[**upload_member_photo**](PeoplePhotosApi.md#upload_member_photo) | **POST** /api/2.0/people/{userid}/photo | Upload a user photo


# **create_member_photo_thumbnails**
> ThumbnailsDataWrapper create_member_photo_thumbnails(userid, thumbnails_request=thumbnails_request)

Create photo thumbnails

Creates photo thumbnails by coordinates of the original image specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
from docspace.models.thumbnails_request import ThumbnailsRequest
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
    api_instance = docspace.PeoplePhotosApi(api_client)
    userid = '9846' # str | User ID
    thumbnails_request = docspace.ThumbnailsRequest() # ThumbnailsRequest | Thumbnails (optional)

    try:
        # Create photo thumbnails
        api_response = api_instance.create_member_photo_thumbnails(userid, thumbnails_request=thumbnails_request)
        print("The response of PeoplePhotosApi->create_member_photo_thumbnails:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePhotosApi->create_member_photo_thumbnails: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **thumbnails_request** | [**ThumbnailsRequest**](ThumbnailsRequest.md)| Thumbnails | [optional] 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Delete a user photo

Deletes a photo of the user with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
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
    api_instance = docspace.PeoplePhotosApi(api_client)
    userid = '9846' # str | User ID

    try:
        # Delete a user photo
        api_response = api_instance.delete_member_photo(userid)
        print("The response of PeoplePhotosApi->delete_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePhotosApi->delete_member_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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

Get a user photo

Returns a photo of the user with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
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
    api_instance = docspace.PeoplePhotosApi(api_client)
    userid = '9846' # str | User ID

    try:
        # Get a user photo
        api_response = api_instance.get_member_photo(userid)
        print("The response of PeoplePhotosApi->get_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePhotosApi->get_member_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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
> ThumbnailsDataWrapper update_member_photo(userid, update_photo_member_request=update_photo_member_request)

Update a user photo

Updates a photo of the user with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.thumbnails_data_wrapper import ThumbnailsDataWrapper
from docspace.models.update_photo_member_request import UpdatePhotoMemberRequest
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
    api_instance = docspace.PeoplePhotosApi(api_client)
    userid = '9846' # str | User ID
    update_photo_member_request = docspace.UpdatePhotoMemberRequest() # UpdatePhotoMemberRequest | Update photo (optional)

    try:
        # Update a user photo
        api_response = api_instance.update_member_photo(userid, update_photo_member_request=update_photo_member_request)
        print("The response of PeoplePhotosApi->update_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePhotosApi->update_member_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **update_photo_member_request** | [**UpdatePhotoMemberRequest**](UpdatePhotoMemberRequest.md)| Update photo | [optional] 

### Return type

[**ThumbnailsDataWrapper**](ThumbnailsDataWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

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
> FileUploadResultWrapper upload_member_photo(userid, form_collection=form_collection)

Upload a user photo

Uploads a photo of the user with the ID specified in the request.

### Example

* Api Key Authentication (asc_auth_key):

```python
import docspace
from docspace.models.file_upload_result_wrapper import FileUploadResultWrapper
from docspace.models.key_value_pair_string_string_values import KeyValuePairStringStringValues
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
    api_instance = docspace.PeoplePhotosApi(api_client)
    userid = '9846' # str | User ID
    form_collection = [docspace.KeyValuePairStringStringValues()] # List[KeyValuePairStringStringValues] | Image data (optional)

    try:
        # Upload a user photo
        api_response = api_instance.upload_member_photo(userid, form_collection=form_collection)
        print("The response of PeoplePhotosApi->upload_member_photo:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PeoplePhotosApi->upload_member_photo: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| User ID | 
 **form_collection** | [**List[KeyValuePairStringStringValues]**](KeyValuePairStringStringValues.md)| Image data | [optional] 

### Return type

[**FileUploadResultWrapper**](FileUploadResultWrapper.md)

### Authorization

[asc_auth_key](../README.md#asc_auth_key)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Result of file uploading |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

