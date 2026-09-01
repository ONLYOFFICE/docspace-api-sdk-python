# AiOpenAIToolCallDelta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | 
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
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


