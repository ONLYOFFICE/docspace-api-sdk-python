# TenantQuotaSettingsDto
The storage quota of the whole portal on a Standalone installation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the tenant quota is enabled or not. | [optional] 
**quota** | **int** | The tenant quota. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last tenant quota recalculation. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_quota_settings_dto import TenantQuotaSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuotaSettingsDto from a JSON string
tenant_quota_settings_dto_instance = TenantQuotaSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantQuotaSettingsDto.to_json())

# convert the object into a dict
tenant_quota_settings_dto_dict = tenant_quota_settings_dto_instance.to_dict()
# create an instance of TenantQuotaSettingsDto from a dict
tenant_quota_settings_dto_from_dict = TenantQuotaSettingsDto.from_dict(tenant_quota_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


