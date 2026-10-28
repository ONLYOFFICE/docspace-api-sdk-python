# RestrictedAiModelsDto
The AI models the portal is not allowed to use.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** | The identifiers of the models the portal is not allowed to use. | 

## Example

```python
from docspace_api_sdk.models.restricted_ai_models_dto import RestrictedAiModelsDto

# TODO update the JSON string below
json = "{}"
# create an instance of RestrictedAiModelsDto from a JSON string
restricted_ai_models_dto_instance = RestrictedAiModelsDto.from_json(json)
# print the JSON string representation of the object
print(RestrictedAiModelsDto.to_json())

# convert the object into a dict
restricted_ai_models_dto_dict = restricted_ai_models_dto_instance.to_dict()
# create an instance of RestrictedAiModelsDto from a dict
restricted_ai_models_dto_from_dict = RestrictedAiModelsDto.from_dict(restricted_ai_models_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


