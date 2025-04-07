# CookieSettingsRequestsDto

Cookies settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**life_time** | **int** | Lifetime value in minutes | [optional] 
**enabled** | **bool** | Specifies if the cookie settings are enabled or not | [optional] 

## Example

```python
from docspace.models.cookie_settings_requests_dto import CookieSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of CookieSettingsRequestsDto from a JSON string
cookie_settings_requests_dto_instance = CookieSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(CookieSettingsRequestsDto.to_json())

# convert the object into a dict
cookie_settings_requests_dto_dict = cookie_settings_requests_dto_instance.to_dict()
# create an instance of CookieSettingsRequestsDto from a dict
cookie_settings_requests_dto_from_dict = CookieSettingsRequestsDto.from_dict(cookie_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


