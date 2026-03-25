# McpToolArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[McpToolDto]**](McpToolDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_tool_array_wrapper import McpToolArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of McpToolArrayWrapper from a JSON string
mcp_tool_array_wrapper_instance = McpToolArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(McpToolArrayWrapper.to_json())

# convert the object into a dict
mcp_tool_array_wrapper_dict = mcp_tool_array_wrapper_instance.to_dict()
# create an instance of McpToolArrayWrapper from a dict
mcp_tool_array_wrapper_from_dict = McpToolArrayWrapper.from_dict(mcp_tool_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


