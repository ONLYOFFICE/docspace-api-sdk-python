# SetAppEnabledBody
Whether a portal application is switched on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the application is available in this portal. Switching it off leaves its settings document stored, so  switching it back on restores the configuration it had; connected clients are told of the new state without a  reload. | [optional] 

## Example

```python
from docspace_api_sdk.models.set_app_enabled_body import SetAppEnabledBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppEnabledBody from a JSON string
set_app_enabled_body_instance = SetAppEnabledBody.from_json(json)
# print the JSON string representation of the object
print(SetAppEnabledBody.to_json())

# convert the object into a dict
set_app_enabled_body_dict = set_app_enabled_body_instance.to_dict()
# create an instance of SetAppEnabledBody from a dict
set_app_enabled_body_from_dict = SetAppEnabledBody.from_dict(set_app_enabled_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


