# ColorThemeColorsRequestDto
A pair of colours of a theme.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accent** | **str** | The accent colour, as a hex code. | [optional] 
**buttons** | **str** | The button colour, as a hex code. | [optional] 

## Example

```python
from docspace_api_sdk.models.color_theme_colors_request_dto import ColorThemeColorsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of ColorThemeColorsRequestDto from a JSON string
color_theme_colors_request_dto_instance = ColorThemeColorsRequestDto.from_json(json)
# print the JSON string representation of the object
print(ColorThemeColorsRequestDto.to_json())

# convert the object into a dict
color_theme_colors_request_dto_dict = color_theme_colors_request_dto_instance.to_dict()
# create an instance of ColorThemeColorsRequestDto from a dict
color_theme_colors_request_dto_from_dict = ColorThemeColorsRequestDto.from_dict(color_theme_colors_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


