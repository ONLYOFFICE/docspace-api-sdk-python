# NotificationSettingsDto
The notification settings parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationType**](NotificationType.md) |  | [optional] 
**is_enabled** | **bool** | Specifies if the notification type is enabled or not. | [optional] 

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


