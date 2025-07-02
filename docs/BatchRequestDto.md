# BatchRequestDto
The request parameters for copying/moving files.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Specifies whether to return only the current operation | [optional] 
**folder_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of folder IDs to be copied/moved. | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of file IDs to be copied/moved. | [optional] 
**dest_folder_id** | [**BatchRequestDtoDestFolderId**](BatchRequestDtoDestFolderId.md) |  | [optional] 
**conflict_resolve_type** | [**FileConflictResolveType**](FileConflictResolveType.md) |  | [optional] 
**delete_after** | **bool** | Specifies whether to delete the source files/folders after they are moved or copied to the destination folder. | [optional] 
**content** | **bool** | Specifies whether to copy or move the folder content or not. | [optional] 
**to_fill_out** | **bool** | Specifies whether the file is copied for filling out | [optional] 

## Example

```python
from docspace-api-python.models.batch_request_dto import BatchRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of BatchRequestDto from a JSON string
batch_request_dto_instance = BatchRequestDto.from_json(json)
# print the JSON string representation of the object
print(BatchRequestDto.to_json())

# convert the object into a dict
batch_request_dto_dict = batch_request_dto_instance.to_dict()
# create an instance of BatchRequestDto from a dict
batch_request_dto_from_dict = BatchRequestDto.from_dict(batch_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


