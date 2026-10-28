# TenantUserInvitationSettingsDto
Whether the portal currently lets anyone be invited into it, member and guest kept apart.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_inviting_members** | **bool** | Whether new members may be invited through the Contacts section. Switching it off stops new invitations  from being created; links already handed out keep working and members already invited stay. | 
**allow_inviting_guests** | **bool** | Whether every member, and not only an administrator, may invite an outside guest into a room. It is  independent of `allowInvitingMembers`, and switching it off has the same forward-only effect. | 

## Example

```python
from docspace_api_sdk.models.tenant_user_invitation_settings_dto import TenantUserInvitationSettingsDto

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


