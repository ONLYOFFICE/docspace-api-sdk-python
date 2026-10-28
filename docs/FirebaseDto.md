# FirebaseDto
The Firebase project a client initialises its SDK with to receive push notifications from this portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** | The web API key of the project. Every field of this object is an empty string on an installation that  configures no Firebase project, and an empty `projectId` is the cheapest thing to test for before  initialising an SDK. None of these values is a secret - they are meant to be embedded in a client. | 
**auth_domain** | **str** | The host the Firebase SDK performs its own authentication against. | 
**project_id** | **str** | The identifier of the Firebase project itself, which ties all the other fields together. | 
**storage_bucket** | **str** | The Cloud Storage bucket of the project. The portal does not store portal files there; it is part of the  SDK configuration. | 
**messaging_sender_id** | **str** | The sender ID that push messages of this project arrive under, which a client checks an incoming message  against. | 
**app_id** | **str** | The identifier of the Firebase application registration this client is to use. | 
**measurement_id** | **str** | The Google Analytics measurement ID of the project, empty when the project reports no analytics. | 
**database_url** | **str** | The Realtime Database endpoint of the project, empty when the project has no such database. | 

## Example

```python
from docspace_api_sdk.models.firebase_dto import FirebaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FirebaseDto from a JSON string
firebase_dto_instance = FirebaseDto.from_json(json)
# print the JSON string representation of the object
print(FirebaseDto.to_json())

# convert the object into a dict
firebase_dto_dict = firebase_dto_instance.to_dict()
# create an instance of FirebaseDto from a dict
firebase_dto_from_dict = FirebaseDto.from_dict(firebase_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


