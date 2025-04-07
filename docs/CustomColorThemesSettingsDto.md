# CustomColorThemesSettingsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**themes** | [**List[CustomColorThemesSettingsItem]**](CustomColorThemesSettingsItem.md) | Themes | [optional] 
**selected** | **int** | Selected | [optional] 
**limit** | **int** | Limit | [optional] 

## Example

```python
from docspace.models.custom_color_themes_settings_dto import CustomColorThemesSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColorThemesSettingsDto from a JSON string
custom_color_themes_settings_dto_instance = CustomColorThemesSettingsDto.from_json(json)
# print the JSON string representation of the object
print(CustomColorThemesSettingsDto.to_json())

# convert the object into a dict
custom_color_themes_settings_dto_dict = custom_color_themes_settings_dto_instance.to_dict()
# create an instance of CustomColorThemesSettingsDto from a dict
custom_color_themes_settings_dto_from_dict = CustomColorThemesSettingsDto.from_dict(custom_color_themes_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


