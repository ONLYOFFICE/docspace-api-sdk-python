# AiToolsUpdateCustomServerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**config** | **object** | One MCP server configuration. The shape is intentionally open — MCP allows per-transport fields (`command`/`args` for stdio, `url` for HTTP, plus env, headers, etc.) and the storage layer stays agnostic to which transport is in use. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_update_custom_server_request import AiToolsUpdateCustomServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsUpdateCustomServerRequest from a JSON string
ai_tools_update_custom_server_request_instance = AiToolsUpdateCustomServerRequest.from_json(json)
# print the JSON string representation of the object
print(AiToolsUpdateCustomServerRequest.to_json())

# convert the object into a dict
ai_tools_update_custom_server_request_dict = ai_tools_update_custom_server_request_instance.to_dict()
# create an instance of AiToolsUpdateCustomServerRequest from a dict
ai_tools_update_custom_server_request_from_dict = AiToolsUpdateCustomServerRequest.from_dict(ai_tools_update_custom_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


