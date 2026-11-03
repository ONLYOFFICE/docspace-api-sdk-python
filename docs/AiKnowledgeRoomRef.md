# AiKnowledgeRoomRef
One Knowledge room a round searches: the account and room ID from `GET api/2.0/ai/context/get-knowledge-folders`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | **str** | The account the room belongs to; `docspace` for a room of this portal. | 
**id** | **str** | The room ID; anything that is not a positive integer is ignored. | 

## Example

```python
from docspace_api_sdk.models.ai_knowledge_room_ref import AiKnowledgeRoomRef

# TODO update the JSON string below
json = "{}"
# create an instance of AiKnowledgeRoomRef from a JSON string
ai_knowledge_room_ref_instance = AiKnowledgeRoomRef.from_json(json)
# print the JSON string representation of the object
print(AiKnowledgeRoomRef.to_json())

# convert the object into a dict
ai_knowledge_room_ref_dict = ai_knowledge_room_ref_instance.to_dict()
# create an instance of AiKnowledgeRoomRef from a dict
ai_knowledge_room_ref_from_dict = AiKnowledgeRoomRef.from_dict(ai_knowledge_room_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


