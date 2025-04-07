# NotificationSettingsRequestsDto

Notification settings request parameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationType**](NotificationType.md) |  | [optional] 
**is_enabled** | **bool** | Specifies if the notification type is enabled or not | [optional] 

## Example

```python
from docspace.models.notification_settings_requests_dto import NotificationSettingsRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationSettingsRequestsDto from a JSON string
notification_settings_requests_dto_instance = NotificationSettingsRequestsDto.from_json(json)
# print the JSON string representation of the object
print(NotificationSettingsRequestsDto.to_json())

# convert the object into a dict
notification_settings_requests_dto_dict = notification_settings_requests_dto_instance.to_dict()
# create an instance of NotificationSettingsRequestsDto from a dict
notification_settings_requests_dto_from_dict = NotificationSettingsRequestsDto.from_dict(notification_settings_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


