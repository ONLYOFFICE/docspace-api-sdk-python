# ChunkedUploadSessionResponseWrapperWrapper
The successful API response containing the ChunkedUploadSessionResponseWrapper object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ChunkedUploadSessionResponseWrapper**](ChunkedUploadSessionResponseWrapper.md) | The ChunkedUploadSessionResponseWrapper object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.chunked_upload_session_response_wrapper_wrapper import ChunkedUploadSessionResponseWrapperWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkedUploadSessionResponseWrapperWrapper from a JSON string
chunked_upload_session_response_wrapper_wrapper_instance = ChunkedUploadSessionResponseWrapperWrapper.from_json(json)
# print the JSON string representation of the object
print(ChunkedUploadSessionResponseWrapperWrapper.to_json())

# convert the object into a dict
chunked_upload_session_response_wrapper_wrapper_dict = chunked_upload_session_response_wrapper_wrapper_instance.to_dict()
# create an instance of ChunkedUploadSessionResponseWrapperWrapper from a dict
chunked_upload_session_response_wrapper_wrapper_from_dict = ChunkedUploadSessionResponseWrapperWrapper.from_dict(chunked_upload_session_response_wrapper_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


