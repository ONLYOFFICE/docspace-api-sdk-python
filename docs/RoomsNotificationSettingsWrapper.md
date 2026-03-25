# RoomsNotificationSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RoomsNotificationSettingsDto**](RoomsNotificationSettingsDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.rooms_notification_settings_wrapper import RoomsNotificationSettingsWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of RoomsNotificationSettingsWrapper from a JSON string
rooms_notification_settings_wrapper_instance = RoomsNotificationSettingsWrapper.from_json(json)
# print the JSON string representation of the object
print(RoomsNotificationSettingsWrapper.to_json())

# convert the object into a dict
rooms_notification_settings_wrapper_dict = rooms_notification_settings_wrapper_instance.to_dict()
# create an instance of RoomsNotificationSettingsWrapper from a dict
rooms_notification_settings_wrapper_from_dict = RoomsNotificationSettingsWrapper.from_dict(rooms_notification_settings_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


