# TenantDeepLinkSettingsDto
How the portal opens its links on a mobile device.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handling_mode** | [**DeepLinkHandlingMode**](DeepLinkHandlingMode.md) | The deep link handling mode. | [optional] 
**last_modified** | **datetime** | The timestamp indicating when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_deep_link_settings_dto import TenantDeepLinkSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDeepLinkSettingsDto from a JSON string
tenant_deep_link_settings_dto_instance = TenantDeepLinkSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantDeepLinkSettingsDto.to_json())

# convert the object into a dict
tenant_deep_link_settings_dto_dict = tenant_deep_link_settings_dto_instance.to_dict()
# create an instance of TenantDeepLinkSettingsDto from a dict
tenant_deep_link_settings_dto_from_dict = TenantDeepLinkSettingsDto.from_dict(tenant_deep_link_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


