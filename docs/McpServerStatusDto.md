# McpServerStatusDto
MCP server status within a room, reflecting the current user's connection state for OAuth-based servers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the MCP server. | [optional] 
**name** | **str** | Display name of the MCP server. | 
**server_type** | [**ServerType**](ServerType.md) |  | [optional] 
**connected** | **bool** | Indicates whether the current user has an active connection to this server. For direct-connection servers this is always true; for OAuth-based servers it reflects whether the user has completed authorization. | [optional] 
**icon** | [**Icon**](Icon.md) |  | [optional] 
**need_reset** | **bool** | Indicates whether the server requires a configuration reset due to connectivity or credential issues. | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_server_status_dto import McpServerStatusDto

# TODO update the JSON string below
json = "{}"
# create an instance of McpServerStatusDto from a JSON string
mcp_server_status_dto_instance = McpServerStatusDto.from_json(json)
# print the JSON string representation of the object
print(McpServerStatusDto.to_json())

# convert the object into a dict
mcp_server_status_dto_dict = mcp_server_status_dto_instance.to_dict()
# create an instance of McpServerStatusDto from a dict
mcp_server_status_dto_from_dict = McpServerStatusDto.from_dict(mcp_server_status_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


