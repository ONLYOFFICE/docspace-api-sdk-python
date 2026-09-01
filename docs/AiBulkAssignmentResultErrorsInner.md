# AiBulkAssignmentResultErrorsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**AiActionType**](AiActionType.md) |  | 
**error** | [**AiTErrorData**](AiTErrorData.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_bulk_assignment_result_errors_inner import AiBulkAssignmentResultErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiBulkAssignmentResultErrorsInner from a JSON string
ai_bulk_assignment_result_errors_inner_instance = AiBulkAssignmentResultErrorsInner.from_json(json)
# print the JSON string representation of the object
print(AiBulkAssignmentResultErrorsInner.to_json())

# convert the object into a dict
ai_bulk_assignment_result_errors_inner_dict = ai_bulk_assignment_result_errors_inner_instance.to_dict()
# create an instance of AiBulkAssignmentResultErrorsInner from a dict
ai_bulk_assignment_result_errors_inner_from_dict = AiBulkAssignmentResultErrorsInner.from_dict(ai_bulk_assignment_result_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


