# AiFileEntryBaseDto
The file entry information.

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
**created** | **datetime** | The creation date and time of the file entry. | [optional] 
**created_by** | [**AiEmployeeDto**](AiEmployeeDto.md) | The file entry author. | [optional] 
**updated** | **datetime** | The last date and time when the file entry was updated. | [optional] 
**auto_delete** | **datetime** | The date and time when the file entry will be automatically deleted. | [optional] 
**root_folder_type** | [**AiFolderType**](AiFolderType.md) | The root folder type of the file entry. | [optional] 
**parent_room_type** | [**AiFolderType**](AiFolderType.md) | The parent room type of the file entry. | [optional] 
**updated_by** | [**AiEmployeeDto**](AiEmployeeDto.md) | The user who updated the file entry. | [optional] 
**provider_item** | **bool** | Specifies if the file entry provider is specified or not. | [optional] 
**provider_key** | **str** | The provider key of the file entry. | [optional] 
**provider_id** | **int** | The provider ID of the file entry. | [optional] 
**order** | **str** | The order of the file entry. | [optional] 
**is_favorite** | **bool** | Specifies if the file is a favorite or not. | [optional] 
**file_entry_type** | [**AiFileEntryType**](AiFileEntryType.md) | The file entry type. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_file_entry_base_dto import AiFileEntryBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiFileEntryBaseDto from a JSON string
ai_file_entry_base_dto_instance = AiFileEntryBaseDto.from_json(json)
# print the JSON string representation of the object
print(AiFileEntryBaseDto.to_json())

# convert the object into a dict
ai_file_entry_base_dto_dict = ai_file_entry_base_dto_instance.to_dict()
# create an instance of AiFileEntryBaseDto from a dict
ai_file_entry_base_dto_from_dict = AiFileEntryBaseDto.from_dict(ai_file_entry_base_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


