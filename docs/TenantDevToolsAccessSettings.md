# TenantDevToolsAccessSettings
The Developer Tools access settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_access_for_users** | **bool** | Specifies if the Developer Tools access are limited for users or not. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_dev_tools_access_settings import TenantDevToolsAccessSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDevToolsAccessSettings from a JSON string
tenant_dev_tools_access_settings_instance = TenantDevToolsAccessSettings.from_json(json)
# print the JSON string representation of the object
print(TenantDevToolsAccessSettings.to_json())

# convert the object into a dict
tenant_dev_tools_access_settings_dict = tenant_dev_tools_access_settings_instance.to_dict()
# create an instance of TenantDevToolsAccessSettings from a dict
tenant_dev_tools_access_settings_from_dict = TenantDevToolsAccessSettings.from_dict(tenant_dev_tools_access_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


