# CustomColorThemesSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**CustomColorThemesSettingsDto**](CustomColorThemesSettingsDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.custom_color_themes_settings_wrapper import CustomColorThemesSettingsWrapper

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


