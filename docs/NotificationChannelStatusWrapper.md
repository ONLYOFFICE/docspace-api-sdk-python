# NotificationChannelStatusWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**NotificationChannelStatusDto**](NotificationChannelStatusDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.notification_channel_status_wrapper import NotificationChannelStatusWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationChannelStatusWrapper from a JSON string
notification_channel_status_wrapper_instance = NotificationChannelStatusWrapper.from_json(json)
# print the JSON string representation of the object
print(NotificationChannelStatusWrapper.to_json())

# convert the object into a dict
notification_channel_status_wrapper_dict = notification_channel_status_wrapper_instance.to_dict()
# create an instance of NotificationChannelStatusWrapper from a dict
notification_channel_status_wrapper_from_dict = NotificationChannelStatusWrapper.from_dict(notification_channel_status_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


