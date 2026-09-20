# NotificationSettingsDto
Whether one kind of notification is switched on for the calling user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationType**](NotificationType.md) | Which kind of notification the flag belongs to, echoed from the request. It is published as a number:  badges, room activity, the daily feed, and the tips. | [optional] 
**is_enabled** | **bool** | Whether the caller receives that kind of notification. It describes the caller's own account and nobody  else's; a fresh account has the badges on and the other three off, because those are subscriptions that  only `POST api/2.0/settings/notification` creates. | [optional] 

## Example

```python
from docspace_api_sdk.models.notification_settings_dto import NotificationSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSettingsDto from a JSON string
notification_settings_dto_instance = NotificationSettingsDto.from_json(json)
# print the JSON string representation of the object
print(NotificationSettingsDto.to_json())

# convert the object into a dict
notification_settings_dto_dict = notification_settings_dto_instance.to_dict()
# create an instance of NotificationSettingsDto from a dict
notification_settings_dto_from_dict = NotificationSettingsDto.from_dict(notification_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


