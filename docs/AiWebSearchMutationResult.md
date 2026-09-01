# AiWebSearchMutationResult
Outcome of  {@link  WebSearchEngine.configure }  — either the persisted config or a field-scoped error suitable for the settings form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**config** | [**AiWebSearchConfig**](AiWebSearchConfig.md) |  | [optional] 
**error** | [**AiTErrorData**](AiTErrorData.md) |  | [optional] 

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


