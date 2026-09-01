# AiThreadsCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Thread title. | 
**profile_id** | **str** | Optional profile to bind. | [optional] 
**entity_id** | **str** | Optional entity (room) scope. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_threads_create_request import AiThreadsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsCreateRequest from a JSON string
ai_threads_create_request_instance = AiThreadsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsCreateRequest.to_json())

# convert the object into a dict
ai_threads_create_request_dict = ai_threads_create_request_instance.to_dict()
# create an instance of AiThreadsCreateRequest from a dict
ai_threads_create_request_from_dict = AiThreadsCreateRequest.from_dict(ai_threads_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


