# AiPromptsUpdateRequestUpdates
Fields to change.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**folder_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_prompts_update_request_updates import AiPromptsUpdateRequestUpdates

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptsUpdateRequestUpdates from a JSON string
ai_prompts_update_request_updates_instance = AiPromptsUpdateRequestUpdates.from_json(json)
# print the JSON string representation of the object
print(AiPromptsUpdateRequestUpdates.to_json())

# convert the object into a dict
ai_prompts_update_request_updates_dict = ai_prompts_update_request_updates_instance.to_dict()
# create an instance of AiPromptsUpdateRequestUpdates from a dict
ai_prompts_update_request_updates_from_dict = AiPromptsUpdateRequestUpdates.from_dict(ai_prompts_update_request_updates_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


