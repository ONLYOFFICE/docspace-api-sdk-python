# DuplicateRequestDto
The duplicate request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Specifies whether to return only the current operation | [optional] 
**folder_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of folder IDs. | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of file IDs. | [optional] 

## Example

```python
from docspace-api-python.models.duplicate_request_dto import DuplicateRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DuplicateRequestDto from a JSON string
duplicate_request_dto_instance = DuplicateRequestDto.from_json(json)
# print the JSON string representation of the object
print(DuplicateRequestDto.to_json())

# convert the object into a dict
duplicate_request_dto_dict = duplicate_request_dto_instance.to_dict()
# create an instance of DuplicateRequestDto from a dict
duplicate_request_dto_from_dict = DuplicateRequestDto.from_dict(duplicate_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


