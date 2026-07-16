# GeneratedFileDto
Information about a file created by an AI editor generation tool.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The unique identifier of the created file. | [optional] 
**title** | **str** | The file title, including extension. | 
**extension** | **str** | The file extension. | 

## Example

```python
from docspace_api_sdk.models.generated_file_dto import GeneratedFileDto

# TODO update the JSON string below
json = "{}"
# create an instance of GeneratedFileDto from a JSON string
generated_file_dto_instance = GeneratedFileDto.from_json(json)
# print the JSON string representation of the object
print(GeneratedFileDto.to_json())

# convert the object into a dict
generated_file_dto_dict = generated_file_dto_instance.to_dict()
# create an instance of GeneratedFileDto from a dict
generated_file_dto_from_dict = GeneratedFileDto.from_dict(generated_file_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


