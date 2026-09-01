# AiProfileMutationResult
Outcome of `create` / `update` — either a success carrying the persisted profile, or a failure with a field-level error description from the name check or the provider credential check.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the profile was persisted. | 
**profile** | [**AiProfile**](AiProfile.md) | The persisted profile. Present on success. | [optional] 
**error** | [**AiTErrorData**](AiTErrorData.md) | Why the profile was rejected - the name check or the provider credential check. Present on failure. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_profile_mutation_result import AiProfileMutationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiProfileMutationResult from a JSON string
ai_profile_mutation_result_instance = AiProfileMutationResult.from_json(json)
# print the JSON string representation of the object
print(AiProfileMutationResult.to_json())

# convert the object into a dict
ai_profile_mutation_result_dict = ai_profile_mutation_result_instance.to_dict()
# create an instance of AiProfileMutationResult from a dict
ai_profile_mutation_result_from_dict = AiProfileMutationResult.from_dict(ai_profile_mutation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


