# FirebaseDeviceDto
One mobile device of the calling user registered for push notifications.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the registration. | [optional] 
**user_id** | **UUID** | The account the device belongs to; always the caller. | [optional] 
**tenant_id** | **int** | The portal the registration belongs to; always the current one. | [optional] 
**firebase_device_token** | **str** | The Firebase token the device was issued, as it was sent at registration. | [optional] 
**application** | **str** | The application the registration is for; `doc` for the Documents application. | [optional] 
**is_subscribed** | **bool** | Whether the device is currently sent push notifications. | [optional] 

## Example

```python
from docspace_api_sdk.models.firebase_device_dto import FirebaseDeviceDto

# TODO update the JSON string below
json = "{}"
# create an instance of FirebaseDeviceDto from a JSON string
firebase_device_dto_instance = FirebaseDeviceDto.from_json(json)
# print the JSON string representation of the object
print(FirebaseDeviceDto.to_json())

# convert the object into a dict
firebase_device_dto_dict = firebase_device_dto_instance.to_dict()
# create an instance of FirebaseDeviceDto from a dict
firebase_device_dto_from_dict = FirebaseDeviceDto.from_dict(firebase_device_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


