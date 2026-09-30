# NotificationSettingsRequestsDto
Which kind of notification the calling user switches, and which way.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**NotificationType**](NotificationType.md) | The kind of notification being switched. A value outside the defined set is echoed back while nothing is  stored, so confirm the result with `GET api/2.0/settings/notification/{type}` rather than trusting the  answer. | 
**is_enabled** | **bool** | Whether that kind reaches the calling account. It applies to the caller own account alone and to every room  at once; a single room is silenced with `POST api/2.0/settings/notification/rooms` instead. | [optional] 

## Example

```python
from docspace_api_sdk.models.notification_settings_requests_dto import NotificationSettingsRequestsDto

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


