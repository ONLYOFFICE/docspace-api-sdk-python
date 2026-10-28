# DeleteBatchRequestDto
The files and folders to delete, and how final the deletion is.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Which operations the answer carries: `true` returns the operation this call started and nothing else, `false`  returns every operation of the same kind that the caller has running or unread. When nothing was queued, which  happens for an empty selection, `true` falls back to the full list. | [optional] 
**folder_ids** | [**List[DeleteBatchRequestDtoAllOfFolderIds]**](DeleteBatchRequestDtoAllOfFolderIds.md) | The folders to delete, by id, each with everything it contains. A number addresses a folder stored in the  portal itself, a string addresses a folder on a connected third-party account, and both kinds may be sent in  one list. | [optional] 
**file_ids** | [**List[DeleteBatchRequestDtoAllOfFileIds]**](DeleteBatchRequestDtoAllOfFileIds.md) | The files to delete, by id. A number addresses a file stored in the portal itself, a string addresses a file  on a connected third-party account, and both kinds may be sent in one list. | [optional] 
**delete_after** | **bool** | Whether the finished operation is still reported: `false` keeps its final record readable through  `GET api/2.0/files/fileops` until it has been read once, `true` drops the record as soon as the work is done.  It does not postpone the deletion and does not delete anything of its own. | [optional] 
**immediately** | **bool** | Where the deleted items go: `false` moves them to the Trash of the caller, from which they can be restored,  `true` removes them at once and for good. | [optional] 

## Example

```python
from docspace_api_sdk.models.delete_batch_request_dto import DeleteBatchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteBatchRequestDto from a JSON string
delete_batch_request_dto_instance = DeleteBatchRequestDto.from_json(json)
# print the JSON string representation of the object
print(DeleteBatchRequestDto.to_json())

# convert the object into a dict
delete_batch_request_dto_dict = delete_batch_request_dto_instance.to_dict()
# create an instance of DeleteBatchRequestDto from a dict
delete_batch_request_dto_from_dict = DeleteBatchRequestDto.from_dict(delete_batch_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


