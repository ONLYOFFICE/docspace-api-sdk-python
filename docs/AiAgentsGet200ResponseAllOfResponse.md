# AiAgentsGet200ResponseAllOfResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | The AI profile bound to this agent, added by this service on top of what the internal service returns. Absent when the agent has no profile assigned. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_agents_get200_response_all_of_response import AiAgentsGet200ResponseAllOfResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsGet200ResponseAllOfResponse from a JSON string
ai_agents_get200_response_all_of_response_instance = AiAgentsGet200ResponseAllOfResponse.from_json(json)
# print the JSON string representation of the object
print(AiAgentsGet200ResponseAllOfResponse.to_json())

# convert the object into a dict
ai_agents_get200_response_all_of_response_dict = ai_agents_get200_response_all_of_response_instance.to_dict()
# create an instance of AiAgentsGet200ResponseAllOfResponse from a dict
ai_agents_get200_response_all_of_response_from_dict = AiAgentsGet200ResponseAllOfResponse.from_dict(ai_agents_get200_response_all_of_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


