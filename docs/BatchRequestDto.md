# BatchRequestDto

Request parameters for copying/moving files

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | List of folder IDs | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | List of file IDs | [optional] 
**dest_folder_id** | [**BatchRequestDtoDestFolderId**](BatchRequestDtoDestFolderId.md) |  | [optional] 
**conflict_resolve_type** | [**FileConflictResolveType**](FileConflictResolveType.md) |  | [optional] 
**delete_after** | **bool** | Specifies whether to delete a folder after the editing session is finished or not | [optional] 
**content** | **bool** | Content | [optional] 

## Example

```python
from docspace.models.batch_request_dto import BatchRequestDto

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


