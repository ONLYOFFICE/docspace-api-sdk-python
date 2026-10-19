# DarkThemeSettingsDto
The interface theme the calling account has chosen.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | [**DarkThemeSettingsType**](DarkThemeSettingsType.md) | The theme type. | [optional] 
**last_modified** | **datetime** | The last modified date. | [optional] 

## Example

```python
from docspace_api_sdk.models.dark_theme_settings_dto import DarkThemeSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of DarkThemeSettingsDto from a JSON string
dark_theme_settings_dto_instance = DarkThemeSettingsDto.from_json(json)
# print the JSON string representation of the object
print(DarkThemeSettingsDto.to_json())

# convert the object into a dict
dark_theme_settings_dto_dict = dark_theme_settings_dto_instance.to_dict()
# create an instance of DarkThemeSettingsDto from a dict
dark_theme_settings_dto_from_dict = DarkThemeSettingsDto.from_dict(dark_theme_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


