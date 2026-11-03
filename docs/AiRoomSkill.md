# AiRoomSkill
A skill of an Instructions room: the frontmatter of one Markdown skill file. `name` and `description` are what the model is shown; the body is read through `GET api/2.0/ai/context/get-room-skill`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The skill's ID, as `GET api/2.0/ai/context/get-room-skill` takes it. | 
**name** | **str** | The skill's name, from its frontmatter. | 
**description** | **str** | What the skill is for, from its frontmatter; empty when it declares none. | 

## Example

```python
from docspace_api_sdk.models.ai_room_skill import AiRoomSkill

# TODO update the JSON string below
json = "{}"
# create an instance of AiRoomSkill from a JSON string
ai_room_skill_instance = AiRoomSkill.from_json(json)
# print the JSON string representation of the object
print(AiRoomSkill.to_json())

# convert the object into a dict
ai_room_skill_dict = ai_room_skill_instance.to_dict()
# create an instance of AiRoomSkill from a dict
ai_room_skill_from_dict = AiRoomSkill.from_dict(ai_room_skill_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


