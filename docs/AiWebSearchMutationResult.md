# AiWebSearchMutationResult
Outcome of `WebSearchEngine.configure` — either the persisted config or a field-scoped error suitable for the settings form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the configuration was persisted. | 
**config** | [**AiWebSearchConfig**](AiWebSearchConfig.md) | The persisted web-search configuration. Present on success. | [optional] 
**error** | [**AiTErrorData**](AiTErrorData.md) | Why the configuration was rejected. Present on failure. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_web_search_mutation_result import AiWebSearchMutationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiWebSearchMutationResult from a JSON string
ai_web_search_mutation_result_instance = AiWebSearchMutationResult.from_json(json)
# print the JSON string representation of the object
print(AiWebSearchMutationResult.to_json())

# convert the object into a dict
ai_web_search_mutation_result_dict = ai_web_search_mutation_result_instance.to_dict()
# create an instance of AiWebSearchMutationResult from a dict
ai_web_search_mutation_result_from_dict = AiWebSearchMutationResult.from_dict(ai_web_search_mutation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


