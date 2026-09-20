# SsoSpCertificateActionTypeDto
What the portal's own key pair may be used for, as the `action` of a service provider certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing** | **str** | The key pair signs the requests the portal sends and nothing else. | [optional] [readonly] 
**encrypt** | **str** | The key pair encrypts what the portal sends and decrypts what comes back, but signs nothing. | [optional] [readonly] 
**signing_and_encrypt** | **str** | The key pair does both, which is what one pair configured on its own has to be set to. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.sso_sp_certificate_action_type_dto import SsoSpCertificateActionTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSpCertificateActionTypeDto from a JSON string
sso_sp_certificate_action_type_dto_instance = SsoSpCertificateActionTypeDto.from_json(json)
# print the JSON string representation of the object
print(SsoSpCertificateActionTypeDto.to_json())

# convert the object into a dict
sso_sp_certificate_action_type_dto_dict = sso_sp_certificate_action_type_dto_instance.to_dict()
# create an instance of SsoSpCertificateActionTypeDto from a dict
sso_sp_certificate_action_type_dto_from_dict = SsoSpCertificateActionTypeDto.from_dict(sso_sp_certificate_action_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


