# AiSkillsRoomDto
An Instructions room with its skills.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the room. | 
**title** | **str** | Room title. | 
**logo** | [**LogoDto**](LogoDto.md) | Room logo. | 
**skills** | [**List[AiSkillDto]**](AiSkillDto.md) | Skills of the room, sorted by file title. | 

## Example

```python
from docspace_api_sdk.models.ai_skills_room_dto import AiSkillsRoomDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiSkillsRoomDto from a JSON string
ai_skills_room_dto_instance = AiSkillsRoomDto.from_json(json)
# print the JSON string representation of the object
print(AiSkillsRoomDto.to_json())

# convert the object into a dict
ai_skills_room_dto_dict = ai_skills_room_dto_instance.to_dict()
# create an instance of AiSkillsRoomDto from a dict
ai_skills_room_dto_from_dict = AiSkillsRoomDto.from_dict(ai_skills_room_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


