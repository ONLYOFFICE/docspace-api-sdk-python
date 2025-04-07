# DarkThemeSettingsRequestDto

Theme settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | [**DarkThemeSettingsType**](DarkThemeSettingsType.md) |  | [optional] 

## Example

```python
from docspace.models.dark_theme_settings_request_dto import DarkThemeSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of DarkThemeSettingsRequestDto from a JSON string
dark_theme_settings_request_dto_instance = DarkThemeSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(DarkThemeSettingsRequestDto.to_json())

# convert the object into a dict
dark_theme_settings_request_dto_dict = dark_theme_settings_request_dto_instance.to_dict()
# create an instance of DarkThemeSettingsRequestDto from a dict
dark_theme_settings_request_dto_from_dict = DarkThemeSettingsRequestDto.from_dict(dark_theme_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


