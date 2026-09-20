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

Crops the avatar of a profile to the rectangle given in the request and rebuilds all of its thumbnail sizes,
which is the second step of changing an avatar by hand.
It works in two modes: with `tmpFile` it takes the temporary image
`POST api/2.0/people/{userid}/photo` produced with `autosave` off, makes the cropped result the main photo and
then discards the temporary file, and without `tmpFile` it re-crops the photo the profile already has.
A caller may only do this to their own profile - the ID in the route has to be the calling account, and an
administrator gets 403 for anybody else - and the account must be allowed to edit its own profile.
The call replaces the stored photo, so the previous crop is lost, and it can be repeated with new coordinates
as often as needed.
Passing `width` and `height` as 0 together with `tmpFile` keeps the whole uploaded image instead of cropping
it.
The answer holds the URLs of every generated size, the same shape `GET api/2.0/people/{userid}/photo`
returns.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The profile whose avatar is cropped, taken from the route. Either the ID of the account or its user name is  accepted, and it has to be the calling account, because a profile photo can only be changed by its owner. | 
 **thumbnails_request** | [**ThumbnailsRequest**](ThumbnailsRequest.md)| The crop rectangle, and optionally the temporary image to crop. | 

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
    userid = '00000000-0000-0000-0000-000000000000' # str | The profile whose avatar is cropped, taken from the route. Either the ID of the account or its user name is  accepted, and it has to be the calling account, because a profile photo can only be changed by its owner.
    thumbnails_request = docspace_api_sdk.ThumbnailsRequest() # ThumbnailsRequest | The crop rectangle, and optionally the temporary image to crop.

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
**200** | The URLs of the rebuilt photo sizes |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The ID in the route is not the calling account, or the account may not edit its own profile |  -  |
**404** | No user has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_member_photo**
> ThumbnailsDataWrapper delete_member_photo(userid)

Removes the avatar of a profile, so that the profile falls back to the default placeholder image.
A caller may only do this to their own profile - the ID in the route has to be the calling account, and an
administrator gets 403 for anybody else - and the account must be allowed to edit its own profile.
The removal is permanent and cannot be undone: the stored image and all of its sizes are deleted, and a new
avatar has to be uploaded through `POST api/2.0/people/{userid}/photo` to replace it.
The call is idempotent, so removing an avatar from a profile that has none succeeds as well, and it raises a
`UserUpdated` webhook.
The answer still holds the URLs of every size, now pointing at the default image.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The profile whose avatar the operation addresses, taken from the route. Either the ID of the account or its  user name is accepted. Reading a photo works for any account the caller may see, while deleting one only  works for the calling account itself. | 

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
    userid = '00000000-0000-0000-0000-000000000000' # str | The profile whose avatar the operation addresses, taken from the route. Either the ID of the account or its  user name is accepted. Reading a photo works for any account the caller may see, while deleting one only  works for the calling account itself.

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
**200** | The URLs of every photo size, now pointing at the default image |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The ID in the route is not the calling account, or the account may not edit its own profile |  -  |
**404** | No user has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_member_photo**
> ThumbnailsDataWrapper get_member_photo(userid)

Returns the URLs of the avatar of a profile in every size the portal keeps: the original, the retina and the
maximum variants, and the big, medium and small thumbnails.
Unlike the operations that change an avatar, this one may be called for another account, as long as the
caller is allowed to see that account - a guest, for instance, only sees the accounts it is related to.
The call is read-only and always answers with a full set of URLs: a profile that has no avatar of its own
gets the URLs of the default placeholder image rather than an empty answer.
The URLs are portal paths meant to be requested directly and may be replaced when the avatar changes, so they
should not be stored for a long time.
To change the avatar use `POST api/2.0/people/{userid}/photo` for an uploaded file,
`PUT api/2.0/people/{userid}/photo` for one taken from a URL, and
`DELETE api/2.0/people/{userid}/photo` to drop it.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The profile whose avatar the operation addresses, taken from the route. Either the ID of the account or its  user name is accepted. Reading a photo works for any account the caller may see, while deleting one only  works for the calling account itself. | 

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
    userid = '00000000-0000-0000-0000-000000000000' # str | The profile whose avatar the operation addresses, taken from the route. Either the ID of the account or its  user name is accepted. Reading a photo works for any account the caller may see, while deleting one only  works for the calling account itself.

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
**200** | The URLs of the photo in every size, or of the default image when the profile has no photo |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**403** | The caller is not allowed to see the requested account |  -  |
**404** | No user has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_photo**
> ThumbnailsDataWrapper update_member_photo(userid, update_photo_member_request)

Sets the avatar of a profile from an image the portal downloads itself from the URL given in `files`, which is
the way to reuse a picture that is already published somewhere.
A caller may only do this to their own profile - the ID in the route has to be the calling account, and an
administrator gets 403 for anybody else - and the account must be allowed to edit its own profile.
The URL has to be absolute or relative to the portal, and it has to use HTTPS unless the request itself came
over HTTP; an address the portal refuses to fetch, and a download that does not succeed, both answer 403.
Passing the URL the profile already uses is a no-op, and an empty `files` is rejected with 400, so use
`DELETE api/2.0/people/{userid}/photo` to remove an avatar rather than sending an empty value.
The downloaded image replaces the stored avatar and all of its sizes at once, raises a `UserUpdated` webhook,
and is subject to the portal limit on image size.
To send the bytes instead of a URL, upload the file through `POST api/2.0/people/{userid}/photo`.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The profile whose avatar is replaced, taken from the route. Either the ID of the account or its user name is  accepted, and it has to be the calling account, because a profile photo can only be changed by its owner. | 
 **update_photo_member_request** | [**UpdatePhotoMemberRequest**](UpdatePhotoMemberRequest.md)| The address of the image to use as the new avatar. | 

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
    userid = '00000000-0000-0000-0000-000000000000' # str | The profile whose avatar is replaced, taken from the route. Either the ID of the account or its user name is  accepted, and it has to be the calling account, because a profile photo can only be changed by its owner.
    update_photo_member_request = docspace_api_sdk.UpdatePhotoMemberRequest() # UpdatePhotoMemberRequest | The address of the image to use as the new avatar.

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
**200** | The URLs of the photo sizes built from the downloaded image |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**400** | The files field is empty |  -  |
**403** | The ID in the route is not the calling account, the account may not edit its own profile, or the URL was refused or could not be downloaded |  -  |
**404** | No user has the specified ID |  -  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_member_photo**
> FileUploadResultWrapper upload_member_photo(userid, file, autosave=autosave)

Uploads an image as multipart form data and either makes it the avatar of a profile straight away or keeps it
as a temporary file to be cropped afterwards.
With `autosave` set to true the image becomes the avatar immediately, all of its sizes are built and their
URLs come back in `data`, each with a `hash` query parameter that changes whenever the avatar does, so a
client can cache them safely.
With `autosave` left false the image is only stored as a temporary file and `data` holds its name, which has
to be passed as `tmpFile` to `POST api/2.0/people/{userid}/photo/thumbnails` to choose the crop; nothing
changes on the profile until that second call succeeds.
A caller may only do this to their own profile, the ID in the route has to be the calling account, and the
image has to be a format the portal can read and stay within the portal limit on image size.
This operation reports every problem in the body instead of as a status code: it answers 200 with `success`
set to false and a human-readable `message`, and it does so for a missing file, an unreadable format, an
oversized image and a rejected permission alike, so a client has to check `success` and must not rely on the
status alone.
A successful upload raises a `UserUpdated` webhook only in the `autosave` case.

For more information, see [api.onlyoffice.com]().

### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **userid** | **str**| The profile whose avatar is uploaded, taken from the route. Either the ID of the account or its user name is  accepted, and it has to be the calling account, because a profile photo can only be changed by its owner. | 
 **file** | **bytes**| The image itself, sent as a multipart form field. It has to be a raster format the portal can read and stay  within the portal limit on image size; sending no file makes the operation answer with `success` false rather  than an error status. | 
 **autosave** | **bool**| Set it to true to make the uploaded image the avatar right away. With the default false the image is only  stored as a temporary file whose name comes back in `data`, and it has to be passed to  `POST api/2.0/people/{userid}/photo/thumbnails` to take effect. | [optional] 

### Return type

[**FileUploadResultWrapper**](FileUploadResultWrapper.md)

### Authorization

[Basic](../README.md#Basic), [OAuth2](../README.md#OAuth2), [ApiKeyBearer](../README.md#ApiKeyBearer), [asc_auth_key](../README.md#asc_auth_key), [Bearer](../README.md#Bearer), [OpenId](../README.md#OpenId)

### Example


```python
import docspace_api_sdk
from docspace_api_sdk.models.file_upload_result_wrapper import FileUploadResultWrapper
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
    userid = '00000000-0000-0000-0000-000000000000' # str | The profile whose avatar is uploaded, taken from the route. Either the ID of the account or its user name is  accepted, and it has to be the calling account, because a profile photo can only be changed by its owner.
    file = None # bytes | The image itself, sent as a multipart form field. It has to be a raster format the portal can read and stay  within the portal limit on image size; sending no file makes the operation answer with `success` false rather  than an error status.
    autosave = True # bool | Set it to true to make the uploaded image the avatar right away. With the default false the image is only  stored as a temporary file whose name comes back in `data`, and it has to be passed to  `POST api/2.0/people/{userid}/photo/thumbnails` to take effect. (optional)

    try:
        # Upload a user photo
        api_response = api_instance.upload_member_photo(userid, file, autosave=autosave)
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
**200** | The upload result: on success the photo URLs or the temporary file name in data, and on failure success set to false with the reason in message |  * X-RateLimit-Limit -  <br>  * X-RateLimit-Remaining -  <br>  * X-RateLimit-Reset -  <br>  |
**401** | Unauthorized |  -  |
**429** | Too Many Requests. |  * Retry-After -  <br>  |
**500** | Internal Server Error. |  -  |
**400** | Bad Request. |  -  |
**502** | Bad Gateway. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |
**503** | Service Unavailable. Returned by the reverse proxy, response body may be HTML and not JSON. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

