# EncryptionKeyDto
The encryption key pair of a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | The identifier of the key pair. | [optional] 
**user_id** | **UUID** | The identifier of the user the key pair belongs to. | [optional] 
**var_date** | **datetime** | The date and time when the key pair was created. | [optional] 
**public_key** | **str** | The public key of the pair, used to encrypt the file keys. | [optional] 
**private_key_enc** | **str** | The private key of the pair, encrypted with the user password. | [optional] 
**crypto_engine_id** | **str** | The identifier of the crypto engine the key pair was issued for. | [optional] 

## Example

```python
from docspace_api_sdk.models.encryption_key_dto import EncryptionKeyDto

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeyDto from a JSON string
encryption_key_dto_instance = EncryptionKeyDto.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeyDto.to_json())

# convert the object into a dict
encryption_key_dto_dict = encryption_key_dto_instance.to_dict()
# create an instance of EncryptionKeyDto from a dict
encryption_key_dto_from_dict = EncryptionKeyDto.from_dict(encryption_key_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


