# CustomColorThemeDto
One colour theme of the portal interface.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The theme id; the built-in themes have the lowest ids. | [optional] 
**name** | **str** | The theme name; empty for a custom theme. | [optional] 
**main** | [**ColorThemeColorsDto**](ColorThemeColorsDto.md) | The accent and button colours of the interface. | [optional] 
**text** | [**ColorThemeColorsDto**](ColorThemeColorsDto.md) | The colours of the text shown on the accent and on the buttons. | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_color_theme_dto import CustomColorThemeDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColorThemeDto from a JSON string
custom_color_theme_dto_instance = CustomColorThemeDto.from_json(json)
# print the JSON string representation of the object
print(CustomColorThemeDto.to_json())

# convert the object into a dict
custom_color_theme_dto_dict = custom_color_theme_dto_instance.to_dict()
# create an instance of CustomColorThemeDto from a dict
custom_color_theme_dto_from_dict = CustomColorThemeDto.from_dict(custom_color_theme_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


