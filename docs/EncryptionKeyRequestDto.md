# EncryptionKeyRequestDto
The request parameters for storing the encryption key pair of a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The identifier of the key pair. | [optional] 
**public_key** | **str** | The public key of the pair, used to encrypt the file keys. | [optional] 
**private_key_enc** | **str** | The private key of the pair, encrypted with the user password. | [optional] 

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


