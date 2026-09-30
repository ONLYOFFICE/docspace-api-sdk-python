# AiEditorToolsList200ResponseToolsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tool name, as it is passed back to the call endpoint. | 
**description** | **str** | What the tool does, empty when the server declares nothing. | 
**input_schema** | **Dict[str, Optional[object]]** | JSON Schema of the tool arguments. | 
**require_approval** | **bool** | Whether the editor has to ask the user before running the tool. Read-only operations arrive with this off. | 

## Example

```python
from docspace_api_sdk.models.ai_editor_tools_list200_response_tools_inner import AiEditorToolsList200ResponseToolsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiEditorToolsList200ResponseToolsInner from a JSON string
ai_editor_tools_list200_response_tools_inner_instance = AiEditorToolsList200ResponseToolsInner.from_json(json)
# print the JSON string representation of the object
print(AiEditorToolsList200ResponseToolsInner.to_json())

# convert the object into a dict
ai_editor_tools_list200_response_tools_inner_dict = ai_editor_tools_list200_response_tools_inner_instance.to_dict()
# create an instance of AiEditorToolsList200ResponseToolsInner from a dict
ai_editor_tools_list200_response_tools_inner_from_dict = AiEditorToolsList200ResponseToolsInner.from_dict(ai_editor_tools_list200_response_tools_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


