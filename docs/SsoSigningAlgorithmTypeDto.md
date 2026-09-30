# SsoSigningAlgorithmTypeDto
The signing algorithms the SSO settings accept.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rsa_sha1** | **str** | The RSA-SHA1 signing algorithm, which the built-in configuration uses. SHA-1 is the weakest of the three  and some identity providers no longer accept it. | [optional] [readonly] 
**rsa_sha256** | **str** | The RSA-SHA256 signing algorithm. | [optional] [readonly] 
**rsa_sha512** | **str** | The RSA-SHA512 signing algorithm. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.sso_signing_algorithm_type_dto import SsoSigningAlgorithmTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSigningAlgorithmTypeDto from a JSON string
sso_signing_algorithm_type_dto_instance = SsoSigningAlgorithmTypeDto.from_json(json)
# print the JSON string representation of the object
print(SsoSigningAlgorithmTypeDto.to_json())

# convert the object into a dict
sso_signing_algorithm_type_dto_dict = sso_signing_algorithm_type_dto_instance.to_dict()
# create an instance of SsoSigningAlgorithmTypeDto from a dict
sso_signing_algorithm_type_dto_from_dict = SsoSigningAlgorithmTypeDto.from_dict(sso_signing_algorithm_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


