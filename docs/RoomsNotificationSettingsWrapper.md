# RoomsNotificationSettingsWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**RoomsNotificationSettingsDto**](RoomsNotificationSettingsDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

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


