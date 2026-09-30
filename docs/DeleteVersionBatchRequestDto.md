# DeleteVersionBatchRequestDto
The file whose versions are deleted, and the versions to delete.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Which operations the answer carries: `true` returns the operation this call started and nothing else, `false`  returns every operation of the same kind that the caller has running or unread. When nothing was queued, which  happens for an empty selection, `true` falls back to the full list. | [optional] 
**delete_after** | **bool** | Whether the finished operation is still reported: `false` keeps its final record readable through  `GET api/2.0/files/fileops` until it has been read once, `true` drops the record as soon as the work is done.  It does not postpone the deletion and does not delete anything of its own. | [optional] 
**file_id** | **int** | The file whose history the versions are taken from; only files stored in the portal itself are addressed here. | 
**versions** | **List[int]** | The version numbers to remove, as reported by `GET api/2.0/files/file/{fileId}/history`. At least one number  has to be sent: an empty list removes the file itself instead of one of its versions. The number of the  current version is refused outright, while a number that no longer exists is passed over without a complaint. | 

## Example

```python
from docspace_api_sdk.models.delete_version_batch_request_dto import DeleteVersionBatchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteVersionBatchRequestDto from a JSON string
delete_version_batch_request_dto_instance = DeleteVersionBatchRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeleteVersionBatchRequestDto.to_json())

# convert the object into a dict
delete_version_batch_request_dto_dict = delete_version_batch_request_dto_instance.to_dict()
# create an instance of DeleteVersionBatchRequestDto from a dict
delete_version_batch_request_dto_from_dict = DeleteVersionBatchRequestDto.from_dict(delete_version_batch_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


