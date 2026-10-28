# TenantDevToolsAccessSettingsDto
Whether the developer tools are closed to the portal's users with the `User` role.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_access_for_users** | **bool** | Specifies if the Developer Tools access are limited for users or not. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

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


