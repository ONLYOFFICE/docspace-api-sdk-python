# AiToolsSetDisabledRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server_type** | **str** |  | 
**tool_names** | **List[str]** | Tool names to disable. | 
**entity_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_set_disabled_request import AiToolsSetDisabledRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsSetDisabledRequest from a JSON string
ai_tools_set_disabled_request_instance = AiToolsSetDisabledRequest.from_json(json)
# print the JSON string representation of the object
print(AiToolsSetDisabledRequest.to_json())

# convert the object into a dict
ai_tools_set_disabled_request_dict = ai_tools_set_disabled_request_instance.to_dict()
# create an instance of AiToolsSetDisabledRequest from a dict
ai_tools_set_disabled_request_from_dict = AiToolsSetDisabledRequest.from_dict(ai_tools_set_disabled_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


