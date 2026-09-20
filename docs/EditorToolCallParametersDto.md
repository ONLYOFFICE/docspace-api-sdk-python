# EditorToolCallParametersDto
The editor tool call parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What the generated fillable form should ask for, in the words the request was made in. | 
**topic** | **str** | What the generated presentation is about. | [optional] 
**slide_count** | **str** | How many slides to generate, as the request spelled it. | [optional] 
**style** | **str** | The visual style the slides should be generated in. | [optional] 

## Example

```python
from docspace_api_sdk.models.editor_tool_call_parameters_dto import EditorToolCallParametersDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditorToolCallParametersDto from a JSON string
editor_tool_call_parameters_dto_instance = EditorToolCallParametersDto.from_json(json)
# print the JSON string representation of the object
print(EditorToolCallParametersDto.to_json())

# convert the object into a dict
editor_tool_call_parameters_dto_dict = editor_tool_call_parameters_dto_instance.to_dict()
# create an instance of EditorToolCallParametersDto from a dict
editor_tool_call_parameters_dto_from_dict = EditorToolCallParametersDto.from_dict(editor_tool_call_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


