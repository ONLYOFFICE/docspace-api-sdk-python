# TenantDeepLinkSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**handling_mode** | [**DeepLinkHandlingMode**](DeepLinkHandlingMode.md) |  | [optional] 

## Example

```python
from docspace.models.tenant_deep_link_settings import TenantDeepLinkSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDeepLinkSettings from a JSON string
tenant_deep_link_settings_instance = TenantDeepLinkSettings.from_json(json)
# print the JSON string representation of the object
print(TenantDeepLinkSettings.to_json())

# convert the object into a dict
tenant_deep_link_settings_dict = tenant_deep_link_settings_instance.to_dict()
# create an instance of TenantDeepLinkSettings from a dict
tenant_deep_link_settings_from_dict = TenantDeepLinkSettings.from_dict(tenant_deep_link_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


