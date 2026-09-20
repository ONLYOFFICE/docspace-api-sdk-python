# SetAppSettingsBodySettings
The configuration the application reads, as any valid JSON value. Its shape is defined by the application and  is neither validated nor interpreted by the portal, which stores it verbatim. It replaces the whole stored  document rather than merging into it, and `null` drops it so the application falls back to its own defaults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.set_app_settings_body_settings import SetAppSettingsBodySettings

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppSettingsBodySettings from a JSON string
set_app_settings_body_settings_instance = SetAppSettingsBodySettings.from_json(json)
# print the JSON string representation of the object
print(SetAppSettingsBodySettings.to_json())

# convert the object into a dict
set_app_settings_body_settings_dict = set_app_settings_body_settings_instance.to_dict()
# create an instance of SetAppSettingsBodySettings from a dict
set_app_settings_body_settings_from_dict = SetAppSettingsBodySettings.from_dict(set_app_settings_body_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


