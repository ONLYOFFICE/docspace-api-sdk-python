# AiFileEntryDtoInteger
The generic file entry information.

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

## Example

```python
from docspace_api_sdk.models.ai_file_entry_dto_integer import AiFileEntryDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of AiFileEntryDtoInteger from a JSON string
ai_file_entry_dto_integer_instance = AiFileEntryDtoInteger.from_json(json)
# print the JSON string representation of the object
print(AiFileEntryDtoInteger.to_json())

# convert the object into a dict
ai_file_entry_dto_integer_dict = ai_file_entry_dto_integer_instance.to_dict()
# create an instance of AiFileEntryDtoInteger from a dict
ai_file_entry_dto_integer_from_dict = AiFileEntryDtoInteger.from_dict(ai_file_entry_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


