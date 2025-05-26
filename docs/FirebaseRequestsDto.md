# FirebaseRequestsDto

The Firebase-related request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**firebase_device_token** | **str** | The Firebase device token. | [optional] 
**is_subscribed** | **bool** | Specifies whether the user is subscribed to the push notifications or not. | [optional] 

## Example

```python
from docspace.models.firebase_requests_dto import FirebaseRequestsDto

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


