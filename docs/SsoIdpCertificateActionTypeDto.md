# SsoIdpCertificateActionTypeDto
What the identity provider's certificate may be used for, as the `action` of an identity provider certificate.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verification** | **str** | The certificate verifies the signatures on what the provider sends, and nothing else - the counterpart of  the service provider's signing action. | [optional] [readonly] 
**decrypt** | **str** | The certificate is used to decrypt what the provider sends, but verifies no signature. | [optional] [readonly] 
**verification_and_decrypt** | **str** | The certificate does both, which is what a single provider certificate has to be set to. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.sso_idp_certificate_action_type_dto import SsoIdpCertificateActionTypeDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoIdpCertificateActionTypeDto from a JSON string
sso_idp_certificate_action_type_dto_instance = SsoIdpCertificateActionTypeDto.from_json(json)
# print the JSON string representation of the object
print(SsoIdpCertificateActionTypeDto.to_json())

# convert the object into a dict
sso_idp_certificate_action_type_dto_dict = sso_idp_certificate_action_type_dto_instance.to_dict()
# create an instance of SsoIdpCertificateActionTypeDto from a dict
sso_idp_certificate_action_type_dto_from_dict = SsoIdpCertificateActionTypeDto.from_dict(sso_idp_certificate_action_type_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


