# TenantAuditSettingsDto
How long the portal keeps its login history and its audit trail.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_history_life_time** | **int** | How many days login events are kept, from 1 to 180; 180 when the portal never changed it. | [optional] 
**audit_trail_life_time** | **int** | How many days audit trail events are kept, from 1 to 180; 180 when the portal never changed it. | [optional] 
**last_modified** | **datetime** | When the pair was last stored; when it never was, the moment it was read instead. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_audit_settings_dto import TenantAuditSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAuditSettingsDto from a JSON string
tenant_audit_settings_dto_instance = TenantAuditSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantAuditSettingsDto.to_json())

# convert the object into a dict
tenant_audit_settings_dto_dict = tenant_audit_settings_dto_instance.to_dict()
# create an instance of TenantAuditSettingsDto from a dict
tenant_audit_settings_dto_from_dict = TenantAuditSettingsDto.from_dict(tenant_audit_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


