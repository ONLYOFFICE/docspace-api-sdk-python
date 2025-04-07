# MailDomainSettingsRequestsDto

Request parameters for mail domain settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | [optional] 
**domains** | **List[str]** | List of trusted domains | [optional] 
**invite_users_as_visitors** | **bool** | Invites as a user or not | [optional] 

## Example

```python
from docspace.models.mail_domain_settings_requests_dto import MailDomainSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of MailDomainSettingsRequestsDto from a JSON string
mail_domain_settings_requests_dto_instance = MailDomainSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(MailDomainSettingsRequestsDto.to_json())

# convert the object into a dict
mail_domain_settings_requests_dto_dict = mail_domain_settings_requests_dto_instance.to_dict()
# create an instance of MailDomainSettingsRequestsDto from a dict
mail_domain_settings_requests_dto_from_dict = MailDomainSettingsRequestsDto.from_dict(mail_domain_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


