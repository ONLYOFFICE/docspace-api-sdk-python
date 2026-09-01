# AiOpenAIChatCompletionChunk

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**object** | **str** |  | 
**created** | **float** |  | 
**model** | **str** |  | 
**choices** | [**List[AiOpenAIChunkChoice]**](AiOpenAIChunkChoice.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_chat_completion_chunk import AiOpenAIChatCompletionChunk

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIChatCompletionChunk from a JSON string
ai_open_ai_chat_completion_chunk_instance = AiOpenAIChatCompletionChunk.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIChatCompletionChunk.to_json())

# convert the object into a dict
ai_open_ai_chat_completion_chunk_dict = ai_open_ai_chat_completion_chunk_instance.to_dict()
# create an instance of AiOpenAIChatCompletionChunk from a dict
ai_open_ai_chat_completion_chunk_from_dict = AiOpenAIChatCompletionChunk.from_dict(ai_open_ai_chat_completion_chunk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


