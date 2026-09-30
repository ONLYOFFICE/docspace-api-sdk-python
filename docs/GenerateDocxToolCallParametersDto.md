# GenerateDocxToolCallParametersDto
The generate docx tool call parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What the generated text document should contain, in the words the request was made in. | 

## Example

```python
from docspace_api_sdk.models.generate_docx_tool_call_parameters_dto import GenerateDocxToolCallParametersDto

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateDocxToolCallParametersDto from a JSON string
generate_docx_tool_call_parameters_dto_instance = GenerateDocxToolCallParametersDto.from_json(json)
# print the JSON string representation of the object
print(GenerateDocxToolCallParametersDto.to_json())

# convert the object into a dict
generate_docx_tool_call_parameters_dto_dict = generate_docx_tool_call_parameters_dto_instance.to_dict()
# create an instance of GenerateDocxToolCallParametersDto from a dict
generate_docx_tool_call_parameters_dto_from_dict = GenerateDocxToolCallParametersDto.from_dict(generate_docx_tool_call_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


