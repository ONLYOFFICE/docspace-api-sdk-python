# FileEncryptionInfoDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_keys** | [**List[EncryptionKeyDto]**](EncryptionKeyDto.md) |  | [optional] 
**file_keys** | [**List[FileKeys]**](FileKeys.md) |  | [optional] 

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


