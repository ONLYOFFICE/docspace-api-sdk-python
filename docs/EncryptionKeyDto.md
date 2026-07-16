# EncryptionKeyDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** |  | [optional] 
**user_id** | **UUID** |  | [optional] 
**var_date** | **datetime** |  | [optional] 
**public_key** | **str** |  | [optional] 
**private_key_enc** | **str** |  | [optional] 
**crypto_engine_id** | **str** |  | [optional] 

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


