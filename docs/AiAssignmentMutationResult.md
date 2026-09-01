# AiAssignmentMutationResult
Outcome of `AssignmentsEngine.assign` / `AssignmentsEngine.unassign`. Either a success or a field-scoped error suitable for displaying in the profile editor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the assignment was persisted. | 
**error** | [**AiTErrorData**](AiTErrorData.md) | Why the assignment was rejected. Present on failure. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_assignment_mutation_result import AiAssignmentMutationResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiAssignmentMutationResult from a JSON string
ai_assignment_mutation_result_instance = AiAssignmentMutationResult.from_json(json)
# print the JSON string representation of the object
print(AiAssignmentMutationResult.to_json())

# convert the object into a dict
ai_assignment_mutation_result_dict = ai_assignment_mutation_result_instance.to_dict()
# create an instance of AiAssignmentMutationResult from a dict
ai_assignment_mutation_result_from_dict = AiAssignmentMutationResult.from_dict(ai_assignment_mutation_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


