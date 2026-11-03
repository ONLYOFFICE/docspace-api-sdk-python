# AiContextRoom
A room the caller can connect to a chat as context.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The room ID. | 
**name** | **str** | The room title. | 

## Example

```python
from docspace_api_sdk.models.ai_context_room import AiContextRoom

# TODO update the JSON string below
json = "{}"
# create an instance of AiContextRoom from a JSON string
ai_context_room_instance = AiContextRoom.from_json(json)
# print the JSON string representation of the object
print(AiContextRoom.to_json())

# convert the object into a dict
ai_context_room_dict = ai_context_room_instance.to_dict()
# create an instance of AiContextRoom from a dict
ai_context_room_from_dict = AiContextRoom.from_dict(ai_context_room_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


