# EditorToolCallStateDto
The editor tool call state. Used to run the agent flow in the editor.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | The tool name. | 
**parameters** | **object** | The tool call parameters. | 

## Example

```python
from docspace_api_sdk.models.editor_tool_call_state_dto import EditorToolCallStateDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditorToolCallStateDto from a JSON string
editor_tool_call_state_dto_instance = EditorToolCallStateDto.from_json(json)
# print the JSON string representation of the object
print(EditorToolCallStateDto.to_json())

# convert the object into a dict
editor_tool_call_state_dto_dict = editor_tool_call_state_dto_instance.to_dict()
# create an instance of EditorToolCallStateDto from a dict
editor_tool_call_state_dto_from_dict = EditorToolCallStateDto.from_dict(editor_tool_call_state_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


