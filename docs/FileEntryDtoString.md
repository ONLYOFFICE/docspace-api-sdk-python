# FileEntryDtoString
The generic file entry information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The file entry title. | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**shared** | **bool** | Specifies if the file entry is shared via link or not. | [optional] 
**shared_for_user** | **bool** | Specifies if the file entry is shared for user or not. | [optional] 
**parent_shared** | **bool** | Indicates whether the parent entity is shared. | [optional] 
**short_web_url** | **str** | The short Web URL. | [optional] 
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
**is_favorite** | **bool** | Specifies if the file is a favorite or not. | [optional] 
**file_entry_type** | [**FileEntryType**](FileEntryType.md) |  | [optional] 
**id** | **str** | The file entry ID. | [optional] 
**root_folder_id** | **str** | The root folder ID of the file entry. | [optional] 
**origin_id** | **str** | The origin ID of the file entry. | [optional] 
**origin_room_id** | **str** | The origin room ID of the file entry. | [optional] 
**origin_title** | **str** | The origin title of the file entry. | [optional] 
**origin_room_title** | **str** | The origin room title of the file entry. | [optional] 
**can_share** | **bool** | Specifies if the file entry can be shared or not. | [optional] 
**share_settings** | [**FileEntryDtoIntegerAllOfShareSettings**](FileEntryDtoIntegerAllOfShareSettings.md) |  | [optional] 
**security** | [**FileEntryDtoIntegerAllOfSecurity**](FileEntryDtoIntegerAllOfSecurity.md) |  | [optional] 
**available_share_rights** | [**FileEntryDtoIntegerAllOfAvailableShareRights**](FileEntryDtoIntegerAllOfAvailableShareRights.md) |  | [optional] 
**request_token** | **str** | The request token of the file entry. | [optional] 
**external** | **bool** | Specifies if the folder can be accessed via an external link or not. | [optional] 
**expiration_date** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**is_link_expired** | **bool** | Indicates whether the shareable link associated with the file or folder has expired. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_entry_dto_string import FileEntryDtoString

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryDtoString from a JSON string
file_entry_dto_string_instance = FileEntryDtoString.from_json(json)
# print the JSON string representation of the object
print(FileEntryDtoString.to_json())

# convert the object into a dict
file_entry_dto_string_dict = file_entry_dto_string_instance.to_dict()
# create an instance of FileEntryDtoString from a dict
file_entry_dto_string_from_dict = FileEntryDtoString.from_dict(file_entry_dto_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


