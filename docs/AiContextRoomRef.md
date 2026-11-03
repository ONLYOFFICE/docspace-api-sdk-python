# AiContextRoomRef
One Instructions room a round runs with as context: the account and room ID from `GET api/2.0/ai/context/get-context-folders`, plus the skills of the room the round may use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud** | **str** | The account the room belongs to; `docspace` for a room of this portal. | 
**id** | **str** | The room ID. | 
**skills** | [**List[AiRoomSkill]**](AiRoomSkill.md) | The skills of the room the round may use, as `GET api/2.0/ai/context/get-room-skills` lists them. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_context_room_ref import AiContextRoomRef

# TODO update the JSON string below
json = "{}"
# create an instance of AiContextRoomRef from a JSON string
ai_context_room_ref_instance = AiContextRoomRef.from_json(json)
# print the JSON string representation of the object
print(AiContextRoomRef.to_json())

# convert the object into a dict
ai_context_room_ref_dict = ai_context_room_ref_instance.to_dict()
# create an instance of AiContextRoomRef from a dict
ai_context_room_ref_from_dict = AiContextRoomRef.from_dict(ai_context_room_ref_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


