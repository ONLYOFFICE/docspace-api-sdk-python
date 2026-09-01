# SetAppSettingsBody
Request body for saving application-specific settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | [**SetAppSettingsBodySettings**](SetAppSettingsBodySettings.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.set_app_settings_body import SetAppSettingsBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppSettingsBody from a JSON string
set_app_settings_body_instance = SetAppSettingsBody.from_json(json)
# print the JSON string representation of the object
print(SetAppSettingsBody.to_json())

# convert the object into a dict
set_app_settings_body_dict = set_app_settings_body_instance.to_dict()
# create an instance of SetAppSettingsBody from a dict
set_app_settings_body_from_dict = SetAppSettingsBody.from_dict(set_app_settings_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


