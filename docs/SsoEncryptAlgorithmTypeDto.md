# SsoEncryptAlgorithmTypeDto
The encryption algorithms the SSO settings accept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aes128** | **str** | The AES-128-CBC encryption algorithm, which the built-in configuration uses. | [optional] [readonly] 
**aes256** | **str** | The AES-256-CBC encryption algorithm, the strongest of the three. | [optional] [readonly] 
**tri_dec** | **str** | The Triple DES CBC encryption algorithm, kept for identity providers that support nothing newer. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.sso_encrypt_algorithm_type_dto import SsoEncryptAlgorithmTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoEncryptAlgorithmTypeDto from a JSON string
sso_encrypt_algorithm_type_dto_instance = SsoEncryptAlgorithmTypeDto.from_json(json)
# print the JSON string representation of the object
print(SsoEncryptAlgorithmTypeDto.to_json())

# convert the object into a dict
sso_encrypt_algorithm_type_dto_dict = sso_encrypt_algorithm_type_dto_instance.to_dict()
# create an instance of SsoEncryptAlgorithmTypeDto from a dict
sso_encrypt_algorithm_type_dto_from_dict = SsoEncryptAlgorithmTypeDto.from_dict(sso_encrypt_algorithm_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


