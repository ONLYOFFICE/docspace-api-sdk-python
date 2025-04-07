# TenantUserQuotaSettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantUserQuotaSettings**](TenantUserQuotaSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.tenant_user_quota_settings_wrapper import TenantUserQuotaSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantUserQuotaSettingsWrapper from a JSON string
tenant_user_quota_settings_wrapper_instance = TenantUserQuotaSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantUserQuotaSettingsWrapper.to_json())

# convert the object into a dict
tenant_user_quota_settings_wrapper_dict = tenant_user_quota_settings_wrapper_instance.to_dict()
# create an instance of TenantUserQuotaSettingsWrapper from a dict
tenant_user_quota_settings_wrapper_from_dict = TenantUserQuotaSettingsWrapper.from_dict(tenant_user_quota_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


