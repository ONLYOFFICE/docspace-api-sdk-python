# McpServerShortDto
Compact MCP server summary without sensitive details like endpoint URL or authentication headers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the MCP server. | [optional] 
**name** | **str** | Display name of the MCP server. | [optional] 
**server_type** | [**ServerType**](ServerType.md) |  | [optional] 
**enabled** | **bool** | Indicates whether the server is currently enabled and available for room assignment. | [optional] 
**icon** | [**Icon**](Icon.md) |  | [optional] 
**need_reset** | **bool** | Indicates whether the server requires a configuration reset due to connectivity or credential issues. | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_server_short_dto import McpServerShortDto

# TODO update the JSON string below
json = "{}"
# create an instance of McpServerShortDto from a JSON string
mcp_server_short_dto_instance = McpServerShortDto.from_json(json)
# print the JSON string representation of the object
print(McpServerShortDto.to_json())

# convert the object into a dict
mcp_server_short_dto_dict = mcp_server_short_dto_instance.to_dict()
# create an instance of McpServerShortDto from a dict
mcp_server_short_dto_from_dict = McpServerShortDto.from_dict(mcp_server_short_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


