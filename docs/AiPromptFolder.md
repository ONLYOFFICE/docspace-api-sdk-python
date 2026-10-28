# AiPromptFolder
Folder for organizing saved prompts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique folder identifier (UUID). | 
**name** | **str** | Folder display name. | 
**created_at** | **float** | Timestamp (ms since epoch) when the folder was created. | 
**updated_at** | **float** | Timestamp (ms since epoch) of the last folder modification. | 

## Example

```python
from docspace_api_sdk.models.ai_prompt_folder import AiPromptFolder

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptFolder from a JSON string
ai_prompt_folder_instance = AiPromptFolder.from_json(json)
# print the JSON string representation of the object
print(AiPromptFolder.to_json())

# convert the object into a dict
ai_prompt_folder_dict = ai_prompt_folder_instance.to_dict()
# create an instance of AiPromptFolder from a dict
ai_prompt_folder_from_dict = AiPromptFolder.from_dict(ai_prompt_folder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


