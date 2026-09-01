# FileEncryptionInfoDto
The encryption information of a file: the user key pairs and the per-user file keys.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_keys** | [**List[EncryptionKeyDto]**](EncryptionKeyDto.md) | The key pairs of the users who have access to the file. | [optional] 
**file_keys** | [**List[FileKeys]**](FileKeys.md) | The file keys issued to those users. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_encryption_info_dto import FileEncryptionInfoDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileEncryptionInfoDto from a JSON string
file_encryption_info_dto_instance = FileEncryptionInfoDto.from_json(json)
# print the JSON string representation of the object
print(FileEncryptionInfoDto.to_json())

# convert the object into a dict
file_encryption_info_dto_dict = file_encryption_info_dto_instance.to_dict()
# create an instance of FileEncryptionInfoDto from a dict
file_encryption_info_dto_from_dict = FileEncryptionInfoDto.from_dict(file_encryption_info_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


