# CookieSettingsRequestsDto
How long an authentication session of the portal stays valid, and whether that limit is applied.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**life_time** | **int** | How long, in minutes, a session issued from now on remains valid. A value above 9999 is clamped to 9999  rather than refused, and 0 or less clears the number, which together with `enabled` leaves sessions that  never expire on their own. Any positive value invalidates every session issued before this call, the  caller's included, so the client has to keep the fresh cookie the response carries. | [optional] 
**enabled** | **bool** | Whether the stored lifetime is applied at all. While it is false the number is ignored and an issued session  is honoured for a year; while it is true the connections behind expired sessions are dropped as well. | [optional] 

## Example

```python
from docspace_api_sdk.models.cookie_settings_requests_dto import CookieSettingsRequestsDto

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


