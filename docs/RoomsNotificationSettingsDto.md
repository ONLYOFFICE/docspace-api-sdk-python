# RoomsNotificationSettingsDto
The rooms notification settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_rooms** | **List[object]** | The list of rooms with the disabled notifications. | [optional] 

## Example

```python
from docspace-api-python.models.rooms_notification_settings_dto import RoomsNotificationSettingsDto

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


