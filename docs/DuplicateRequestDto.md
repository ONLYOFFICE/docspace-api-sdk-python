# DuplicateRequestDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | List of folder IDs | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | List of file IDs | [optional] 

## Example

```python
from docspace.models.duplicate_request_dto import DuplicateRequestDto

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


