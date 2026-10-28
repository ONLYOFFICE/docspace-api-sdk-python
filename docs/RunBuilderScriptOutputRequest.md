# RunBuilderScriptOutputRequest
Where one produced file goes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file_id** | **int** | The id of a portal file to store the result in as a new version, as reported by a folder listing such as  `GET api/2.0/files/{folderId}`. | [optional] 
**folder_id** | **int** | The id of a folder to save the result in as a new file, as reported by a folder listing such as  `GET api/2.0/files/{folderId}`. | [optional] 
**title** | **str** | The title of the new file, when it has to differ from the name the script saved the result under. | [optional] 

## Example

```python
from docspace_api_sdk.models.run_builder_script_output_request import RunBuilderScriptOutputRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RunBuilderScriptOutputRequest from a JSON string
run_builder_script_output_request_instance = RunBuilderScriptOutputRequest.from_json(json)
# print the JSON string representation of the object
print(RunBuilderScriptOutputRequest.to_json())

# convert the object into a dict
run_builder_script_output_request_dict = run_builder_script_output_request_instance.to_dict()
# create an instance of RunBuilderScriptOutputRequest from a dict
run_builder_script_output_request_from_dict = RunBuilderScriptOutputRequest.from_dict(run_builder_script_output_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


