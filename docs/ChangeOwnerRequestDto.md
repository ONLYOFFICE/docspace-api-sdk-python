# ChangeOwnerRequestDto
The request parameters for changing the file owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of folder IDs to change the owner. | [optional] 
**file_ids** | [**List[BaseBatchRequestDtoFolderIdsInner]**](BaseBatchRequestDtoFolderIdsInner.md) | The list of file IDs to change the owner. | [optional] 
**user_id** | **str** | The new file owner ID. | 

## Example

```python
from docspace-api-sdk.models.change_owner_request_dto import ChangeOwnerRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ChangeOwnerRequestDto from a JSON string
change_owner_request_dto_instance = ChangeOwnerRequestDto.from_json(json)
# print the JSON string representation of the object
print(ChangeOwnerRequestDto.to_json())

# convert the object into a dict
change_owner_request_dto_dict = change_owner_request_dto_instance.to_dict()
# create an instance of ChangeOwnerRequestDto from a dict
change_owner_request_dto_from_dict = ChangeOwnerRequestDto.from_dict(change_owner_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


