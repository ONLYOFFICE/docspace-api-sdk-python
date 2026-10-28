# AiPrompt
Saved prompt template that users can quickly insert into the chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique prompt identifier (UUID). | 
**name** | **str** | Prompt display name shown in the prompt picker. | 
**text** | **str** | Prompt template text. May contain placeholder tokens. | 
**folder_id** | **str** | Optional parent folder ID. `undefined` means the prompt is at the root level. | [optional] 
**created_at** | **float** | Timestamp (ms since epoch) when the prompt was created. | 
**updated_at** | **float** | Timestamp (ms since epoch) of the last prompt modification. | 

## Example

```python
from docspace_api_sdk.models.ai_prompt import AiPrompt

# TODO update the JSON string below
json = "{}"
# create an instance of AiPrompt from a JSON string
ai_prompt_instance = AiPrompt.from_json(json)
# print the JSON string representation of the object
print(AiPrompt.to_json())

# convert the object into a dict
ai_prompt_dict = ai_prompt_instance.to_dict()
# create an instance of AiPrompt from a dict
ai_prompt_from_dict = AiPrompt.from_dict(ai_prompt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


