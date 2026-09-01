# AiNewItemsDtoAgentNewItemsDto
The new item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**AiApiDateTime**](AiApiDateTime.md) | The date and time when the new item was created. | 
**items** | [**List[AiAgentNewItemsDto]**](AiAgentNewItemsDto.md) | The list of items. | 

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


