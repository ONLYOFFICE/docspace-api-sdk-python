# GeneratePresentationToolCallParametersDto
The generate presentation tool call parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topic** | **str** | What the generated presentation is about. | [optional] 
**slide_count** | **str** | How many slides to generate, as the request spelled it. | [optional] 
**style** | **str** | The visual style the slides should be generated in. | [optional] 

## Example

```python
from docspace_api_sdk.models.generate_presentation_tool_call_parameters_dto import GeneratePresentationToolCallParametersDto

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratePresentationToolCallParametersDto from a JSON string
generate_presentation_tool_call_parameters_dto_instance = GeneratePresentationToolCallParametersDto.from_json(json)
# print the JSON string representation of the object
print(GeneratePresentationToolCallParametersDto.to_json())

# convert the object into a dict
generate_presentation_tool_call_parameters_dto_dict = generate_presentation_tool_call_parameters_dto_instance.to_dict()
# create an instance of GeneratePresentationToolCallParametersDto from a dict
generate_presentation_tool_call_parameters_dto_from_dict = GeneratePresentationToolCallParametersDto.from_dict(generate_presentation_tool_call_parameters_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


