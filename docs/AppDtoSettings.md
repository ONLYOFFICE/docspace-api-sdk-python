# AppDtoSettings
Application-specific settings as a JSON document, or null if no overrides exist.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.app_dto_settings import AppDtoSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AppDtoSettings from a JSON string
app_dto_settings_instance = AppDtoSettings.from_json(json)
# print the JSON string representation of the object
print(AppDtoSettings.to_json())

# convert the object into a dict
app_dto_settings_dict = app_dto_settings_instance.to_dict()
# create an instance of AppDtoSettings from a dict
app_dto_settings_from_dict = AppDtoSettings.from_dict(app_dto_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


