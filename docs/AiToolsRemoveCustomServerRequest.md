# AiToolsRemoveCustomServerRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_remove_custom_server_request import AiToolsRemoveCustomServerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsRemoveCustomServerRequest from a JSON string
ai_tools_remove_custom_server_request_instance = AiToolsRemoveCustomServerRequest.from_json(json)
# print the JSON string representation of the object
print(AiToolsRemoveCustomServerRequest.to_json())

# convert the object into a dict
ai_tools_remove_custom_server_request_dict = ai_tools_remove_custom_server_request_instance.to_dict()
# create an instance of AiToolsRemoveCustomServerRequest from a dict
ai_tools_remove_custom_server_request_from_dict = AiToolsRemoveCustomServerRequest.from_dict(ai_tools_remove_custom_server_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


