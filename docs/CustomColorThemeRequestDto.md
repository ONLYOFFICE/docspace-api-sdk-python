# CustomColorThemeRequestDto
A colour theme to store.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the custom theme to replace, or an id no stored theme has to add a new one. | [optional] 
**name** | **str** | Accepted for compatibility with earlier clients and not read: a custom theme is always stored without a name. | [optional] 
**main** | [**ColorThemeColorsRequestDto**](ColorThemeColorsRequestDto.md) | The accent and button colours of the interface. Left out, a stored theme keeps its own. | [optional] 
**text** | [**ColorThemeColorsRequestDto**](ColorThemeColorsRequestDto.md) | The colours of the text shown on the accent and on the buttons. Left out, a stored theme keeps its own. | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_color_theme_request_dto import CustomColorThemeRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColorThemeRequestDto from a JSON string
custom_color_theme_request_dto_instance = CustomColorThemeRequestDto.from_json(json)
# print the JSON string representation of the object
print(CustomColorThemeRequestDto.to_json())

# convert the object into a dict
custom_color_theme_request_dto_dict = custom_color_theme_request_dto_instance.to_dict()
# create an instance of CustomColorThemeRequestDto from a dict
custom_color_theme_request_dto_from_dict = CustomColorThemeRequestDto.from_dict(custom_color_theme_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


