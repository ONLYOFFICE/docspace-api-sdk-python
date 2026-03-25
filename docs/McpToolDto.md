# McpToolDto
Represents a single tool exposed by an MCP server, along with its enabled or disabled state within a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the tool as reported by the MCP server. | 
**enabled** | **bool** | Indicates whether this tool is enabled (true) or disabled (false) for use in AI chat sessions within the room. | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_tool_dto import McpToolDto

# TODO update the JSON string below
json = "{}"
# create an instance of McpToolDto from a JSON string
mcp_tool_dto_instance = McpToolDto.from_json(json)
# print the JSON string representation of the object
print(McpToolDto.to_json())

# convert the object into a dict
mcp_tool_dto_dict = mcp_tool_dto_instance.to_dict()
# create an instance of McpToolDto from a dict
mcp_tool_dto_from_dict = McpToolDto.from_dict(mcp_tool_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


