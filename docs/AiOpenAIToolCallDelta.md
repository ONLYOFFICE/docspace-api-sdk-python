# AiOpenAIToolCallDelta
The incremental part of one tool call the model requested.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** | The zero-based position of the tool call within the message. | 
**id** | **str** | The tool call identifier, quoted back when its result is submitted. | [optional] 
**type** | **str** | Always `function` - the only tool kind the API defines. | [optional] 
**function** | [**AiOpenAIToolCallDeltaFunction**](AiOpenAIToolCallDeltaFunction.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_tool_call_delta import AiOpenAIToolCallDelta

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIToolCallDelta from a JSON string
ai_open_ai_tool_call_delta_instance = AiOpenAIToolCallDelta.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIToolCallDelta.to_json())

# convert the object into a dict
ai_open_ai_tool_call_delta_dict = ai_open_ai_tool_call_delta_instance.to_dict()
# create an instance of AiOpenAIToolCallDelta from a dict
ai_open_ai_tool_call_delta_from_dict = AiOpenAIToolCallDelta.from_dict(ai_open_ai_tool_call_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


