# FolderDtoIntegerAvailableShareRights
The available external rights of the file entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | **List[str]** |  | [optional] 
**external_link** | **List[str]** |  | [optional] 
**group** | **List[str]** |  | [optional] 
**invitation_link** | **List[str]** |  | [optional] 
**primary_external_link** | **List[str]** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_dto_integer_available_share_rights import FolderDtoIntegerAvailableShareRights

# TODO update the JSON string below
json = "{}"
# create an instance of FolderDtoIntegerAvailableShareRights from a JSON string
folder_dto_integer_available_share_rights_instance = FolderDtoIntegerAvailableShareRights.from_json(json)
# print the JSON string representation of the object
print(FolderDtoIntegerAvailableShareRights.to_json())

# convert the object into a dict
folder_dto_integer_available_share_rights_dict = folder_dto_integer_available_share_rights_instance.to_dict()
# create an instance of FolderDtoIntegerAvailableShareRights from a dict
folder_dto_integer_available_share_rights_from_dict = FolderDtoIntegerAvailableShareRights.from_dict(folder_dto_integer_available_share_rights_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


