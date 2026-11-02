# LinkAiProjectSourcesRequest
Rooms to link to the AI project.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | **List[int]** | IDs of the Instructions and Knowledge rooms to link. Each must be an active room the caller can read; rooms already linked are skipped. | 

## Example

```python
from docspace_api_sdk.models.link_ai_project_sources_request import LinkAiProjectSourcesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LinkAiProjectSourcesRequest from a JSON string
link_ai_project_sources_request_instance = LinkAiProjectSourcesRequest.from_json(json)
# print the JSON string representation of the object
print(LinkAiProjectSourcesRequest.to_json())

# convert the object into a dict
link_ai_project_sources_request_dict = link_ai_project_sources_request_instance.to_dict()
# create an instance of LinkAiProjectSourcesRequest from a dict
link_ai_project_sources_request_from_dict = LinkAiProjectSourcesRequest.from_dict(link_ai_project_sources_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


