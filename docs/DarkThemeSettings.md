# DarkThemeSettings



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | [**DarkThemeSettingsType**](DarkThemeSettingsType.md) |  | [optional] 

## Example

```python
from docspace.models.dark_theme_settings import DarkThemeSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DarkThemeSettings from a JSON string
dark_theme_settings_instance = DarkThemeSettings.from_json(json)
# print the JSON string representation of the object
print(DarkThemeSettings.to_json())

# convert the object into a dict
dark_theme_settings_dict = dark_theme_settings_instance.to_dict()
# create an instance of DarkThemeSettings from a dict
dark_theme_settings_from_dict = DarkThemeSettings.from_dict(dark_theme_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


