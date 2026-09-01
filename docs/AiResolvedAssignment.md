# AiResolvedAssignment
Resolved profile for an action — both the storage row and its ID.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** |  | 
**profile** | [**AiProfile**](AiProfile.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_resolved_assignment import AiResolvedAssignment

# TODO update the JSON string below
json = "{}"
# create an instance of AiResolvedAssignment from a JSON string
ai_resolved_assignment_instance = AiResolvedAssignment.from_json(json)
# print the JSON string representation of the object
print(AiResolvedAssignment.to_json())

# convert the object into a dict
ai_resolved_assignment_dict = ai_resolved_assignment_instance.to_dict()
# create an instance of AiResolvedAssignment from a dict
ai_resolved_assignment_from_dict = AiResolvedAssignment.from_dict(ai_resolved_assignment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


