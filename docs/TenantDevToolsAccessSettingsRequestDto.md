# TenantDevToolsAccessSettingsRequestDto
Whether the `User` role is barred from the portal developer tools.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**limited_access_for_users** | **bool** | Whether members holding the `User` role are barred from the developer tools - API keys, OAuth applications  and webhooks. Room administrators and DocSpace administrators keep their access either way. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_dev_tools_access_settings_request_dto import TenantDevToolsAccessSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDevToolsAccessSettingsRequestDto from a JSON string
tenant_dev_tools_access_settings_request_dto_instance = TenantDevToolsAccessSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(TenantDevToolsAccessSettingsRequestDto.to_json())

# convert the object into a dict
tenant_dev_tools_access_settings_request_dto_dict = tenant_dev_tools_access_settings_request_dto_instance.to_dict()
# create an instance of TenantDevToolsAccessSettingsRequestDto from a dict
tenant_dev_tools_access_settings_request_dto_from_dict = TenantDevToolsAccessSettingsRequestDto.from_dict(tenant_dev_tools_access_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


