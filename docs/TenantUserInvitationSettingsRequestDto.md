# TenantUserInvitationSettingsRequestDto
Whether the portal still lets its members invite new members and new guests.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_inviting_members** | **bool** | Whether new DocSpace members may be invited through the Contacts section. Switching it off only stops new  invitations being created; links already issued keep working and members already invited stay. | [optional] 
**allow_inviting_guests** | **bool** | Whether every DocSpace member, and not only an administrator, may invite external guests into rooms.  Switching it off leaves the guests already invited in place. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_user_invitation_settings_request_dto import TenantUserInvitationSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserInvitationSettingsRequestDto from a JSON string
tenant_user_invitation_settings_request_dto_instance = TenantUserInvitationSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TenantUserInvitationSettingsRequestDto.to_json())

# convert the object into a dict
tenant_user_invitation_settings_request_dto_dict = tenant_user_invitation_settings_request_dto_instance.to_dict()
# create an instance of TenantUserInvitationSettingsRequestDto from a dict
tenant_user_invitation_settings_request_dto_from_dict = TenantUserInvitationSettingsRequestDto.from_dict(tenant_user_invitation_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


