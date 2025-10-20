# TenantDevToolsAccessSettingsDto
The request parameters for managing the Developer Tools access settings for the current tenant.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_access_for_users** | **bool** | Determines if users have restricted access to the Developer Tools. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_dev_tools_access_settings_dto import TenantDevToolsAccessSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDevToolsAccessSettingsDto from a JSON string
tenant_dev_tools_access_settings_dto_instance = TenantDevToolsAccessSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantDevToolsAccessSettingsDto.to_json())

# convert the object into a dict
tenant_dev_tools_access_settings_dto_dict = tenant_dev_tools_access_settings_dto_instance.to_dict()
# create an instance of TenantDevToolsAccessSettingsDto from a dict
tenant_dev_tools_access_settings_dto_from_dict = TenantDevToolsAccessSettingsDto.from_dict(tenant_dev_tools_access_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


