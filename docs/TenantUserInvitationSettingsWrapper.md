# TenantUserInvitationSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantUserInvitationSettingsDto**](TenantUserInvitationSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.tenant_user_invitation_settings_wrapper import TenantUserInvitationSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserInvitationSettingsWrapper from a JSON string
tenant_user_invitation_settings_wrapper_instance = TenantUserInvitationSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantUserInvitationSettingsWrapper.to_json())

# convert the object into a dict
tenant_user_invitation_settings_wrapper_dict = tenant_user_invitation_settings_wrapper_instance.to_dict()
# create an instance of TenantUserInvitationSettingsWrapper from a dict
tenant_user_invitation_settings_wrapper_from_dict = TenantUserInvitationSettingsWrapper.from_dict(tenant_user_invitation_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


