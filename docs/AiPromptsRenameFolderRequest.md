# AiPromptsRenameFolderRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Folder id to rename. | 
**name** | **str** | New folder name. | 

## Example

```python
from docspace_api_sdk.models.ai_prompts_rename_folder_request import AiPromptsRenameFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptsRenameFolderRequest from a JSON string
ai_prompts_rename_folder_request_instance = AiPromptsRenameFolderRequest.from_json(json)
# print the JSON string representation of the object
print(AiPromptsRenameFolderRequest.to_json())

# convert the object into a dict
ai_prompts_rename_folder_request_dict = ai_prompts_rename_folder_request_instance.to_dict()
# create an instance of AiPromptsRenameFolderRequest from a dict
ai_prompts_rename_folder_request_from_dict = AiPromptsRenameFolderRequest.from_dict(ai_prompts_rename_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


