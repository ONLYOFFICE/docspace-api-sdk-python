# AiProjectSourcesDto
The sources of an AI project: the Instructions and Knowledge rooms linked to it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instructions_rooms** | [**List[AiProjectSourceDto]**](AiProjectSourceDto.md) | Linked Instructions rooms, sorted by title. | 
**knowledge_rooms** | [**List[AiProjectSourceDto]**](AiProjectSourceDto.md) | Linked Knowledge rooms, sorted by title. | 

## Example

```python
from docspace_api_sdk.models.ai_project_sources_dto import AiProjectSourcesDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiProjectSourcesDto from a JSON string
ai_project_sources_dto_instance = AiProjectSourcesDto.from_json(json)
# print the JSON string representation of the object
print(AiProjectSourcesDto.to_json())

# convert the object into a dict
ai_project_sources_dto_dict = ai_project_sources_dto_instance.to_dict()
# create an instance of AiProjectSourcesDto from a dict
ai_project_sources_dto_from_dict = AiProjectSourcesDto.from_dict(ai_project_sources_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


