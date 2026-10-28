# SsoSpCertificateAdvancedDto
How the portal signs and encrypts what it sends to the identity provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**signing_algorithm** | **str** | The certificate signing algorithm. | [optional] 
**sign_auth_requests** | **bool** | Specifies if SP will sign the SAML authentication requests sent to IdP or not. | [optional] 
**sign_logout_requests** | **bool** | Specifies if SP will sign the SAML logout requests sent to IdP or not. | [optional] 
**sign_logout_responses** | **bool** | Specifies if SP will sign the SAML logout responses sent to IdP or not. | [optional] 
**encrypt_algorithm** | **str** | The certificate encryption algorithm. | [optional] 
**decrypt_algorithm** | **str** | The certificate decryption algorithm. | [optional] 
**encrypt_assertions** | **bool** | Specifies if the assertions will be encrypted or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_sp_certificate_advanced_dto import SsoSpCertificateAdvancedDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSpCertificateAdvancedDto from a JSON string
sso_sp_certificate_advanced_dto_instance = SsoSpCertificateAdvancedDto.from_json(json)
# print the JSON string representation of the object
print(SsoSpCertificateAdvancedDto.to_json())

# convert the object into a dict
sso_sp_certificate_advanced_dto_dict = sso_sp_certificate_advanced_dto_instance.to_dict()
# create an instance of SsoSpCertificateAdvancedDto from a dict
sso_sp_certificate_advanced_dto_from_dict = SsoSpCertificateAdvancedDto.from_dict(sso_sp_certificate_advanced_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


