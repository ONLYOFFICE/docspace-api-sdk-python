# TenantAuditSettingsRequestDto
The body of an audit lifetime change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SetAuditLifetimeSettingsRequest**](SetAuditLifetimeSettingsRequest.md) | The login history and audit trail lifetimes to store. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_audit_settings_request_dto import TenantAuditSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAuditSettingsRequestDto from a JSON string
tenant_audit_settings_request_dto_instance = TenantAuditSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TenantAuditSettingsRequestDto.to_json())

# convert the object into a dict
tenant_audit_settings_request_dto_dict = tenant_audit_settings_request_dto_instance.to_dict()
# create an instance of TenantAuditSettingsRequestDto from a dict
tenant_audit_settings_request_dto_from_dict = TenantAuditSettingsRequestDto.from_dict(tenant_audit_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


