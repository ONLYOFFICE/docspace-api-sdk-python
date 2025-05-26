# SsoIdpCertificateAdvanced

The IdP advanced certificate parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**verify_algorithm** | **str** | The certificate verification algorithm. | [optional] 
**verify_auth_responses_sign** | **bool** | Specifies if the signatures of the SAML authentication responses sent to SP will be verified or not. | [optional] 
**verify_logout_requests_sign** | **bool** | Specifies if the signatures of the SAML logout requests sent to SP will be verified or not. | [optional] 
**verify_logout_responses_sign** | **bool** | Specifies if the signatures of the SAML logout responses sent to SP will be verified or not. | [optional] 
**decrypt_algorithm** | **str** | The certificate decryption algorithm. | [optional] 
**decrypt_assertions** | **bool** | Specifies if the assertions will be decrypted or not. | [optional] 

## Example

```python
from docspace.models.sso_idp_certificate_advanced import SsoIdpCertificateAdvanced

# TODO update the JSON string below
json = "{}"
# create an instance of SsoIdpCertificateAdvanced from a JSON string
sso_idp_certificate_advanced_instance = SsoIdpCertificateAdvanced.from_json(json)
# print the JSON string representation of the object
print(SsoIdpCertificateAdvanced.to_json())

# convert the object into a dict
sso_idp_certificate_advanced_dict = sso_idp_certificate_advanced_instance.to_dict()
# create an instance of SsoIdpCertificateAdvanced from a dict
sso_idp_certificate_advanced_from_dict = SsoIdpCertificateAdvanced.from_dict(sso_idp_certificate_advanced_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


