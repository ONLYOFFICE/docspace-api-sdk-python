# AiAssignmentsGetAllAssignments200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | [**Dict[str, AiProfile]**](AiProfile.md) | The bound profiles keyed by action type, as `GET api/2.0/ai/profiles/list` describes them. A binding whose profile no longer exists is left out. | 
**profiles_total** | **int** | How many profiles the portal has. | 
**chat_profiles_total** | **int** | How many of those profiles can chat; a profile without declared capabilities counts as one that can. | 

## Example

```python
from docspace_api_sdk.models.ai_assignments_get_all_assignments200_response import AiAssignmentsGetAllAssignments200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiAssignmentsGetAllAssignments200Response from a JSON string
ai_assignments_get_all_assignments200_response_instance = AiAssignmentsGetAllAssignments200Response.from_json(json)
# print the JSON string representation of the object
print(AiAssignmentsGetAllAssignments200Response.to_json())

# convert the object into a dict
ai_assignments_get_all_assignments200_response_dict = ai_assignments_get_all_assignments200_response_instance.to_dict()
# create an instance of AiAssignmentsGetAllAssignments200Response from a dict
ai_assignments_get_all_assignments200_response_from_dict = AiAssignmentsGetAllAssignments200Response.from_dict(ai_assignments_get_all_assignments200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


