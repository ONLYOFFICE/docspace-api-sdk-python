# IpRestrictionsSettingsDto
Whether the portal limits sign-in to its list of allowed IP addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enable** | **bool** | Specifies if the IP restrictions are enabled or not. | [optional] 
**last_modified** | **datetime** | The date and time when the settings were last modified. | [optional] 

## Example

```python
from docspace_api_sdk.models.ip_restrictions_settings_dto import IpRestrictionsSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of IpRestrictionsSettingsDto from a JSON string
ip_restrictions_settings_dto_instance = IpRestrictionsSettingsDto.from_json(json)
# print the JSON string representation of the object
print(IpRestrictionsSettingsDto.to_json())

# convert the object into a dict
ip_restrictions_settings_dto_dict = ip_restrictions_settings_dto_instance.to_dict()
# create an instance of IpRestrictionsSettingsDto from a dict
ip_restrictions_settings_dto_from_dict = IpRestrictionsSettingsDto.from_dict(ip_restrictions_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


