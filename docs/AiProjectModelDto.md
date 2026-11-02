# AiProjectModelDto
The AI model selected for an AI project's chat.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **UUID** | ID of the AI model profile selected for the project, as listed by `GET api/2.0/ai/profiles/list`. Null when no model has been selected for the project, or the selected profile no longer exists. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_project_model_dto import AiProjectModelDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiProjectModelDto from a JSON string
ai_project_model_dto_instance = AiProjectModelDto.from_json(json)
# print the JSON string representation of the object
print(AiProjectModelDto.to_json())

# convert the object into a dict
ai_project_model_dto_dict = ai_project_model_dto_instance.to_dict()
# create an instance of AiProjectModelDto from a dict
ai_project_model_dto_from_dict = AiProjectModelDto.from_dict(ai_project_model_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


