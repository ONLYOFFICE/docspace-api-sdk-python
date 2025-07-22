# FileShareDto
The file sharing information and access rights.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access** | [**FileShare**](FileShare.md) |  | [optional] 
**shared_to** | **object** | The user who has the access to the specified file. | [optional] 
**is_locked** | **bool** | Specifies if the access right is locked or not. | [optional] 
**is_owner** | **bool** | Specifies if the user is an owner of the specified file or not. | [optional] 
**can_edit_access** | **bool** | Specifies if the user can edit the access to the specified file or not. | [optional] 
**subject_type** | [**SubjectType**](SubjectType.md) |  | [optional] 

## Example

```python
from docspace-api-sdk.models.file_share_dto import FileShareDto

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


