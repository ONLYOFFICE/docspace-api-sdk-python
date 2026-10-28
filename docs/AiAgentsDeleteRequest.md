# AiAgentsDeleteRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delete_after** | **bool** | Delete the room after the editing session finishes. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_agents_delete_request import AiAgentsDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsDeleteRequest from a JSON string
ai_agents_delete_request_instance = AiAgentsDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(AiAgentsDeleteRequest.to_json())

# convert the object into a dict
ai_agents_delete_request_dict = ai_agents_delete_request_instance.to_dict()
# create an instance of AiAgentsDeleteRequest from a dict
ai_agents_delete_request_from_dict = AiAgentsDeleteRequest.from_dict(ai_agents_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


