# TenantDeepLinkSettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantDeepLinkSettings**](TenantDeepLinkSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.tenant_deep_link_settings_wrapper import TenantDeepLinkSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantDeepLinkSettingsWrapper from a JSON string
tenant_deep_link_settings_wrapper_instance = TenantDeepLinkSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantDeepLinkSettingsWrapper.to_json())

# convert the object into a dict
tenant_deep_link_settings_wrapper_dict = tenant_deep_link_settings_wrapper_instance.to_dict()
# create an instance of TenantDeepLinkSettingsWrapper from a dict
tenant_deep_link_settings_wrapper_from_dict = TenantDeepLinkSettingsWrapper.from_dict(tenant_deep_link_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


