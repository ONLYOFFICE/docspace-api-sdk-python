# CookieSettingsDto
How long an authentication session of the portal stays valid, and whether that limit is applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**life_time** | **int** | How long, in minutes, a session issued from now on remains valid. It is `1440` on a portal that has never  stored a limit, and that stored number is reported whether or not `enabled` puts it to use. | 
**enabled** | **bool** | Whether the stored lifetime is applied at all. While it is `false` the number above is ignored and an  issued session is honoured for a year. | 

## Example

```python
from docspace_api_sdk.models.cookie_settings_dto import CookieSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CookieSettingsDto from a JSON string
cookie_settings_dto_instance = CookieSettingsDto.from_json(json)
# print the JSON string representation of the object
print(CookieSettingsDto.to_json())

# convert the object into a dict
cookie_settings_dto_dict = cookie_settings_dto_instance.to_dict()
# create an instance of CookieSettingsDto from a dict
cookie_settings_dto_from_dict = CookieSettingsDto.from_dict(cookie_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


