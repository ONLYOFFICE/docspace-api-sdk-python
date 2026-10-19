# FileKeysDto
The encrypted file key issued to one user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **UUID** | The identifier of the user the file key was issued to. | [optional] 
**public_key_id** | **UUID** | The identifier of the key pair the file key is encrypted for. | [optional] 
**private_key_enc** | **str** | The file key, encrypted with the public key of the pair. | [optional] 
**tenant_id** | **int** | The identifier of the portal the file belongs to. | [optional] 
**file_id** | **int** | The identifier of the file the key unlocks. | [optional] 
**create_on** | **datetime** | The date and time when the file key was issued. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_keys_dto import FileKeysDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileKeysDto from a JSON string
file_keys_dto_instance = FileKeysDto.from_json(json)
# print the JSON string representation of the object
print(FileKeysDto.to_json())

# convert the object into a dict
file_keys_dto_dict = file_keys_dto_instance.to_dict()
# create an instance of FileKeysDto from a dict
file_keys_dto_from_dict = FileKeysDto.from_dict(file_keys_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


