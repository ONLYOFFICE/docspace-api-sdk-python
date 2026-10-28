# AiActionArgs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | [**List[AiMCPItem]**](AiMCPItem.md) | Extra tools offered to the model for this request. | [optional] 
**is_reasoning** | **bool** | Legacy extended-thinking switch; stands for `medium`. `reasoningLevel` wins when both are set. | [optional] 
**reasoning_level** | [**AiReasoningLevel**](AiReasoningLevel.md) | Depth of extended thinking for the round; providers clamp it to what the model accepts. | [optional] 
**prompt** | [**AiActionArgsPrompt**](AiActionArgsPrompt.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_action_args import AiActionArgs

# TODO update the JSON string below
json = "{}"
# create an instance of AiActionArgs from a JSON string
ai_action_args_instance = AiActionArgs.from_json(json)
# print the JSON string representation of the object
print(AiActionArgs.to_json())

# convert the object into a dict
ai_action_args_dict = ai_action_args_instance.to_dict()
# create an instance of AiActionArgs from a dict
ai_action_args_from_dict = AiActionArgs.from_dict(ai_action_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


