# AiAgentNewItemsDto
The agent new item's information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**AiFileEntryBaseDto**](AiFileEntryBaseDto.md) | The agent file entry. | 
**items** | [**List[AiFileEntryBaseDto]**](AiFileEntryBaseDto.md) | The list of file entry items. | 

## Example

```python
from docspace_api_sdk.models.ai_agent_new_items_dto import AiAgentNewItemsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentNewItemsDto from a JSON string
ai_agent_new_items_dto_instance = AiAgentNewItemsDto.from_json(json)
# print the JSON string representation of the object
print(AiAgentNewItemsDto.to_json())

# convert the object into a dict
ai_agent_new_items_dto_dict = ai_agent_new_items_dto_instance.to_dict()
# create an instance of AiAgentNewItemsDto from a dict
ai_agent_new_items_dto_from_dict = AiAgentNewItemsDto.from_dict(ai_agent_new_items_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


