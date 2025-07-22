# TenantBannerSettings
The promotional banners visibility settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | The banners visibility flag. | [optional] 
**last_modified** | **datetime** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.tenant_banner_settings import TenantBannerSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TenantBannerSettings from a JSON string
tenant_banner_settings_instance = TenantBannerSettings.from_json(json)
# print the JSON string representation of the object
print(TenantBannerSettings.to_json())

# convert the object into a dict
tenant_banner_settings_dict = tenant_banner_settings_instance.to_dict()
# create an instance of TenantBannerSettings from a dict
tenant_banner_settings_from_dict = TenantBannerSettings.from_dict(tenant_banner_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


