# AgentNewItemsDto
The agent new item's information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**FileEntryBaseDto**](FileEntryBaseDto.md) |  | 
**items** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of file entry items. | 

## Example

```python
from docspace_api_sdk.models.agent_new_items_dto import AgentNewItemsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AgentNewItemsDto from a JSON string
agent_new_items_dto_instance = AgentNewItemsDto.from_json(json)
# print the JSON string representation of the object
print(AgentNewItemsDto.to_json())

# convert the object into a dict
agent_new_items_dto_dict = agent_new_items_dto_instance.to_dict()
# create an instance of AgentNewItemsDto from a dict
agent_new_items_dto_from_dict = AgentNewItemsDto.from_dict(agent_new_items_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


