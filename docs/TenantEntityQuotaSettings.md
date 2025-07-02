# TenantEntityQuotaSettings
The tenant entity quota settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the quota is enabled for the tenant entity or not. | [optional] 
**default_quota** | **int** | The default quota of the tenant entity. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last quota recalculation. | [optional] 

## Example

```python
from docspace-api-python.models.tenant_entity_quota_settings import TenantEntityQuotaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantEntityQuotaSettings from a JSON string
tenant_entity_quota_settings_instance = TenantEntityQuotaSettings.from_json(json)
# print the JSON string representation of the object
print(TenantEntityQuotaSettings.to_json())

# convert the object into a dict
tenant_entity_quota_settings_dict = tenant_entity_quota_settings_instance.to_dict()
# create an instance of TenantEntityQuotaSettings from a dict
tenant_entity_quota_settings_from_dict = TenantEntityQuotaSettings.from_dict(tenant_entity_quota_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


