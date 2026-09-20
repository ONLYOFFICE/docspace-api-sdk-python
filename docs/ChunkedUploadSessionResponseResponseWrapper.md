# ChunkedUploadSessionResponseResponseWrapper
The successful API response containing the ChunkedUploadSessionResponse object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ChunkedUploadSessionResponse**](ChunkedUploadSessionResponse.md) | The ChunkedUploadSessionResponse object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.chunked_upload_session_response_response_wrapper import ChunkedUploadSessionResponseResponseWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkedUploadSessionResponseResponseWrapper from a JSON string
chunked_upload_session_response_response_wrapper_instance = ChunkedUploadSessionResponseResponseWrapper.from_json(json)
# print the JSON string representation of the object
print(ChunkedUploadSessionResponseResponseWrapper.to_json())

# convert the object into a dict
chunked_upload_session_response_response_wrapper_dict = chunked_upload_session_response_response_wrapper_instance.to_dict()
# create an instance of ChunkedUploadSessionResponseResponseWrapper from a dict
chunked_upload_session_response_response_wrapper_from_dict = ChunkedUploadSessionResponseResponseWrapper.from_dict(chunked_upload_session_response_response_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


