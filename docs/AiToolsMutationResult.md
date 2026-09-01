# AiToolsMutationResult
Outcome of an MCP-server CRUD call. Either success or a field-scoped error suitable for the settings form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the MCP server was persisted. | 
**error** | [**AiTErrorData**](AiTErrorData.md) | Why the MCP server was rejected. Present on failure. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_mutation_result import AiToolsMutationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsMutationResult from a JSON string
ai_tools_mutation_result_instance = AiToolsMutationResult.from_json(json)
# print the JSON string representation of the object
print(AiToolsMutationResult.to_json())

# convert the object into a dict
ai_tools_mutation_result_dict = ai_tools_mutation_result_instance.to_dict()
# create an instance of AiToolsMutationResult from a dict
ai_tools_mutation_result_from_dict = AiToolsMutationResult.from_dict(ai_tools_mutation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


