# DeleteBatchRequestDto
The request parameters for deleting files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Specifies whether to return only the current operation | [optional] 
**folder_ids** | [**List[DeleteBatchRequestDtoAllOfFolderIds]**](DeleteBatchRequestDtoAllOfFolderIds.md) | The list of folder IDs to be deleted. | [optional] 
**file_ids** | [**List[DeleteBatchRequestDtoAllOfFileIds]**](DeleteBatchRequestDtoAllOfFileIds.md) | The list of file IDs to be deleted. | [optional] 
**delete_after** | **bool** | Specifies whether to delete a file after the editing session is finished or not | [optional] 
**immediately** | **bool** | Specifies whether to move a file to the \\\&quot;Trash\\\&quot; folder or delete it immediately. | [optional] 

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


