# AiOpenAIChoiceDelta
The incremental part of one choice - what this chunk adds to the assistant message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | Sent on the first chunk only, always `assistant`. | [optional] 
**content** | **str** | The text this chunk appends. Null when the chunk carries no text. | [optional] 
**tool_calls** | [**List[AiOpenAIToolCallDelta]**](AiOpenAIToolCallDelta.md) | The tool calls the model requested, emitted in place of text. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_choice_delta import AiOpenAIChoiceDelta

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIChoiceDelta from a JSON string
ai_open_ai_choice_delta_instance = AiOpenAIChoiceDelta.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIChoiceDelta.to_json())

# convert the object into a dict
ai_open_ai_choice_delta_dict = ai_open_ai_choice_delta_instance.to_dict()
# create an instance of AiOpenAIChoiceDelta from a dict
ai_open_ai_choice_delta_from_dict = AiOpenAIChoiceDelta.from_dict(ai_open_ai_choice_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


