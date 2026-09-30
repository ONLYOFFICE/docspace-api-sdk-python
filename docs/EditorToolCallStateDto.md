# EditorToolCallStateDto
A generation the editor is expected to run as soon as the document opens, left behind by an AI agent that created  the file but not its content.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tool_name** | **str** | Which generation to run, which also decides the shape of the parameters below. | 
**parameters** | [**EditorToolCallParametersDto**](EditorToolCallParametersDto.md) | The arguments of the generation named above. | 

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


