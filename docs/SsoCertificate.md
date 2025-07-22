# SsoCertificate
The SSO certificate parameters.

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
from docspace-api-sdk.models.sso_certificate import SsoCertificate

# TODO update the JSON string below
json = "{}"
# create an instance of SsoCertificate from a JSON string
sso_certificate_instance = SsoCertificate.from_json(json)
# print the JSON string representation of the object
print(SsoCertificate.to_json())

# convert the object into a dict
sso_certificate_dict = sso_certificate_instance.to_dict()
# create an instance of SsoCertificate from a dict
sso_certificate_from_dict = SsoCertificate.from_dict(sso_certificate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


