# TenantUserInvitationSettingsDto
User invitation settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_inviting_members** | **bool** | Allow invite new DocSpace members through the Contacts section. | [optional] 
**allow_inviting_guests** | **bool** | Allow all DocSpace members to invite external guests to rooms. | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_user_invitation_settings_dto import TenantUserInvitationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserInvitationSettingsDto from a JSON string
tenant_user_invitation_settings_dto_instance = TenantUserInvitationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantUserInvitationSettingsDto.to_json())

# convert the object into a dict
tenant_user_invitation_settings_dto_dict = tenant_user_invitation_settings_dto_instance.to_dict()
# create an instance of TenantUserInvitationSettingsDto from a dict
tenant_user_invitation_settings_dto_from_dict = TenantUserInvitationSettingsDto.from_dict(tenant_user_invitation_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


