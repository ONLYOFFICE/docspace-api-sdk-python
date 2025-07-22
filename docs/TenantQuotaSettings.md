# TenantQuotaSettings
The tenant quota settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the tenant quota is enabled or not. | [optional] 
**quota** | **int** | The tenant quota. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last tenant quota recalculation. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_quota_settings import TenantQuotaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantQuotaSettings from a JSON string
tenant_quota_settings_instance = TenantQuotaSettings.from_json(json)
# print the JSON string representation of the object
print(TenantQuotaSettings.to_json())

# convert the object into a dict
tenant_quota_settings_dict = tenant_quota_settings_instance.to_dict()
# create an instance of TenantQuotaSettings from a dict
tenant_quota_settings_from_dict = TenantQuotaSettings.from_dict(tenant_quota_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


