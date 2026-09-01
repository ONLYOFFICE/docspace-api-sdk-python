# IPRestrictionsSettings
The IP restriction settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Specifies if the IP restrictions are enabled or not. | [optional] 
**last_modified** | **datetime** | The date and time when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restrictions_settings import IPRestrictionsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of IPRestrictionsSettings from a JSON string
ip_restrictions_settings_instance = IPRestrictionsSettings.from_json(json)
# print the JSON string representation of the object
print(IPRestrictionsSettings.to_json())

# convert the object into a dict
ip_restrictions_settings_dict = ip_restrictions_settings_instance.to_dict()
# create an instance of IPRestrictionsSettings from a dict
ip_restrictions_settings_from_dict = IPRestrictionsSettings.from_dict(ip_restrictions_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


