# NotificationChannelDto
One delivery channel of the installation, with the state it is in for this portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The internal name of the channel as the notification service knows it - `email.sender` for letters,  `telegram.sender` for Telegram messages. It is a key to match on, not a label to print. | 
**is_enabled** | **bool** | Whether the channel can deliver for this portal. Letters are enabled whenever the channel is listed at  all, while Telegram is enabled only while the portal has a bot name and token stored. It says nothing  about the caller, who also has to connect their own Telegram account through  `GET api/2.0/settings/telegram/link`. | 

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


