# UploadRequestDto
The request parameters for uploading a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**file** | **bytearray** | The file to be uploaded. | [optional] 
**content_type** | [**ContentType**](ContentType.md) |  | [optional] 
**content_disposition** | [**ContentDisposition**](ContentDisposition.md) |  | [optional] 
**files** | **List[bytearray]** | The list of files when specified as multipart/form-data. | [optional] 
**create_new_if_exist** | **bool** | Specifies whether to create the new file if it already exists or not. | [optional] 
**store_original_file_flag** | **bool** | Specifies whether to upload documents in the original formats as well or not. | [optional] 
**keep_convert_status** | **bool** | Specifies whether to keep the file converting status or not. | [optional] 
**stream** | **bytearray** | The request input stream. | [optional] 

## Example

```python
from docspace-api-python.models.upload_request_dto import UploadRequestDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadRequestDto from a JSON string
upload_request_dto_instance = UploadRequestDto.from_json(json)
# print the JSON string representation of the object
print(UploadRequestDto.to_json())

# convert the object into a dict
upload_request_dto_dict = upload_request_dto_instance.to_dict()
# create an instance of UploadRequestDto from a dict
upload_request_dto_from_dict = UploadRequestDto.from_dict(upload_request_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


