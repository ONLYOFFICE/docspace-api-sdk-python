# AiThreadsOpenOrCreateRequestEntityMeta
Optional entity hint (lib 0.5.64): only `entityId` is read; the pair is re-resolved server-side before reaching the provider as metadata.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **str** |  | [optional] 
**entity_title** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_threads_open_or_create_request_entity_meta import AiThreadsOpenOrCreateRequestEntityMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsOpenOrCreateRequestEntityMeta from a JSON string
ai_threads_open_or_create_request_entity_meta_instance = AiThreadsOpenOrCreateRequestEntityMeta.from_json(json)
# print the JSON string representation of the object
print(AiThreadsOpenOrCreateRequestEntityMeta.to_json())

# convert the object into a dict
ai_threads_open_or_create_request_entity_meta_dict = ai_threads_open_or_create_request_entity_meta_instance.to_dict()
# create an instance of AiThreadsOpenOrCreateRequestEntityMeta from a dict
ai_threads_open_or_create_request_entity_meta_from_dict = AiThreadsOpenOrCreateRequestEntityMeta.from_dict(ai_threads_open_or_create_request_entity_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


