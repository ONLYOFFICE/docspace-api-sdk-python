# AiRegenerateStreamRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Target thread (must already exist). | 
**action_args** | [**AiActionArgs**](AiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 
**profile_id** | **str** | Session-level profile override for this request only. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_regenerate_stream_request import AiRegenerateStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiRegenerateStreamRequest from a JSON string
ai_regenerate_stream_request_instance = AiRegenerateStreamRequest.from_json(json)
# print the JSON string representation of the object
print(AiRegenerateStreamRequest.to_json())

# convert the object into a dict
ai_regenerate_stream_request_dict = ai_regenerate_stream_request_instance.to_dict()
# create an instance of AiRegenerateStreamRequest from a dict
ai_regenerate_stream_request_from_dict = AiRegenerateStreamRequest.from_dict(ai_regenerate_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


