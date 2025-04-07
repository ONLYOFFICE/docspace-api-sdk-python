# CustomColorThemesSettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CustomColorThemesSettingsDto**](CustomColorThemesSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of CustomColorThemesSettingsWrapper from a JSON string
custom_color_themes_settings_wrapper_instance = CustomColorThemesSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(CustomColorThemesSettingsWrapper.to_json())

# convert the object into a dict
custom_color_themes_settings_wrapper_dict = custom_color_themes_settings_wrapper_instance.to_dict()
# create an instance of CustomColorThemesSettingsWrapper from a dict
custom_color_themes_settings_wrapper_from_dict = CustomColorThemesSettingsWrapper.from_dict(custom_color_themes_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


