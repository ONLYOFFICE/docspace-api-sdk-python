# CustomColorThemesSettingsItem
The custom color theme settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The custom color theme ID. | [optional] 
**name** | **str** | The custom color theme name. | [optional] 
**main** | [**CustomColorThemesSettingsColorItem**](CustomColorThemesSettingsColorItem.md) |  | [optional] 
**text** | [**CustomColorThemesSettingsColorItem**](CustomColorThemesSettingsColorItem.md) |  | [optional] 

## Example

```python
from docspace-api-python.models.custom_color_themes_settings_item import CustomColorThemesSettingsItem

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColorThemesSettingsItem from a JSON string
custom_color_themes_settings_item_instance = CustomColorThemesSettingsItem.from_json(json)
# print the JSON string representation of the object
print(CustomColorThemesSettingsItem.to_json())

# convert the object into a dict
custom_color_themes_settings_item_dict = custom_color_themes_settings_item_instance.to_dict()
# create an instance of CustomColorThemesSettingsItem from a dict
custom_color_themes_settings_item_from_dict = CustomColorThemesSettingsItem.from_dict(custom_color_themes_settings_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


