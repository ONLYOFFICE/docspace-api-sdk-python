# FileUploadResultDto
The file upload result.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the upload succeeded. This is the field to check: the operation answers 200 even when it fails, and  reports the reason in `message` instead of in the status code. | [optional] 
**data** | **object** |  | [optional] 
**message** | **str** | The reason the upload failed, ready to be shown to a person. It is empty for a successful upload, and it is  the only place where a failure is described, because the status code stays 200. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_upload_result_dto import FileUploadResultDto

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


