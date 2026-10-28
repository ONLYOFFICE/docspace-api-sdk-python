# GenerateFormToolCallParametersDto
The generate form tool call parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | What the generated fillable form should ask for, in the words the request was made in. | 

## Example

```python
from docspace_api_sdk.models.generate_form_tool_call_parameters_dto import GenerateFormToolCallParametersDto

# TODO update the JSON string below
json = "{}"
# create an instance of GenerateFormToolCallParametersDto from a JSON string
generate_form_tool_call_parameters_dto_instance = GenerateFormToolCallParametersDto.from_json(json)
# print the JSON string representation of the object
print(GenerateFormToolCallParametersDto.to_json())

# convert the object into a dict
generate_form_tool_call_parameters_dto_dict = generate_form_tool_call_parameters_dto_instance.to_dict()
# create an instance of GenerateFormToolCallParametersDto from a dict
generate_form_tool_call_parameters_dto_from_dict = GenerateFormToolCallParametersDto.from_dict(generate_form_tool_call_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


