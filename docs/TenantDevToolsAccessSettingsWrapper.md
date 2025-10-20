# TenantDevToolsAccessSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantDevToolsAccessSettings**](TenantDevToolsAccessSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_dev_tools_access_settings_wrapper import TenantDevToolsAccessSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDevToolsAccessSettingsWrapper from a JSON string
tenant_dev_tools_access_settings_wrapper_instance = TenantDevToolsAccessSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantDevToolsAccessSettingsWrapper.to_json())

# convert the object into a dict
tenant_dev_tools_access_settings_wrapper_dict = tenant_dev_tools_access_settings_wrapper_instance.to_dict()
# create an instance of TenantDevToolsAccessSettingsWrapper from a dict
tenant_dev_tools_access_settings_wrapper_from_dict = TenantDevToolsAccessSettingsWrapper.from_dict(tenant_dev_tools_access_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


