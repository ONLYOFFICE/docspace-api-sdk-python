# ChunkedUploadSessionResponseWrapperInteger
Represents a wrapper for the response of a chunked upload session operation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Gets or sets a value indicating whether the operation was successful. | [optional] 
**data** | [**ChunkedUploadSessionResponseInteger**](ChunkedUploadSessionResponseInteger.md) | Represents the response returned from a chunked upload session. | [optional] 

## Example

```python
from docspace_api_sdk.models.chunked_upload_session_response_wrapper_integer import ChunkedUploadSessionResponseWrapperInteger

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkedUploadSessionResponseWrapperInteger from a JSON string
chunked_upload_session_response_wrapper_integer_instance = ChunkedUploadSessionResponseWrapperInteger.from_json(json)
# print the JSON string representation of the object
print(ChunkedUploadSessionResponseWrapperInteger.to_json())

# convert the object into a dict
chunked_upload_session_response_wrapper_integer_dict = chunked_upload_session_response_wrapper_integer_instance.to_dict()
# create an instance of ChunkedUploadSessionResponseWrapperInteger from a dict
chunked_upload_session_response_wrapper_integer_from_dict = ChunkedUploadSessionResponseWrapperInteger.from_dict(chunked_upload_session_response_wrapper_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


