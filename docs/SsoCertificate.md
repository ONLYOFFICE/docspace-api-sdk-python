# SsoCertificate


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**self_signed** | **bool** | Specifies if a certificate is self-signed or not | [optional] 
**crt** | **str** | Certificate | [optional] 
**key** | **str** | Key | [optional] 
**action** | **str** | Action | [optional] 
**domain_name** | **str** | Domain name | [optional] 
**start_date** | **datetime** | Start date | [optional] 
**expired_date** | **datetime** | Expiration date | [optional] 

## Example

```python
from docspace.models.sso_certificate import SsoCertificate

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


