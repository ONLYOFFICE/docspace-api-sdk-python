# CookieSettingsDto
The cookie settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**life_time** | **int** | The cookie lifetime value in minutes. | [optional] 
**enabled** | **bool** | Specifies if the cookie settings are enabled or not. | [optional] 

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


