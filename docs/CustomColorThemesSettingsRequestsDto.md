# CustomColorThemesSettingsRequestsDto
The request parameters for managing the portal theme settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | [**CustomColorThemesSettingsItem**](CustomColorThemesSettingsItem.md) |  | [optional] 
**selected** | **int** | Specifies the optional value indicating the selected custom color theme. | [optional] 

## Example

```python
from docspace-api-python.models.custom_color_themes_settings_requests_dto import CustomColorThemesSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColorThemesSettingsRequestsDto from a JSON string
custom_color_themes_settings_requests_dto_instance = CustomColorThemesSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(CustomColorThemesSettingsRequestsDto.to_json())

# convert the object into a dict
custom_color_themes_settings_requests_dto_dict = custom_color_themes_settings_requests_dto_instance.to_dict()
# create an instance of CustomColorThemesSettingsRequestsDto from a dict
custom_color_themes_settings_requests_dto_from_dict = CustomColorThemesSettingsRequestsDto.from_dict(custom_color_themes_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


