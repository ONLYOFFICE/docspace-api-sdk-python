# AiSkillDto
A skill of an Instructions room: a Markdown file in the room root with a YAML frontmatter.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the skill file. | 
**name** | **str** | Skill name from the frontmatter. | 
**description** | **str** | Skill description from the frontmatter. | 

## Example

```python
from docspace_api_sdk.models.ai_skill_dto import AiSkillDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiSkillDto from a JSON string
ai_skill_dto_instance = AiSkillDto.from_json(json)
# print the JSON string representation of the object
print(AiSkillDto.to_json())

# convert the object into a dict
ai_skill_dto_dict = ai_skill_dto_instance.to_dict()
# create an instance of AiSkillDto from a dict
ai_skill_dto_from_dict = AiSkillDto.from_dict(ai_skill_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


