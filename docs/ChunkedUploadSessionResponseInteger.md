# ChunkedUploadSessionResponseInteger
Represents the response returned from a chunked upload session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier for the entity. | [optional] 
**path** | **List[int]** | Represents the hierarchical path of folders associated with a chunked upload session. | [optional] 
**created** | **datetime** | The timestamp indicating when the chunked upload session was created. | [optional] 
**expired** | **datetime** | The date and time when the chunked upload session is set to expire. | [optional] 
**location** | **str** | Represents the URI or path of the chunked upload session's current location. | [optional] 
**bytes_total** | **int** | The total size, in bytes, of the file being uploaded in the chunked upload session. | [optional] 

## Example

```python
from docspace_api_sdk.models.chunked_upload_session_response_integer import ChunkedUploadSessionResponseInteger

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkedUploadSessionResponseInteger from a JSON string
chunked_upload_session_response_integer_instance = ChunkedUploadSessionResponseInteger.from_json(json)
# print the JSON string representation of the object
print(ChunkedUploadSessionResponseInteger.to_json())

# convert the object into a dict
chunked_upload_session_response_integer_dict = chunked_upload_session_response_integer_instance.to_dict()
# create an instance of ChunkedUploadSessionResponseInteger from a dict
chunked_upload_session_response_integer_from_dict = ChunkedUploadSessionResponseInteger.from_dict(chunked_upload_session_response_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


