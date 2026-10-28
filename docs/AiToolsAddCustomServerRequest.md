# AiToolsAddCustomServerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Server name (unique within scope). | 
**config** | **object** | Server transport configuration. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_add_custom_server_request import AiToolsAddCustomServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsAddCustomServerRequest from a JSON string
ai_tools_add_custom_server_request_instance = AiToolsAddCustomServerRequest.from_json(json)
# print the JSON string representation of the object
print(AiToolsAddCustomServerRequest.to_json())

# convert the object into a dict
ai_tools_add_custom_server_request_dict = ai_tools_add_custom_server_request_instance.to_dict()
# create an instance of AiToolsAddCustomServerRequest from a dict
ai_tools_add_custom_server_request_from_dict = AiToolsAddCustomServerRequest.from_dict(ai_tools_add_custom_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


