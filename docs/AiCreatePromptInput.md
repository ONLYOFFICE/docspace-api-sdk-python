# AiCreatePromptInput
Input for creating a prompt — the engine generates `id`/`createdAt`/`updatedAt`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The prompt name. | 
**text** | **str** | The prompt body. | 
**folder_id** | **str** | The folder to file the prompt under. Omit or send null to leave it outside any folder. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_create_prompt_input import AiCreatePromptInput

# TODO update the JSON string below
json = "{}"
# create an instance of AiCreatePromptInput from a JSON string
ai_create_prompt_input_instance = AiCreatePromptInput.from_json(json)
# print the JSON string representation of the object
print(AiCreatePromptInput.to_json())

# convert the object into a dict
ai_create_prompt_input_dict = ai_create_prompt_input_instance.to_dict()
# create an instance of AiCreatePromptInput from a dict
ai_create_prompt_input_from_dict = AiCreatePromptInput.from_dict(ai_create_prompt_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


