# AiOpenAIChunkChoice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | 
**delta** | [**AiOpenAIChoiceDelta**](AiOpenAIChoiceDelta.md) |  | 
**finish_reason** | [**AiOpenAIFinishReason**](AiOpenAIFinishReason.md) |  | 

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


