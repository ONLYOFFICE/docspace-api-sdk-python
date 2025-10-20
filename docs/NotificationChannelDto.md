# NotificationChannelDto
The notification channel information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The notification channel name. | 
**is_enabled** | **bool** | Specifies whether the notification channel is enabled. | 

## Example

```python
from docspace_api_sdk.models.notification_channel_dto import NotificationChannelDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelDto from a JSON string
notification_channel_dto_instance = NotificationChannelDto.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelDto.to_json())

# convert the object into a dict
notification_channel_dto_dict = notification_channel_dto_instance.to_dict()
# create an instance of NotificationChannelDto from a dict
notification_channel_dto_from_dict = NotificationChannelDto.from_dict(notification_channel_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


