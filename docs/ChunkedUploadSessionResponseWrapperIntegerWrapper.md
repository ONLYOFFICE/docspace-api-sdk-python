# ChunkedUploadSessionResponseWrapperIntegerWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ChunkedUploadSessionResponseWrapperInteger**](ChunkedUploadSessionResponseWrapperInteger.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.chunked_upload_session_response_wrapper_integer_wrapper import ChunkedUploadSessionResponseWrapperIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkedUploadSessionResponseWrapperIntegerWrapper from a JSON string
chunked_upload_session_response_wrapper_integer_wrapper_instance = ChunkedUploadSessionResponseWrapperIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(ChunkedUploadSessionResponseWrapperIntegerWrapper.to_json())

# convert the object into a dict
chunked_upload_session_response_wrapper_integer_wrapper_dict = chunked_upload_session_response_wrapper_integer_wrapper_instance.to_dict()
# create an instance of ChunkedUploadSessionResponseWrapperIntegerWrapper from a dict
chunked_upload_session_response_wrapper_integer_wrapper_from_dict = ChunkedUploadSessionResponseWrapperIntegerWrapper.from_dict(chunked_upload_session_response_wrapper_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


