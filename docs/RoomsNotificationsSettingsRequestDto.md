# RoomsNotificationsSettingsRequestDto
Which single room the calling user silences, and which way.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms_id** | **object** |  | [optional] 
**mute** | **bool** | Which way the room goes: `true` adds it to the caller silenced list, `false` takes it off again. While a room  is silenced its activity is left out of the hourly and daily digests, the letters it would send at once are  not sent, and its new-item counters are hidden. | [optional] 

## Example

```python
from docspace_api_sdk.models.rooms_notifications_settings_request_dto import RoomsNotificationsSettingsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomsNotificationsSettingsRequestDto from a JSON string
rooms_notifications_settings_request_dto_instance = RoomsNotificationsSettingsRequestDto.from_json(json)
# print the JSON string representation of the object
print(RoomsNotificationsSettingsRequestDto.to_json())

# convert the object into a dict
rooms_notifications_settings_request_dto_dict = rooms_notifications_settings_request_dto_instance.to_dict()
# create an instance of RoomsNotificationsSettingsRequestDto from a dict
rooms_notifications_settings_request_dto_from_dict = RoomsNotificationsSettingsRequestDto.from_dict(rooms_notifications_settings_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


