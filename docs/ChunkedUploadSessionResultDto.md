# ChunkedUploadSessionResultDto
The reserved chunked upload wrapped in the envelope the two older session operations answer with.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Always true in a body that reaches the caller, because a call that does not succeed answers with an error  status and no body at all. It cannot be used to tell a refusal from a success. | [optional] 
**data** | [**ChunkedUploadSessionDto**](ChunkedUploadSessionDto.md) | The reserved upload itself, in the same shape the newer session operations answer with directly. | [optional] 

## Example

```python
from docspace_api_sdk.models.chunked_upload_session_result_dto import ChunkedUploadSessionResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChunkedUploadSessionResultDto from a JSON string
chunked_upload_session_result_dto_instance = ChunkedUploadSessionResultDto.from_json(json)
# print the JSON string representation of the object
print(ChunkedUploadSessionResultDto.to_json())

# convert the object into a dict
chunked_upload_session_result_dto_dict = chunked_upload_session_result_dto_instance.to_dict()
# create an instance of ChunkedUploadSessionResultDto from a dict
chunked_upload_session_result_dto_from_dict = ChunkedUploadSessionResultDto.from_dict(chunked_upload_session_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


