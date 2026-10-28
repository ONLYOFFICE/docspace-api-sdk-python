# RunBuilderScriptRequestDtoArgument
Values the script reads through the global `Argument` object, such as `Argument.title`. A JSON object without  http or https addresses.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from docspace_api_sdk.models.run_builder_script_request_dto_argument import RunBuilderScriptRequestDtoArgument

# TODO update the JSON string below
json = "{}"
# create an instance of RunBuilderScriptRequestDtoArgument from a JSON string
run_builder_script_request_dto_argument_instance = RunBuilderScriptRequestDtoArgument.from_json(json)
# print the JSON string representation of the object
print(RunBuilderScriptRequestDtoArgument.to_json())

# convert the object into a dict
run_builder_script_request_dto_argument_dict = run_builder_script_request_dto_argument_instance.to_dict()
# create an instance of RunBuilderScriptRequestDtoArgument from a dict
run_builder_script_request_dto_argument_from_dict = RunBuilderScriptRequestDtoArgument.from_dict(run_builder_script_request_dto_argument_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


