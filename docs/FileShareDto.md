# FileShareDto
The file sharing information and access rights.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**shared_to** | **object** | The user who has the access to the specified file. | [optional] 
**shared_to_user** | [**EmployeeFullDto**](EmployeeFullDto.md) |  | [optional] 
**shared_to_group** | [**GroupSummaryDto**](GroupSummaryDto.md) |  | [optional] 
**shared_link** | [**FileShareLink**](FileShareLink.md) |  | [optional] 
**is_locked** | **bool** | Specifies if the access right is locked or not. | 
**is_owner** | **bool** | Specifies if the user is an owner of the specified file or not. | 
**can_edit_access** | **bool** | Specifies if the user can edit the access to the specified file or not. | 
**can_edit_internal** | **bool** | Indicates whether internal editing permissions are granted. | 
**can_edit_deny_download** | **bool** | Determines whether the user has permission to modify the deny download setting for the file share. | 
**can_edit_expiration_date** | **bool** | Indicates whether the expiration date of access permissions can be edited. | 
**can_revoke** | **bool** | Specifies whether the file sharing access can be revoked by the current user. | 
**subject_type** | [**SubjectType**](SubjectType.md) |  | 

## Example

```python
from docspace_api_sdk.models.file_share_dto import FileShareDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileShareDto from a JSON string
file_share_dto_instance = FileShareDto.from_json(json)
# print the JSON string representation of the object
print(FileShareDto.to_json())

# convert the object into a dict
file_share_dto_dict = file_share_dto_instance.to_dict()
# create an instance of FileShareDto from a dict
file_share_dto_from_dict = FileShareDto.from_dict(file_share_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


