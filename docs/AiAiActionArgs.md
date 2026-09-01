# AiAiActionArgs
Wire-serializable subset of the engine's `ActionArgs` — drops the engine-injected `signal`/`fetch`; `profile`/`messages` are owned by the engine and never sent by the caller.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | [**List[AiTMCPItem]**](AiTMCPItem.md) | Extra tools offered to the model for this request. | [optional] 
**is_reasoning** | **bool** | Enable extended thinking / reasoning for this request. | [optional] 
**prompt** | [**AiAiActionArgsPrompt**](AiAiActionArgsPrompt.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_action_args import AiAiActionArgs

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiActionArgs from a JSON string
ai_ai_action_args_instance = AiAiActionArgs.from_json(json)
# print the JSON string representation of the object
print(AiAiActionArgs.to_json())

# convert the object into a dict
ai_ai_action_args_dict = ai_ai_action_args_instance.to_dict()
# create an instance of AiAiActionArgs from a dict
ai_ai_action_args_from_dict = AiAiActionArgs.from_dict(ai_ai_action_args_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


