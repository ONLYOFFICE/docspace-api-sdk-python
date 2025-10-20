# TenantBannerSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantBannerSettings**](TenantBannerSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_banner_settings_wrapper import TenantBannerSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of TenantBannerSettingsWrapper from a JSON string
tenant_banner_settings_wrapper_instance = TenantBannerSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(TenantBannerSettingsWrapper.to_json())

# convert the object into a dict
tenant_banner_settings_wrapper_dict = tenant_banner_settings_wrapper_instance.to_dict()
# create an instance of TenantBannerSettingsWrapper from a dict
tenant_banner_settings_wrapper_from_dict = TenantBannerSettingsWrapper.from_dict(tenant_banner_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


