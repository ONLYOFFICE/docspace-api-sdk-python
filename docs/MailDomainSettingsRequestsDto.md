# MailDomainSettingsRequestsDto
The request parameters for configuring trusted mail domains and visitor invitation settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) |  | 
**domains** | **List[str]** | The list of authorized email domains that are considered trusted. | 
**invite_users_as_visitors** | **bool** | Specifies the default permission level for the invited users (visitors or not). | [optional] 

## Example

```python
from docspace_api_sdk.models.mail_domain_settings_requests_dto import MailDomainSettingsRequestsDto

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


