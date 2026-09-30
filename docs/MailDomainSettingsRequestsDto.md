# MailDomainSettingsRequestsDto
Which email domains the portal treats as already verified, and how their users join.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TenantTrustedDomainsType**](TenantTrustedDomainsType.md) | How trusted domains are decided: no domain is trusted, every domain is, or only the ones listed in `domains`.  Only the custom mode reads `domains`; under the other two the list is ignored rather than refused. | 
**domains** | **List[str]** | The trusted domains, as bare hostnames such as `example.com` without a scheme or an `@`. This is the whole  list that is to hold afterwards and not a list of additions. Each entry is lowercased before it is stored,  and one entry that is not a valid hostname - or an empty list in the custom mode - fails the whole call  without saving anything. | 
**invite_users_as_visitors** | **bool** | What a user joining through a trusted domain becomes: `true` admits them as a guest, `false` as a full  member. It applies to joins made from now on and does not change anybody who has already joined. | 

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


