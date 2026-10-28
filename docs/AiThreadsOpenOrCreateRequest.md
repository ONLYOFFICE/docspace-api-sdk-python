# AiThreadsOpenOrCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** |  | [optional] 
**profile** | [**AiProfile**](AiProfile.md) | Profile the title generation runs on. | 
**profile_id** | **str** |  | 
**first_message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | First user message a fresh thread derives its title from. | 
**entity_id** | **str** | Opaque scope token persisted on a freshly created thread. | [optional] 
**entity_meta** | [**AiThreadsOpenOrCreateRequestEntityMeta**](AiThreadsOpenOrCreateRequestEntityMeta.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_threads_open_or_create_request import AiThreadsOpenOrCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsOpenOrCreateRequest from a JSON string
ai_threads_open_or_create_request_instance = AiThreadsOpenOrCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsOpenOrCreateRequest.to_json())

# convert the object into a dict
ai_threads_open_or_create_request_dict = ai_threads_open_or_create_request_instance.to_dict()
# create an instance of AiThreadsOpenOrCreateRequest from a dict
ai_threads_open_or_create_request_from_dict = AiThreadsOpenOrCreateRequest.from_dict(ai_threads_open_or_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


