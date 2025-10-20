# FileDtoInteger
The file parameters.

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
**folder_id** | **int** | The folder ID where the file is located. | [optional] 
**version** | **int** | The file version. | [optional] 
**version_group** | **int** | The version group of the file. | [optional] 
**content_length** | **str** | The content length of the file. | [optional] 
**pure_content_length** | **int** | The pure content length of the file. | [optional] 
**file_status** | [**FileStatus**](FileStatus.md) |  | [optional] 
**mute** | **bool** | Specifies if the file is muted or not. | [optional] 
**view_url** | **str** | The URL link to view the file. | [optional] 
**web_url** | **str** | The Web URL link to the file. | [optional] 
**file_type** | [**FileType**](FileType.md) |  | [optional] 
**file_exst** | **str** | The file extension. | [optional] 
**comment** | **str** | The comment to the file. | [optional] 
**encrypted** | **bool** | Specifies if the file is encrypted or not. | [optional] 
**thumbnail_url** | **str** | The thumbnail URL of the file. | [optional] 
**thumbnail_status** | [**Thumbnail**](Thumbnail.md) |  | [optional] 
**locked** | **bool** | Specifies if the file is locked or not. | [optional] 
**locked_by** | **str** | The user ID of the person who locked the file. | [optional] 
**has_draft** | **bool** | Specifies if the file has a draft or not. | [optional] 
**form_filling_status** | [**FormFillingStatus**](FormFillingStatus.md) |  | [optional] 
**is_form** | **bool** | Specifies if the file is a form or not. | [optional] 
**custom_filter_enabled** | **bool** | Specifies if the Custom Filter editing mode is enabled for a file or not. | [optional] 
**custom_filter_enabled_by** | **str** | The name of the user who enabled a Custom Filter editing mode for a file. | [optional] 
**start_filling** | **bool** | Specifies if the filling has started or not. | [optional] 
**in_process_folder_id** | **int** | The InProcess folder ID of the file. | [optional] 
**in_process_folder_title** | **str** | The InProcess folder title of the file. | [optional] 
**draft_location** | [**DraftLocationInteger**](DraftLocationInteger.md) |  | [optional] 
**view_accessibility** | [**FileDtoIntegerAllOfViewAccessibility**](FileDtoIntegerAllOfViewAccessibility.md) |  | [optional] 
**last_opened** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**expired** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_dto_integer import FileDtoInteger

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


