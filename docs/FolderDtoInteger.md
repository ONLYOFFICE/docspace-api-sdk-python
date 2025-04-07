# FolderDtoInteger


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title | [optional] 
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**shared** | **bool** | Specifies if the file is shared or not | [optional] 
**created** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**created_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**updated** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**auto_delete** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**root_folder_type** | [**FolderType**](FolderType.md) |  | [optional] 
**parent_room_type** | [**FolderType**](FolderType.md) |  | [optional] 
**updated_by** | [**EmployeeDto**](EmployeeDto.md) |  | [optional] 
**provider_item** | **bool** | Provider is specified or not | [optional] 
**provider_key** | **str** | Provider key | [optional] 
**provider_id** | **int** | Provider ID | [optional] 
**order** | **str** | Order | [optional] 
**id** | **int** | Id | [optional] 
**root_folder_id** | **int** | Root folder id | [optional] 
**origin_id** | **int** | Origin id | [optional] 
**origin_room_id** | **int** | Origin room id | [optional] 
**origin_title** | **str** | Origin title | [optional] 
**origin_room_title** | **str** | Origin room title | [optional] 
**can_share** | **bool** | Can share | [optional] 
**security** | [**FileDtoIntegerSecurity**](FileDtoIntegerSecurity.md) |  | [optional] 
**request_token** | **str** |  | [optional] 
**parent_id** | **int** | Parent folder ID | [optional] 
**files_count** | **int** | Number of files | [optional] 
**folders_count** | **int** | Number of folders | [optional] 
**is_shareable** | **bool** | Specifies if a folder is shareable or not | [optional] 
**is_favorite** | **bool** | Specifies if a folder is favorite or not | [optional] 
**new** | **int** | Number for a new folder | [optional] 
**mute** | **bool** | Specifies if a folder is muted or not | [optional] 
**tags** | **List[str]** | List of tags | [optional] 
**logo** | [**Logo**](Logo.md) |  | [optional] 
**pinned** | **bool** | Specifies if a folder is pinned or not | [optional] 
**room_type** | [**RoomType**](RoomType.md) |  | [optional] 
**private** | **bool** | Specifies if a folder is private or not | [optional] 
**indexing** | **bool** | Indexing | [optional] 
**deny_download** | **bool** | Deny download | [optional] 
**lifetime** | [**RoomDataLifetimeDto**](RoomDataLifetimeDto.md) |  | [optional] 
**watermark** | [**WatermarkDto**](WatermarkDto.md) |  | [optional] 
**type** | [**FolderType**](FolderType.md) |  | [optional] 
**in_room** | **bool** | InRoom | [optional] 
**quota_limit** | **int** | Quota | [optional] 
**is_custom_quota** | **bool** | Specifies if the room has a custom quota or not | [optional] 
**used_space** | **int** | Counter | [optional] 
**external** | **bool** | Specifies if the link external | [optional] 
**password_protected** | **bool** | Specifies if the password protected | [optional] 
**expired** | **bool** | Expired | [optional] 
**file_entry_type** | [**FileEntryType**](FileEntryType.md) |  | [optional] 

## Example

```python
from docspace.models.folder_dto_integer import FolderDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of FolderDtoInteger from a JSON string
folder_dto_integer_instance = FolderDtoInteger.from_json(json)
# print the JSON string representation of the object
print(FolderDtoInteger.to_json())

# convert the object into a dict
folder_dto_integer_dict = folder_dto_integer_instance.to_dict()
# create an instance of FolderDtoInteger from a dict
folder_dto_integer_from_dict = FolderDtoInteger.from_dict(folder_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


