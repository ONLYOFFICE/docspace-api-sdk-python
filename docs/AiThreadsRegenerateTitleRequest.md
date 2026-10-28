# AiThreadsRegenerateTitleRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** |  | 
**profile** | [**AiProfile**](AiProfile.md) | Profile used to regenerate the title. | 
**entity_meta** | [**AiThreadsOpenOrCreateRequestEntityMeta**](AiThreadsOpenOrCreateRequestEntityMeta.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_threads_regenerate_title_request import AiThreadsRegenerateTitleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsRegenerateTitleRequest from a JSON string
ai_threads_regenerate_title_request_instance = AiThreadsRegenerateTitleRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsRegenerateTitleRequest.to_json())

# convert the object into a dict
ai_threads_regenerate_title_request_dict = ai_threads_regenerate_title_request_instance.to_dict()
# create an instance of AiThreadsRegenerateTitleRequest from a dict
ai_threads_regenerate_title_request_from_dict = AiThreadsRegenerateTitleRequest.from_dict(ai_threads_regenerate_title_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


