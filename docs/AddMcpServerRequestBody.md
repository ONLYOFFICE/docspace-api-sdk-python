# AddMcpServerRequestBody
Parameters for creating a new custom MCP server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Unique display name for the server. Only letters, numbers, underscores, and hyphens are allowed. Maximum 128 characters. | 
**description** | **str** | Human-readable description of the server's purpose and capabilities. Maximum 255 characters. | 
**endpoint** | **str** | Base URL of the MCP server endpoint. Must be a valid, reachable URL. The system will verify connectivity during registration. | 
**headers** | **Dict[str, str]** | Optional HTTP headers to include with every request to the MCP server (e.g., authentication tokens or API keys). | [optional] 
**icon** | **str** | Optional Base64-encoded icon image for the server. Used as the visual identifier in the UI. | [optional] 

## Example

```python
from docspace_api_sdk.models.add_mcp_server_request_body import AddMcpServerRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of AddMcpServerRequestBody from a JSON string
add_mcp_server_request_body_instance = AddMcpServerRequestBody.from_json(json)
# print the JSON string representation of the object
print(AddMcpServerRequestBody.to_json())

# convert the object into a dict
add_mcp_server_request_body_dict = add_mcp_server_request_body_instance.to_dict()
# create an instance of AddMcpServerRequestBody from a dict
add_mcp_server_request_body_from_dict = AddMcpServerRequestBody.from_dict(add_mcp_server_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


