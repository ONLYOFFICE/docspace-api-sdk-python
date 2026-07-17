# NewItemsDtoAgentNewItemsDto
The new item parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | 
**items** | [**List[AgentNewItemsDto]**](AgentNewItemsDto.md) | The list of items. | 

## Example

```python
from docspace_api_sdk.models.new_items_dto_agent_new_items_dto import NewItemsDtoAgentNewItemsDto

# TODO update the JSON string below
json = "{}"
# create an instance of NewItemsDtoAgentNewItemsDto from a JSON string
new_items_dto_agent_new_items_dto_instance = NewItemsDtoAgentNewItemsDto.from_json(json)
# print the JSON string representation of the object
print(NewItemsDtoAgentNewItemsDto.to_json())

# convert the object into a dict
new_items_dto_agent_new_items_dto_dict = new_items_dto_agent_new_items_dto_instance.to_dict()
# create an instance of NewItemsDtoAgentNewItemsDto from a dict
new_items_dto_agent_new_items_dto_from_dict = NewItemsDtoAgentNewItemsDto.from_dict(new_items_dto_agent_new_items_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


