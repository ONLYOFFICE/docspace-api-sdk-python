# AiAssignmentsAssignRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**AiActionType**](AiActionType.md) | Action the assignment applies to. | 
**profile_id** | **str** | Profile id to bind. | 

## Example

```python
from docspace_api_sdk.models.ai_assignments_assign_request import AiAssignmentsAssignRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAssignmentsAssignRequest from a JSON string
ai_assignments_assign_request_instance = AiAssignmentsAssignRequest.from_json(json)
# print the JSON string representation of the object
print(AiAssignmentsAssignRequest.to_json())

# convert the object into a dict
ai_assignments_assign_request_dict = ai_assignments_assign_request_instance.to_dict()
# create an instance of AiAssignmentsAssignRequest from a dict
ai_assignments_assign_request_from_dict = AiAssignmentsAssignRequest.from_dict(ai_assignments_assign_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


