# FirebaseRequestsDto
Which mobile device receives the Documents push notifications, and whether it is subscribed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firebase_device_token** | **str** | The registration token Firebase issued to the mobile client for this device, obtained on the device itself.  It is kept as an opaque string of up to 255 characters and is never verified here; it identifies the device  and is matched but never changed, and a token belonging to another member or another portal matches nothing. | [optional] 
**is_subscribed** | **bool** | Whether the device is to receive the room activity messages - an invitation, a role change, an archived room,  a new document. On a first registration it is stored as given; on a registration that already exists it is  ignored, because registering does not update, and the subscription is changed with  `PUT api/2.0/settings/push/docsubscribe` instead. | [optional] 

## Example

```python
from docspace_api_sdk.models.firebase_requests_dto import FirebaseRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of FirebaseRequestsDto from a JSON string
firebase_requests_dto_instance = FirebaseRequestsDto.from_json(json)
# print the JSON string representation of the object
print(FirebaseRequestsDto.to_json())

# convert the object into a dict
firebase_requests_dto_dict = firebase_requests_dto_instance.to_dict()
# create an instance of FirebaseRequestsDto from a dict
firebase_requests_dto_from_dict = FirebaseRequestsDto.from_dict(firebase_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


