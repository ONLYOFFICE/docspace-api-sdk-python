# AiSkillsDto
Instructions rooms with their skills.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rooms** | [**List[AiSkillsRoomDto]**](AiSkillsRoomDto.md) | The rooms, sorted by title. | 

## Example

```python
from docspace_api_sdk.models.ai_skills_dto import AiSkillsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiSkillsDto from a JSON string
ai_skills_dto_instance = AiSkillsDto.from_json(json)
# print the JSON string representation of the object
print(AiSkillsDto.to_json())

# convert the object into a dict
ai_skills_dto_dict = ai_skills_dto_instance.to_dict()
# create an instance of AiSkillsDto from a dict
ai_skills_dto_from_dict = AiSkillsDto.from_dict(ai_skills_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


