# CustomColorThemesSettingsRequestsDto
The custom colour theme being saved, the theme being selected, or both.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**theme** | [**CustomColorThemesSettingsItem**](CustomColorThemesSettingsItem.md) | The theme to store, with its accent and button colours for the interface and for the text on it. An `id` that  matches a stored custom theme replaces it, an unknown `id` appends a new one, and an `id` belonging to a  built-in theme is treated as a request for a new custom theme rather than overwriting the built-in one. Once  the plan limit on custom themes is reached a new theme is silently not added, so compare the returned themes  against `limit` instead of assuming it was saved. Leave it out to change only the selection. | [optional] 
**selected** | **int** | The theme the whole portal switches to, by theme ID. An ID matching no stored theme is ignored rather than  refused, and leaving it out keeps the selection as it is. | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_color_themes_settings_requests_dto import CustomColorThemesSettingsRequestsDto

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


