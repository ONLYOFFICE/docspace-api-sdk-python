# AiAssignmentsCascadeProfileDeleteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | The profile whose assignments are removed. May be sent as the `profileId` query parameter instead of in the body. | 

## Example

```python
from docspace_api_sdk.models.ai_assignments_cascade_profile_delete_request import AiAssignmentsCascadeProfileDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAssignmentsCascadeProfileDeleteRequest from a JSON string
ai_assignments_cascade_profile_delete_request_instance = AiAssignmentsCascadeProfileDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(AiAssignmentsCascadeProfileDeleteRequest.to_json())

# convert the object into a dict
ai_assignments_cascade_profile_delete_request_dict = ai_assignments_cascade_profile_delete_request_instance.to_dict()
# create an instance of AiAssignmentsCascadeProfileDeleteRequest from a dict
ai_assignments_cascade_profile_delete_request_from_dict = AiAssignmentsCascadeProfileDeleteRequest.from_dict(ai_assignments_cascade_profile_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


