# AiToolsReplaceAllCustomServersRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**map** | **Dict[str, object]** | Full replacement set, keyed by server name. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_replace_all_custom_servers_request import AiToolsReplaceAllCustomServersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsReplaceAllCustomServersRequest from a JSON string
ai_tools_replace_all_custom_servers_request_instance = AiToolsReplaceAllCustomServersRequest.from_json(json)
# print the JSON string representation of the object
print(AiToolsReplaceAllCustomServersRequest.to_json())

# convert the object into a dict
ai_tools_replace_all_custom_servers_request_dict = ai_tools_replace_all_custom_servers_request_instance.to_dict()
# create an instance of AiToolsReplaceAllCustomServersRequest from a dict
ai_tools_replace_all_custom_servers_request_from_dict = AiToolsReplaceAllCustomServersRequest.from_dict(ai_tools_replace_all_custom_servers_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


