# AiOpenAIChunkChoice
One choice of a streaming completion, carrying the part this chunk adds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | The zero-based position of the choice. This service emits a single choice, so always 0. | 
**delta** | [**AiOpenAIChoiceDelta**](AiOpenAIChoiceDelta.md) | What this chunk adds to the choice. | 
**finish_reason** | [**AiOpenAIFinishReason**](AiOpenAIFinishReason.md) | Why the completion stopped, or null while it is still streaming. | 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_chunk_choice import AiOpenAIChunkChoice

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIChunkChoice from a JSON string
ai_open_ai_chunk_choice_instance = AiOpenAIChunkChoice.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIChunkChoice.to_json())

# convert the object into a dict
ai_open_ai_chunk_choice_dict = ai_open_ai_chunk_choice_instance.to_dict()
# create an instance of AiOpenAIChunkChoice from a dict
ai_open_ai_chunk_choice_from_dict = AiOpenAIChunkChoice.from_dict(ai_open_ai_chunk_choice_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


