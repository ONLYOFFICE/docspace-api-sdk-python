# RoomsNotificationSettingsDto
The rooms the calling user has silenced.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_rooms** | **List[object]** | The identifiers of the silenced rooms, in the order they were added, and belonging to the caller's own  account alone. They are kept as opaque values, so a numeric identifier of a portal room and a string  identifier of a room on a connected third-party account both appear here, and an identifier stays on the  list after its room is deleted. An empty list means nothing is silenced. | [optional] 

## Example

```python
from docspace_api_sdk.models.rooms_notification_settings_dto import RoomsNotificationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RoomsNotificationSettingsDto from a JSON string
rooms_notification_settings_dto_instance = RoomsNotificationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(RoomsNotificationSettingsDto.to_json())

# convert the object into a dict
rooms_notification_settings_dto_dict = rooms_notification_settings_dto_instance.to_dict()
# create an instance of RoomsNotificationSettingsDto from a dict
rooms_notification_settings_dto_from_dict = RoomsNotificationSettingsDto.from_dict(rooms_notification_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


