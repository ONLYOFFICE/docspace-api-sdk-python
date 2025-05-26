# TenantAuditSettings

The tenant audit settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**login_history_life_time** | **int** | The login history lifetime. | [optional] 
**audit_trail_life_time** | **int** | The audit trail lifetime. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace.models.tenant_audit_settings import TenantAuditSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAuditSettings from a JSON string
tenant_audit_settings_instance = TenantAuditSettings.from_json(json)
# print the JSON string representation of the object
print(TenantAuditSettings.to_json())

# convert the object into a dict
tenant_audit_settings_dict = tenant_audit_settings_instance.to_dict()
# create an instance of TenantAuditSettings from a dict
tenant_audit_settings_from_dict = TenantAuditSettings.from_dict(tenant_audit_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


