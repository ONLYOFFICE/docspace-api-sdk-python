# ProviderSettingsDto
Available AI provider type settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**ProviderType**](ProviderType.md) |  | [optional] 
**url** | **str** | Default API endpoint URL for the provider type. | [optional] 

## Example

```python
from docspace_api_sdk.models.provider_settings_dto import ProviderSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ProviderSettingsDto from a JSON string
provider_settings_dto_instance = ProviderSettingsDto.from_json(json)
# print the JSON string representation of the object
print(ProviderSettingsDto.to_json())

# convert the object into a dict
provider_settings_dto_dict = provider_settings_dto_instance.to_dict()
# create an instance of ProviderSettingsDto from a dict
provider_settings_dto_from_dict = ProviderSettingsDto.from_dict(provider_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


