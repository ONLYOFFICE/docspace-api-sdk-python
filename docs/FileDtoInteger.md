# FileDtoInteger


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
**folder_id** | **int** | Folder ID | [optional] 
**version** | **int** | Version | [optional] 
**version_group** | **int** | Version group | [optional] 
**content_length** | **str** | Content length | [optional] 
**pure_content_length** | **int** | Pure content length | [optional] 
**file_status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**mute** | **bool** | Muted or not | [optional] 
**view_url** | **str** | URL to view a file | [optional] 
**web_url** | **str** | Web URL | [optional] 
**file_type** | [**FileType**](FileType.md) |  | [optional] 
**file_exst** | **str** | File extension | [optional] 
**comment** | **str** | Comment | [optional] 
**encrypted** | **bool** | Encrypted or not | [optional] 
**thumbnail_url** | **str** | Thumbnail URL | [optional] 
**thumbnail_status** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**locked** | **bool** | Locked or not | [optional] 
**locked_by** | **str** | User ID who locked a file | [optional] 
**has_draft** | **bool** | Is there a draft or not | [optional] 
**is_form** | **bool** | Is there a form or not | [optional] 
**start_filling** | **bool** | Specifies if the filling has started or not | [optional] 
**in_process_folder_id** | **int** | InProcess folder ID | [optional] 
**in_process_folder_title** | **str** | InProcess folder title | [optional] 
**draft_location** | [**DraftLocationInteger**](DraftLocationInteger.md) |  | [optional] 
**view_accessibility** | [**FileDtoIntegerViewAccessibility**](FileDtoIntegerViewAccessibility.md) |  | [optional] 
**available_external_rights** | **Dict[str, bool]** | Available external rights | [optional] 
**last_opened** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**expired** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**file_entry_type** | [**FileEntryType**](FileEntryType.md) |  | [optional] 

## Example

```python
from docspace.models.file_dto_integer import FileDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of FileDtoInteger from a JSON string
file_dto_integer_instance = FileDtoInteger.from_json(json)
# print the JSON string representation of the object
print(FileDtoInteger.to_json())

# convert the object into a dict
file_dto_integer_dict = file_dto_integer_instance.to_dict()
# create an instance of FileDtoInteger from a dict
file_dto_integer_from_dict = FileDtoInteger.from_dict(file_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


