# IPRestrictionsSettingsWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**IPRestrictionsSettings**](IPRestrictionsSettings.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.ip_restrictions_settings_wrapper import IPRestrictionsSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of IPRestrictionsSettingsWrapper from a JSON string
ip_restrictions_settings_wrapper_instance = IPRestrictionsSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(IPRestrictionsSettingsWrapper.to_json())

# convert the object into a dict
ip_restrictions_settings_wrapper_dict = ip_restrictions_settings_wrapper_instance.to_dict()
# create an instance of IPRestrictionsSettingsWrapper from a dict
ip_restrictions_settings_wrapper_from_dict = IPRestrictionsSettingsWrapper.from_dict(ip_restrictions_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


