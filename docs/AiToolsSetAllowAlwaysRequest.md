# AiToolsSetAllowAlwaysRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_type** | **str** |  | 
**tool_name** | **str** |  | 
**value** | **bool** | Whether the tool is always allowed. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_set_allow_always_request import AiToolsSetAllowAlwaysRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsSetAllowAlwaysRequest from a JSON string
ai_tools_set_allow_always_request_instance = AiToolsSetAllowAlwaysRequest.from_json(json)
# print the JSON string representation of the object
print(AiToolsSetAllowAlwaysRequest.to_json())

# convert the object into a dict
ai_tools_set_allow_always_request_dict = ai_tools_set_allow_always_request_instance.to_dict()
# create an instance of AiToolsSetAllowAlwaysRequest from a dict
ai_tools_set_allow_always_request_from_dict = AiToolsSetAllowAlwaysRequest.from_dict(ai_tools_set_allow_always_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


