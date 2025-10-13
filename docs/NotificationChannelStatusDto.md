# NotificationChannelStatusDto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | [**List[NotificationChannelDto]**](NotificationChannelDto.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.notification_channel_status_dto import NotificationChannelStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelStatusDto from a JSON string
notification_channel_status_dto_instance = NotificationChannelStatusDto.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelStatusDto.to_json())

# convert the object into a dict
notification_channel_status_dto_dict = notification_channel_status_dto_instance.to_dict()
# create an instance of NotificationChannelStatusDto from a dict
notification_channel_status_dto_from_dict = NotificationChannelStatusDto.from_dict(notification_channel_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


