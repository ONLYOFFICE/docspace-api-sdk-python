# SetRestrictedAiModelsRequestDto
The complete set of AI chat models that are to be barred on the portal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**models** | **List[str]** | The identifiers of the models no user of the portal may pick, taken from  `GET api/2.0/portal/payment/ai-prices`. This is the whole set that is to hold afterwards and not a list of  additions: send the models already barred together with the new one to add a restriction, leave one out to  lift it, and send an empty set to lift them all. | 

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


