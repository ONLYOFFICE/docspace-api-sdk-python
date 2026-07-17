# SetMcpToolsRequestBody
Parameters for updating the disabled tools list of an MCP server in a room.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled_tools** | **List[str]** | List of tool names to disable. Tools not included in this list will remain enabled. Pass an empty list to enable all tools. | 

## Example

```python
from docspace_api_sdk.models.set_mcp_tools_request_body import SetMcpToolsRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of SetMcpToolsRequestBody from a JSON string
set_mcp_tools_request_body_instance = SetMcpToolsRequestBody.from_json(json)
# print the JSON string representation of the object
print(SetMcpToolsRequestBody.to_json())

# convert the object into a dict
set_mcp_tools_request_body_dict = set_mcp_tools_request_body_instance.to_dict()
# create an instance of SetMcpToolsRequestBody from a dict
set_mcp_tools_request_body_from_dict = SetMcpToolsRequestBody.from_dict(set_mcp_tools_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


