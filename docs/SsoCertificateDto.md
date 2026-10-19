# SsoCertificateDto
A certificate used to sign or encrypt SAML messages, with its validity period.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_signed** | **bool** | Specifies if a certificate is self-signed or not. | [optional] 
**crt** | **str** | The CRT certificate file. | [optional] 
**key** | **str** | The certificate key. | [optional] 
**action** | **str** | The certificate action. | [optional] 
**domain_name** | **str** | The certificate domain name. | [optional] 
**start_date** | **datetime** | The certificate start date. | [optional] 
**expired_date** | **datetime** | The certificate expiration date. | [optional] 

## Example

```python
from docspace_api_sdk.models.sso_certificate_dto import SsoCertificateDto

# TODO update the JSON string below
json = "{}"
# create an instance of SsoCertificateDto from a JSON string
sso_certificate_dto_instance = SsoCertificateDto.from_json(json)
# print the JSON string representation of the object
print(SsoCertificateDto.to_json())

# convert the object into a dict
sso_certificate_dto_dict = sso_certificate_dto_instance.to_dict()
# create an instance of SsoCertificateDto from a dict
sso_certificate_dto_from_dict = SsoCertificateDto.from_dict(sso_certificate_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


