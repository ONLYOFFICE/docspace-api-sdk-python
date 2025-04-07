# RoomsNotificationsSettingsRequestDto

Request parameters for the room notification settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms_id** | **object** | Room ID | [optional] 
**mute** | **bool** | Specifies if the room notifications are disabled or not | [optional] 

## Example

```python
from docspace.models.rooms_notifications_settings_request_dto import RoomsNotificationsSettingsRequestDto

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


