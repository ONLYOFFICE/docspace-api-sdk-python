# AiOpenAIStreamChunk
A chunk or the terminal error envelope emitted on a failed stream.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The completion identifier, stable across every chunk of one response. | 
**object** | **str** | Always `chat.completion.chunk`. | 
**created** | **float** | When the completion started, in Unix seconds. | 
**model** | **str** | The model that produced the completion - the resolved profile's model. | 
**choices** | [**List[AiOpenAIChunkChoice]**](AiOpenAIChunkChoice.md) | The choices carried by this chunk. This service emits exactly one. | 
**error** | [**AiOpenAIStreamErrorError**](AiOpenAIStreamErrorError.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_stream_chunk import AiOpenAIStreamChunk

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIStreamChunk from a JSON string
ai_open_ai_stream_chunk_instance = AiOpenAIStreamChunk.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIStreamChunk.to_json())

# convert the object into a dict
ai_open_ai_stream_chunk_dict = ai_open_ai_stream_chunk_instance.to_dict()
# create an instance of AiOpenAIStreamChunk from a dict
ai_open_ai_stream_chunk_from_dict = AiOpenAIStreamChunk.from_dict(ai_open_ai_stream_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


