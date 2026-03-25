# McpServerArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[McpServerDto]**](McpServerDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.mcp_server_array_wrapper import McpServerArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of McpServerArrayWrapper from a JSON string
mcp_server_array_wrapper_instance = McpServerArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(McpServerArrayWrapper.to_json())

# convert the object into a dict
mcp_server_array_wrapper_dict = mcp_server_array_wrapper_instance.to_dict()
# create an instance of McpServerArrayWrapper from a dict
mcp_server_array_wrapper_from_dict = McpServerArrayWrapper.from_dict(mcp_server_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


