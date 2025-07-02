# SsoSpCertificateAdvanced
The SP advanced certificate parameters.

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
from docspace-api-python.models.sso_sp_certificate_advanced import SsoSpCertificateAdvanced

# TODO update the JSON string below
json = "{}"
# create an instance of SsoSpCertificateAdvanced from a JSON string
sso_sp_certificate_advanced_instance = SsoSpCertificateAdvanced.from_json(json)
# print the JSON string representation of the object
print(SsoSpCertificateAdvanced.to_json())

# convert the object into a dict
sso_sp_certificate_advanced_dict = sso_sp_certificate_advanced_instance.to_dict()
# create an instance of SsoSpCertificateAdvanced from a dict
sso_sp_certificate_advanced_from_dict = SsoSpCertificateAdvanced.from_dict(sso_sp_certificate_advanced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


