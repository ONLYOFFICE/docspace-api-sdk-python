# FileUploadResultDto

File upload result dto

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Specifies if the operation is successful or not | [optional] 
**data** | **object** | Data | [optional] 
**message** | **str** | Message | [optional] 

## Example

```python
from docspace.models.file_upload_result_dto import FileUploadResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadResultDto from a JSON string
file_upload_result_dto_instance = FileUploadResultDto.from_json(json)
# print the JSON string representation of the object
print(FileUploadResultDto.to_json())

# convert the object into a dict
file_upload_result_dto_dict = file_upload_result_dto_instance.to_dict()
# create an instance of FileUploadResultDto from a dict
file_upload_result_dto_from_dict = FileUploadResultDto.from_dict(file_upload_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


