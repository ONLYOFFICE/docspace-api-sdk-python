# SetRestrictedAiModelsRequestDto
The request parameters for setting restricted AI models.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** | The set of restricted AI model IDs. | 

## Example

```python
from docspace_api_sdk.models.set_restricted_ai_models_request_dto import SetRestrictedAiModelsRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of SetRestrictedAiModelsRequestDto from a JSON string
set_restricted_ai_models_request_dto_instance = SetRestrictedAiModelsRequestDto.from_json(json)
# print the JSON string representation of the object
print(SetRestrictedAiModelsRequestDto.to_json())

# convert the object into a dict
set_restricted_ai_models_request_dto_dict = set_restricted_ai_models_request_dto_instance.to_dict()
# create an instance of SetRestrictedAiModelsRequestDto from a dict
set_restricted_ai_models_request_dto_from_dict = SetRestrictedAiModelsRequestDto.from_dict(set_restricted_ai_models_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


