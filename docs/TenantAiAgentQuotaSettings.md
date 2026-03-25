# TenantAiAgentQuotaSettings
The AI agent quota settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable_quota** | **bool** | Specifies if the quota is enabled for the tenant entity or not. | [optional] 
**default_quota** | **int** | The default quota of the tenant entity. | [optional] 
**last_recalculate_date** | **datetime** | The date of the last quota recalculation. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_ai_agent_quota_settings import TenantAiAgentQuotaSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantAiAgentQuotaSettings from a JSON string
tenant_ai_agent_quota_settings_instance = TenantAiAgentQuotaSettings.from_json(json)
# print the JSON string representation of the object
print(TenantAiAgentQuotaSettings.to_json())

# convert the object into a dict
tenant_ai_agent_quota_settings_dict = tenant_ai_agent_quota_settings_instance.to_dict()
# create an instance of TenantAiAgentQuotaSettings from a dict
tenant_ai_agent_quota_settings_from_dict = TenantAiAgentQuotaSettings.from_dict(tenant_ai_agent_quota_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


