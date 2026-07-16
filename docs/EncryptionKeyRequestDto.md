# EncryptionKeyRequestDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**public_key** | **str** |  | [optional] 
**private_key_enc** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.encryption_key_request_dto import EncryptionKeyRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyRequestDto from a JSON string
encryption_key_request_dto_instance = EncryptionKeyRequestDto.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyRequestDto.to_json())

# convert the object into a dict
encryption_key_request_dto_dict = encryption_key_request_dto_instance.to_dict()
# create an instance of EncryptionKeyRequestDto from a dict
encryption_key_request_dto_from_dict = EncryptionKeyRequestDto.from_dict(encryption_key_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


