# AiAiActionArgsPrompt
Override the action's baked-in system prompt (replace or append).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mode** | **str** |  | 
**text** | **str** |  | 

## Example

```python
from docspace_api_sdk.models.ai_ai_action_args_prompt import AiAiActionArgsPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiActionArgsPrompt from a JSON string
ai_ai_action_args_prompt_instance = AiAiActionArgsPrompt.from_json(json)
# print the JSON string representation of the object
print(AiAiActionArgsPrompt.to_json())

# convert the object into a dict
ai_ai_action_args_prompt_dict = ai_ai_action_args_prompt_instance.to_dict()
# create an instance of AiAiActionArgsPrompt from a dict
ai_ai_action_args_prompt_from_dict = AiAiActionArgsPrompt.from_dict(ai_ai_action_args_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


