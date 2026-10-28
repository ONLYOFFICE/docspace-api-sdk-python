# AiAgentsUpdateQuotaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | [**List[AiAgentsUpdateQuotaRequestRoomIdsInner]**](AiAgentsUpdateQuotaRequestRoomIdsInner.md) | Agent (room) ids to update. | 
**quota** | **float** | New quota in bytes; a negative value disables the custom quota. | 

## Example

```python
from docspace_api_sdk.models.ai_agents_update_quota_request import AiAgentsUpdateQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsUpdateQuotaRequest from a JSON string
ai_agents_update_quota_request_instance = AiAgentsUpdateQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(AiAgentsUpdateQuotaRequest.to_json())

# convert the object into a dict
ai_agents_update_quota_request_dict = ai_agents_update_quota_request_instance.to_dict()
# create an instance of AiAgentsUpdateQuotaRequest from a dict
ai_agents_update_quota_request_from_dict = AiAgentsUpdateQuotaRequest.from_dict(ai_agents_update_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


