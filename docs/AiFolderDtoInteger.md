# AiFolderDtoInteger
The folder parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The file entry title. | [optional] 
**access** | [**AiFileShare**](AiFileShare.md) | The access rights to the file entry. | [optional] 
**shared_by** | [**AiEmployeeDto**](AiEmployeeDto.md) | Provides information about the employee who shared the file or folder. | [optional] 
**owned_by** | [**AiEmployeeDto**](AiEmployeeDto.md) | The information about the employee who owns the file entry. | [optional] 
**shared** | **bool** | Specifies if the file entry is shared via link or not. | [optional] 
**shared_for_user** | **bool** | Specifies if the file entry is shared for user or not. | [optional] 
**shared_external** | **bool** | Specifies if the file entry is shared via a public (non-internal) external link. | [optional] 
**parent_shared** | **bool** | Indicates whether the parent entity is shared. | [optional] 
**short_web_url** | **str** | The short Web URL. | [optional] 
**created** | [**AiApiDateTime**](AiApiDateTime.md) | The creation date and time of the file entry. | [optional] 
**created_by** | [**AiEmployeeDto**](AiEmployeeDto.md) | The file entry author. | [optional] 
**updated** | [**AiApiDateTime**](AiApiDateTime.md) | The last date and time when the file entry was updated. | [optional] 
**auto_delete** | [**AiApiDateTime**](AiApiDateTime.md) | The date and time when the file entry will be automatically deleted. | [optional] 
**root_folder_type** | [**AiFolderType**](AiFolderType.md) | The root folder type of the file entry. | [optional] 
**parent_room_type** | [**AiFolderType**](AiFolderType.md) | The parent room type of the file entry. | [optional] 
**updated_by** | [**AiEmployeeDto**](AiEmployeeDto.md) | The user who updated the file entry. | [optional] 
**provider_item** | **bool** | Specifies if the file entry provider is specified or not. | [optional] 
**provider_key** | **str** | The provider key of the file entry. | [optional] 
**provider_id** | **int** | The provider ID of the file entry. | [optional] 
**order** | **str** | The order of the file entry. | [optional] 
**is_favorite** | **bool** | Specifies if the file is a favorite or not. | [optional] 
**file_entry_type** | [**AiFileEntryType**](AiFileEntryType.md) | The file entry type. | [optional] 
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
**expiration_date** | [**AiApiDateTime**](AiApiDateTime.md) | Represents the expiration date of the file entry. | [optional] 
**is_link_expired** | **bool** | Indicates whether the shareable link associated with the file or folder has expired. | [optional] 
**parent_id** | **int** | The parent folder ID of the folder. | [optional] 
**files_count** | **int** | The number of files that the folder contains. | [optional] 
**folders_count** | **int** | The number of folders that the folder contains. | [optional] 
**is_shareable** | **bool** | Specifies if the folder can be shared or not. | [optional] 
**new** | **int** | The new element index in the folder. | [optional] 
**mute** | **bool** | Specifies if the folder notifications are enabled or not. | [optional] 
**tags** | **List[str]** | The list of tags of the folder. | [optional] 
**logo** | [**AiLogo**](AiLogo.md) | The folder logo. | [optional] 
**pinned** | **bool** | Specifies if the folder is pinned or not. | [optional] 
**room_type** | [**AiRoomType**](AiRoomType.md) | The room type of the folder. | [optional] 
**private** | **bool** | Specifies if the folder is private or not. | [optional] 
**indexing** | **bool** | Specifies if the folder is indexed or not. | [optional] 
**deny_download** | **bool** | Specifies if the folder can be downloaded or not. | [optional] 
**lifetime** | [**AiRoomDataLifetimeDto**](AiRoomDataLifetimeDto.md) | The room data lifetime settings of the folder. | [optional] 
**watermark** | [**AiWatermarkDto**](AiWatermarkDto.md) | The watermark settings of the folder. | [optional] 
**type** | [**AiFolderType**](AiFolderType.md) | The folder type. | [optional] 
**in_room** | **bool** | Specifies if the folder is placed in the room or not. | [optional] 
**quota_limit** | **int** | The folder quota limit. | [optional] 
**is_custom_quota** | **bool** | Specifies if the folder room has a custom quota or not. | [optional] 
**used_space** | **int** | How much folder space is used (counter). | [optional] 
**password_protected** | **bool** | Specifies if the folder is password protected or not. | [optional] 
**expired** | **bool** | Specifies if an external link to the folder is expired or not. | [optional] 
**chat_settings** | [**AiChatSettingsDto**](AiChatSettingsDto.md) | The AI chat settings for the folder room. Contains configuration for AI provider, model selection, and custom prompts.  Only applicable to rooms with AI chat functionality enabled. Null if the room does not have chat settings configured. | [optional] 
**root_room_type** | [**AiRoomType**](AiRoomType.md) | The room type of the root folder. Indicates the type of the parent room if the current folder is nested within a room hierarchy.  This property helps identify the context in which a nested folder exists. | [optional] 
**save_form_as_xlsx** | **bool** | Specifies whether to save form data as XLSX file. | [optional] 
**send_form_to_external_db** | **bool** | Specifies whether to send form data to external database. | [optional] 
**original_form_id** | **int** | The original form ID that corresponds to this FormFillingFolderDone folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_folder_dto_integer import AiFolderDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of AiFolderDtoInteger from a JSON string
ai_folder_dto_integer_instance = AiFolderDtoInteger.from_json(json)
# print the JSON string representation of the object
print(AiFolderDtoInteger.to_json())

# convert the object into a dict
ai_folder_dto_integer_dict = ai_folder_dto_integer_instance.to_dict()
# create an instance of AiFolderDtoInteger from a dict
ai_folder_dto_integer_from_dict = AiFolderDtoInteger.from_dict(ai_folder_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


