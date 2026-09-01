# TenantBannerSettingsWrapper
The successful API response containing the TenantBannerSettings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**TenantBannerSettings**](TenantBannerSettings.md) | The TenantBannerSettings object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

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


