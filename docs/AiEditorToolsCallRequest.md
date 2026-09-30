# AiEditorToolsCallRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the tool to run, as listed by the tools endpoint. A name that is unknown or excluded from the editor is rejected with 400. | 
**arguments** | **Dict[str, Optional[object]]** | Arguments for the tool, shaped by that tool's own input schema. Treated as empty when it is not an object. | [optional] 
**entity_id** | **str** | Room the call is scoped to. Left out for a portal-wide call. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_editor_tools_call_request import AiEditorToolsCallRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiEditorToolsCallRequest from a JSON string
ai_editor_tools_call_request_instance = AiEditorToolsCallRequest.from_json(json)
# print the JSON string representation of the object
print(AiEditorToolsCallRequest.to_json())

# convert the object into a dict
ai_editor_tools_call_request_dict = ai_editor_tools_call_request_instance.to_dict()
# create an instance of AiEditorToolsCallRequest from a dict
ai_editor_tools_call_request_from_dict = AiEditorToolsCallRequest.from_dict(ai_editor_tools_call_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


