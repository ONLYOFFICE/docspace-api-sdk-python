# AiAiRegenerateStreamRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Target thread (must already exist). | 
**action_args** | [**AiAiActionArgs**](AiAiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 
**profile_id** | **str** | Session-level profile override for this request only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_regenerate_stream_request import AiAiRegenerateStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiRegenerateStreamRequest from a JSON string
ai_ai_regenerate_stream_request_instance = AiAiRegenerateStreamRequest.from_json(json)
# print the JSON string representation of the object
print(AiAiRegenerateStreamRequest.to_json())

# convert the object into a dict
ai_ai_regenerate_stream_request_dict = ai_ai_regenerate_stream_request_instance.to_dict()
# create an instance of AiAiRegenerateStreamRequest from a dict
ai_ai_regenerate_stream_request_from_dict = AiAiRegenerateStreamRequest.from_dict(ai_ai_regenerate_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


