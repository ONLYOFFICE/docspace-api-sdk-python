# EncryptionKeysConfig
The encryption keys of the editor configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**crypto_engine_id** | **str** | The crypto engine ID of the encryption key. | [optional] [readonly] 
**private_key_enc** | **str** | The private key. | [optional] 
**public_key** | **str** | The public key. | [optional] 

## Example

```python
from docspace-api-sdk.models.encryption_keys_config import EncryptionKeysConfig

# TODO update the JSON string below
json = "{}"
# create an instance of EncryptionKeysConfig from a JSON string
encryption_keys_config_instance = EncryptionKeysConfig.from_json(json)
# print the JSON string representation of the object
print(EncryptionKeysConfig.to_json())

# convert the object into a dict
encryption_keys_config_dict = encryption_keys_config_instance.to_dict()
# create an instance of EncryptionKeysConfig from a dict
encryption_keys_config_from_dict = EncryptionKeysConfig.from_dict(encryption_keys_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


