# FileEntryDto

The file entry information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The file entry title. | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**shared** | **bool** | Specifies if the file entry is shared or not. | [optional] 
**created** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**updated** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**auto_delete** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**root_folder_type** | [**FolderType**](FolderType.md) |  | [optional] 
**parent_room_type** | [**FolderType**](FolderType.md) |  | [optional] 
**updated_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**provider_item** | **bool** | Specifies if the file entry provider is specified or not. | [optional] 
**provider_key** | **str** | The provider key of the file entry. | [optional] 
**provider_id** | **int** | The provider ID of the file entry. | [optional] 
**order** | **str** | The order of the file entry. | [optional] 
**file_entry_type** | [**FileEntryType**](FileEntryType.md) |  | [optional] 

## Example

```python
from docspace.models.file_entry_dto import FileEntryDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryDto from a JSON string
file_entry_dto_instance = FileEntryDto.from_json(json)
# print the JSON string representation of the object
print(FileEntryDto.to_json())

# convert the object into a dict
file_entry_dto_dict = file_entry_dto_instance.to_dict()
# create an instance of FileEntryDto from a dict
file_entry_dto_from_dict = FileEntryDto.from_dict(file_entry_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


