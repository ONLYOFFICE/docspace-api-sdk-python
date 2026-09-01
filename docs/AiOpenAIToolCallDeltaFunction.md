# AiOpenAIToolCallDeltaFunction
The call itself: the function name and its JSON-encoded arguments.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**arguments** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_tool_call_delta_function import AiOpenAIToolCallDeltaFunction

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIToolCallDeltaFunction from a JSON string
ai_open_ai_tool_call_delta_function_instance = AiOpenAIToolCallDeltaFunction.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIToolCallDeltaFunction.to_json())

# convert the object into a dict
ai_open_ai_tool_call_delta_function_dict = ai_open_ai_tool_call_delta_function_instance.to_dict()
# create an instance of AiOpenAIToolCallDeltaFunction from a dict
ai_open_ai_tool_call_delta_function_from_dict = AiOpenAIToolCallDeltaFunction.from_dict(ai_open_ai_tool_call_delta_function_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


