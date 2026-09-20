# AiNewItemsDtoAgentNewItemsDto
One day of the entries the caller has not opened yet, the groups running from the most recent day backwards.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**AiApiDateTime**](AiApiDateTime.md) | The day the grouped entries were last changed, written with the offset of the portal time zone. The time part  is the moment of the newest entry of the group. | 
**items** | [**List[AiAgentNewItemsDto]**](AiAgentNewItemsDto.md) | What changed on that day, the most recent first. Folders are left out of it, so an entry here is always a file  or a room that holds them. | 

## Example

```python
from docspace_api_sdk.models.ai_new_items_dto_agent_new_items_dto import AiNewItemsDtoAgentNewItemsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiNewItemsDtoAgentNewItemsDto from a JSON string
ai_new_items_dto_agent_new_items_dto_instance = AiNewItemsDtoAgentNewItemsDto.from_json(json)
# print the JSON string representation of the object
print(AiNewItemsDtoAgentNewItemsDto.to_json())

# convert the object into a dict
ai_new_items_dto_agent_new_items_dto_dict = ai_new_items_dto_agent_new_items_dto_instance.to_dict()
# create an instance of AiNewItemsDtoAgentNewItemsDto from a dict
ai_new_items_dto_agent_new_items_dto_from_dict = AiNewItemsDtoAgentNewItemsDto.from_dict(ai_new_items_dto_agent_new_items_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


