# SetAppSettingsRequest
The configuration document a portal application keeps.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**settings** | **object** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.set_app_settings_request import SetAppSettingsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppSettingsRequest from a JSON string
set_app_settings_request_instance = SetAppSettingsRequest.from_json(json)
# print the JSON string representation of the object
print(SetAppSettingsRequest.to_json())

# convert the object into a dict
set_app_settings_request_dict = set_app_settings_request_instance.to_dict()
# create an instance of SetAppSettingsRequest from a dict
set_app_settings_request_from_dict = SetAppSettingsRequest.from_dict(set_app_settings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


