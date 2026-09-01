# AiPromptMutationResult
Outcome of `create` / `update` / `move` on a prompt — either the persisted prompt or a field-scoped error.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the prompt was persisted. | 
**prompt** | [**AiPrompt**](AiPrompt.md) | The persisted prompt. Present on success. | [optional] 
**error** | [**AiTErrorData**](AiTErrorData.md) | Why the prompt was rejected. Present on failure. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_prompt_mutation_result import AiPromptMutationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptMutationResult from a JSON string
ai_prompt_mutation_result_instance = AiPromptMutationResult.from_json(json)
# print the JSON string representation of the object
print(AiPromptMutationResult.to_json())

# convert the object into a dict
ai_prompt_mutation_result_dict = ai_prompt_mutation_result_instance.to_dict()
# create an instance of AiPromptMutationResult from a dict
ai_prompt_mutation_result_from_dict = AiPromptMutationResult.from_dict(ai_prompt_mutation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


