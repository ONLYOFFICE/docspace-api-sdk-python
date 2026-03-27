# TenantAiAccessSettings
The tenant-level settings for enabling or disabling all AI functionality in DocSpace.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Specifies whether AI functionality is enabled for the tenant.  When set to `false`, all AI features (chat, agents, vectorization) are disabled tenant-wide. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_ai_access_settings import TenantAiAccessSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAiAccessSettings from a JSON string
tenant_ai_access_settings_instance = TenantAiAccessSettings.from_json(json)
# print the JSON string representation of the object
print(TenantAiAccessSettings.to_json())

# convert the object into a dict
tenant_ai_access_settings_dict = tenant_ai_access_settings_instance.to_dict()
# create an instance of TenantAiAccessSettings from a dict
tenant_ai_access_settings_from_dict = TenantAiAccessSettings.from_dict(tenant_ai_access_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


