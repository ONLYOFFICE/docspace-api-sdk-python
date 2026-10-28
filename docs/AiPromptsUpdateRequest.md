# AiPromptsUpdateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Prompt id to update. | 
**updates** | [**AiPromptsUpdateRequestUpdates**](AiPromptsUpdateRequestUpdates.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_prompts_update_request import AiPromptsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptsUpdateRequest from a JSON string
ai_prompts_update_request_instance = AiPromptsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AiPromptsUpdateRequest.to_json())

# convert the object into a dict
ai_prompts_update_request_dict = ai_prompts_update_request_instance.to_dict()
# create an instance of AiPromptsUpdateRequest from a dict
ai_prompts_update_request_from_dict = AiPromptsUpdateRequest.from_dict(ai_prompts_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


