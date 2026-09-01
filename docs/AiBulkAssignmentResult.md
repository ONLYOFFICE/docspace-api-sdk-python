# AiBulkAssignmentResult
Outcome of  {@link  AssignmentsEngine.bulkAssign } . Either every entry persisted, or no entries persisted and a per-key error report. The engine validates first and writes second so a single bad entry never leaves the assignment table in a half-written state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**errors** | [**List[AiBulkAssignmentResultErrorsInner]**](AiBulkAssignmentResultErrorsInner.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_bulk_assignment_result import AiBulkAssignmentResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiBulkAssignmentResult from a JSON string
ai_bulk_assignment_result_instance = AiBulkAssignmentResult.from_json(json)
# print the JSON string representation of the object
print(AiBulkAssignmentResult.to_json())

# convert the object into a dict
ai_bulk_assignment_result_dict = ai_bulk_assignment_result_instance.to_dict()
# create an instance of AiBulkAssignmentResult from a dict
ai_bulk_assignment_result_from_dict = AiBulkAssignmentResult.from_dict(ai_bulk_assignment_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


