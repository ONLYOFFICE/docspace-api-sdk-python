# TenantAiAccessSettingsDto
The request parameters for managing the tenant-level AI access settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether AI functionality is enabled for the tenant.  Set to `true` to enable all AI features or `false` to disable them tenant-wide. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_ai_access_settings_dto import TenantAiAccessSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAiAccessSettingsDto from a JSON string
tenant_ai_access_settings_dto_instance = TenantAiAccessSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantAiAccessSettingsDto.to_json())

# convert the object into a dict
tenant_ai_access_settings_dto_dict = tenant_ai_access_settings_dto_instance.to_dict()
# create an instance of TenantAiAccessSettingsDto from a dict
tenant_ai_access_settings_dto_from_dict = TenantAiAccessSettingsDto.from_dict(tenant_ai_access_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


