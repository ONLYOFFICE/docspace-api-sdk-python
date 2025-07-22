# DarkThemeSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**DarkThemeSettings**](DarkThemeSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.dark_theme_settings_wrapper import DarkThemeSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DarkThemeSettingsWrapper from a JSON string
dark_theme_settings_wrapper_instance = DarkThemeSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(DarkThemeSettingsWrapper.to_json())

# convert the object into a dict
dark_theme_settings_wrapper_dict = dark_theme_settings_wrapper_instance.to_dict()
# create an instance of DarkThemeSettingsWrapper from a dict
dark_theme_settings_wrapper_from_dict = DarkThemeSettingsWrapper.from_dict(dark_theme_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


