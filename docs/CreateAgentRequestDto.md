# CreateAgentRequestDto
Request to create a new AI agent room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | The room name. | 
**quota** | **int** | The room quota. | [optional] 
**indexing** | **bool** | Specifies whether to create a room with indexing. | [optional] 
**deny_download** | **bool** | Specifies whether to deny downloads from the room. | [optional] 
**lifetime** | [**RoomDataLifetimeDto**](RoomDataLifetimeDto.md) |  | [optional] 
**watermark** | [**WatermarkRequestDto**](WatermarkRequestDto.md) |  | [optional] 
**logo** | [**LogoRequest**](LogoRequest.md) |  | [optional] 
**tags** | **List[str]** | The list of tags. | [optional] 
**color** | **str** | The room color. | [optional] 
**cover** | **str** | The room cover. | [optional] 
**private** | **bool** | Specifies whether the room to be created is private or not. | [optional] 
**share** | [**List[FileShareParams]**](FileShareParams.md) | The collection of sharing parameters. | [optional] 
**chat_settings** | [**ChatSettings**](ChatSettings.md) |  | 
**attach_default_tools** | **bool** | Specifies whether to attach default tools to the agent or not. | [optional] 

## Example

```python
from docspace_api_sdk.models.create_agent_request_dto import CreateAgentRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAgentRequestDto from a JSON string
create_agent_request_dto_instance = CreateAgentRequestDto.from_json(json)
# print the JSON string representation of the object
print(CreateAgentRequestDto.to_json())

# convert the object into a dict
create_agent_request_dto_dict = create_agent_request_dto_instance.to_dict()
# create an instance of CreateAgentRequestDto from a dict
create_agent_request_dto_from_dict = CreateAgentRequestDto.from_dict(create_agent_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


