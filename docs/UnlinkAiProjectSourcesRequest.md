# UnlinkAiProjectSourcesRequest
Rooms to unlink from the AI project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | **List[int]** | IDs of the rooms to unlink. IDs that are not linked to the project are ignored. | 

## Example

```python
from docspace_api_sdk.models.unlink_ai_project_sources_request import UnlinkAiProjectSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnlinkAiProjectSourcesRequest from a JSON string
unlink_ai_project_sources_request_instance = UnlinkAiProjectSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(UnlinkAiProjectSourcesRequest.to_json())

# convert the object into a dict
unlink_ai_project_sources_request_dict = unlink_ai_project_sources_request_instance.to_dict()
# create an instance of UnlinkAiProjectSourcesRequest from a dict
unlink_ai_project_sources_request_from_dict = UnlinkAiProjectSourcesRequest.from_dict(unlink_ai_project_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


