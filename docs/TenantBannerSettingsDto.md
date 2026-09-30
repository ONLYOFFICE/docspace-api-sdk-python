# TenantBannerSettingsDto
Whether the portal promotional banners are hidden.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hidden** | **bool** | Whether the promotional banners are hidden from every user of the portal. The flag is only honoured on a  self-hosted installation; a SaaS portal keeps showing the banners whatever is stored here. | [optional] 

## Example

```python
from docspace_api_sdk.models.tenant_banner_settings_dto import TenantBannerSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of TenantBannerSettingsDto from a JSON string
tenant_banner_settings_dto_instance = TenantBannerSettingsDto.from_json(json)
# print the JSON string representation of the object
print(TenantBannerSettingsDto.to_json())

# convert the object into a dict
tenant_banner_settings_dto_dict = tenant_banner_settings_dto_instance.to_dict()
# create an instance of TenantBannerSettingsDto from a dict
tenant_banner_settings_dto_from_dict = TenantBannerSettingsDto.from_dict(tenant_banner_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


