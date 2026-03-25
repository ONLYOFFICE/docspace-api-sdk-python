# McpServerDto
Full MCP server configuration, including connection details and authentication headers. Returned for administrator-level operations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **UUID** | Unique identifier of the MCP server. | [optional] 
**name** | **str** | Display name of the MCP server. | [optional] 
**description** | **str** | Human-readable description of the server&#39;s purpose and capabilities. | [optional] 
**endpoint** | **str** | Base URL of the MCP server endpoint. | [optional] 
**server_type** | [**ServerType**](ServerType.md) |  | [optional] 
**headers** | **Dict[str, str]** | HTTP headers sent with every request to the server (e.g., authentication tokens). | [optional] 
**enabled** | **bool** | Indicates whether the server is currently enabled and available for room assignment. | [optional] 
**icon** | [**Icon**](Icon.md) |  | [optional] 
**need_reset** | **bool** | Indicates whether the server requires a configuration reset due to connectivity or credential issues. | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_server_dto import McpServerDto

# TODO update the JSON string below
json = "{}"
# create an instance of McpServerDto from a JSON string
mcp_server_dto_instance = McpServerDto.from_json(json)
# print the JSON string representation of the object
print(McpServerDto.to_json())

# convert the object into a dict
mcp_server_dto_dict = mcp_server_dto_instance.to_dict()
# create an instance of McpServerDto from a dict
mcp_server_dto_from_dict = McpServerDto.from_dict(mcp_server_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


