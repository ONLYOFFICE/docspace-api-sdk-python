# FolderDtoInteger
The folder parameters.

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
**id** | **int** | The file entry ID. | [optional] 
**root_folder_id** | **int** | The root folder ID of the file entry. | [optional] 
**origin_id** | **int** | The origin ID of the file entry. | [optional] 
**origin_room_id** | **int** | The origin room ID of the file entry. | [optional] 
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
**parent_id** | **int** | The parent folder ID of the folder. | [optional] 
**files_count** | **int** | The number of files that the folder contains. | [optional] 
**folders_count** | **int** | The number of folders that the folder contains. | [optional] 
**is_shareable** | **bool** | Specifies if the folder can be shared or not. | [optional] 
**new** | **int** | The new element index in the folder. | [optional] 
**mute** | **bool** | Specifies if the folder notifications are enabled or not. | [optional] 
**tags** | **List[str]** | The list of tags of the folder. | [optional] 
**logo** | [**Logo**](Logo.md) |  | [optional] 
**pinned** | **bool** | Specifies if the folder is pinned or not. | [optional] 
**room_type** | [**RoomType**](RoomType.md) |  | [optional] 
**private** | **bool** | Specifies if the folder is private or not. | [optional] 
**indexing** | **bool** | Specifies if the folder is indexed or not. | [optional] 
**deny_download** | **bool** | Specifies if the folder can be downloaded or not. | [optional] 
**lifetime** | [**RoomDataLifetimeDto**](RoomDataLifetimeDto.md) |  | [optional] 
**watermark** | [**WatermarkDto**](WatermarkDto.md) |  | [optional] 
**type** | [**FolderType**](FolderType.md) |  | [optional] 
**in_room** | **bool** | Specifies if the folder is placed in the room or not. | [optional] 
**quota_limit** | **int** | The folder quota limit. | [optional] 
**is_custom_quota** | **bool** | Specifies if the folder room has a custom quota or not. | [optional] 
**used_space** | **int** | How much folder space is used (counter). | [optional] 
**password_protected** | **bool** | Specifies if the folder is password protected or not. | [optional] 
**expired** | **bool** | Specifies if an external link to the folder is expired or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.folder_dto_integer import FolderDtoInteger

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


