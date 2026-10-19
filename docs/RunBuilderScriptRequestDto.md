# RunBuilderScriptRequestDto
The document builder script to run and where to put what it produces.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**script** | **str** | The document builder script. It names a portal file by its id where the document builder documentation  writes an address - `builder.OpenFile(1234)`; an address written out in the script is refused. | 
**folder_id** | **int** | The id of the folder for the produced files that `outputs` does not list, as reported by a folder listing  such as `GET api/2.0/files/{folderId}`. | [optional] 
**outputs** | [**Dict[str, RunBuilderScriptOutputRequest]**](RunBuilderScriptOutputRequest.md) | Destinations of the produced files, keyed by the name the script saves each one under - the second argument of  `builder.SaveFile(docx, result.docx)`. | [optional] 
**argument** | [**RunBuilderScriptRequestDtoArgument**](RunBuilderScriptRequestDtoArgument.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.run_builder_script_request_dto import RunBuilderScriptRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of RunBuilderScriptRequestDto from a JSON string
run_builder_script_request_dto_instance = RunBuilderScriptRequestDto.from_json(json)
# print the JSON string representation of the object
print(RunBuilderScriptRequestDto.to_json())

# convert the object into a dict
run_builder_script_request_dto_dict = run_builder_script_request_dto_instance.to_dict()
# create an instance of RunBuilderScriptRequestDto from a dict
run_builder_script_request_dto_from_dict = RunBuilderScriptRequestDto.from_dict(run_builder_script_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


