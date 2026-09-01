# AiAgentsCreateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** | Profile id bound to the agent. | 
**prompt** | **str** | Agent system prompt; stored as the room's `chatSettings.prompt`. | 
**private** | **bool** | Whether the agent room is private. | [optional] 
**share** | **List[object]** | Initial share entries (`FileShareParams`). | [optional] 
**attach_default_tools** | **bool** | Whether to attach the default DocSpace MCP tool server. | [optional] 
**title** | **str** | Agent (room) title. | [optional] 
**quota** | **float** | Room quota in bytes. | [optional] 
**indexing** | **bool** | Whether room content is indexed for search. | [optional] 
**deny_download** | **bool** | Whether downloading room content is denied. | [optional] 
**lifetime** | **object** | Room data lifetime policy (`RoomDataLifetimeDto`). | [optional] 
**watermark** | **object** | Watermark settings (`WatermarkRequestDto`). | [optional] 
**logo** | **object** | Room logo (`LogoRequest`). | [optional] 
**tags** | **List[str]** | Room tags. | [optional] 
**color** | **str** | Room accent color. | [optional] 
**cover** | **str** | Room cover image id. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_agents_create_request import AiAgentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAgentsCreateRequest from a JSON string
ai_agents_create_request_instance = AiAgentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AiAgentsCreateRequest.to_json())

# convert the object into a dict
ai_agents_create_request_dict = ai_agents_create_request_instance.to_dict()
# create an instance of AiAgentsCreateRequest from a dict
ai_agents_create_request_from_dict = AiAgentsCreateRequest.from_dict(ai_agents_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


