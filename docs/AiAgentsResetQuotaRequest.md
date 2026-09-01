# AiAgentsResetQuotaRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**room_ids** | [**List[AiAgentsUpdateQuotaRequestRoomIdsInner]**](AiAgentsUpdateQuotaRequestRoomIdsInner.md) | Agent (room) ids to reset to the tenant default quota. | 

## Example

```python
from docspace_api_sdk.models.ai_agents_reset_quota_request import AiAgentsResetQuotaRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsResetQuotaRequest from a JSON string
ai_agents_reset_quota_request_instance = AiAgentsResetQuotaRequest.from_json(json)
# print the JSON string representation of the object
print(AiAgentsResetQuotaRequest.to_json())

# convert the object into a dict
ai_agents_reset_quota_request_dict = ai_agents_reset_quota_request_instance.to_dict()
# create an instance of AiAgentsResetQuotaRequest from a dict
ai_agents_reset_quota_request_from_dict = AiAgentsResetQuotaRequest.from_dict(ai_agents_reset_quota_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


