# McpServerShortWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**McpServerShortDto**](McpServerShortDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_server_short_wrapper import McpServerShortWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of McpServerShortWrapper from a JSON string
mcp_server_short_wrapper_instance = McpServerShortWrapper.from_json(json)
# print the JSON string representation of the object
print(McpServerShortWrapper.to_json())

# convert the object into a dict
mcp_server_short_wrapper_dict = mcp_server_short_wrapper_instance.to_dict()
# create an instance of McpServerShortWrapper from a dict
mcp_server_short_wrapper_from_dict = McpServerShortWrapper.from_dict(mcp_server_short_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


