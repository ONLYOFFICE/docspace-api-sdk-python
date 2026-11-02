# AiProjectSourceDto
A room linked to an AI project as its source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | ID of the room. | 
**title** | **str** | Room title. | 
**logo** | [**LogoDto**](LogoDto.md) | Room logo. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_project_source_dto import AiProjectSourceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiProjectSourceDto from a JSON string
ai_project_source_dto_instance = AiProjectSourceDto.from_json(json)
# print the JSON string representation of the object
print(AiProjectSourceDto.to_json())

# convert the object into a dict
ai_project_source_dto_dict = ai_project_source_dto_instance.to_dict()
# create an instance of AiProjectSourceDto from a dict
ai_project_source_dto_from_dict = AiProjectSourceDto.from_dict(ai_project_source_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


