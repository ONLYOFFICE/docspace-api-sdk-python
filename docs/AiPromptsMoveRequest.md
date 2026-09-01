# AiPromptsMoveRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Prompt id to move. | 
**folder_id** | **str** | Target folder id, or `null` for root. | 

## Example

```python
from docspace_api_sdk.models.ai_prompts_move_request import AiPromptsMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiPromptsMoveRequest from a JSON string
ai_prompts_move_request_instance = AiPromptsMoveRequest.from_json(json)
# print the JSON string representation of the object
print(AiPromptsMoveRequest.to_json())

# convert the object into a dict
ai_prompts_move_request_dict = ai_prompts_move_request_instance.to_dict()
# create an instance of AiPromptsMoveRequest from a dict
ai_prompts_move_request_from_dict = AiPromptsMoveRequest.from_dict(ai_prompts_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


