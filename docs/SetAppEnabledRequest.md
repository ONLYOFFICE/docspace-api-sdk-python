# SetAppEnabledRequest
Whether a portal application is switched on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether the application is available in this portal. Switching it off leaves its settings document stored, so  switching it back on restores the configuration it had; connected clients are told of the new state without a  reload. The field is mandatory: a body without it is rejected with 400 and leaves the application as it was. | 

## Example

```python
from docspace_api_sdk.models.set_app_enabled_request import SetAppEnabledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAppEnabledRequest from a JSON string
set_app_enabled_request_instance = SetAppEnabledRequest.from_json(json)
# print the JSON string representation of the object
print(SetAppEnabledRequest.to_json())

# convert the object into a dict
set_app_enabled_request_dict = set_app_enabled_request_instance.to_dict()
# create an instance of SetAppEnabledRequest from a dict
set_app_enabled_request_from_dict = SetAppEnabledRequest.from_dict(set_app_enabled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


