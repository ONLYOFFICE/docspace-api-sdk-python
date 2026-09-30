# UploadSessionResponseDto
How far a chunked upload has got, and the file it produced once the last byte has arrived.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The file the parts are being written into. An upload that took over a file of the same title carries it from  the start, while an upload that creates a new file has nothing to name yet and reports 0 until the answer that  sets `uploaded` to true. | [optional] 
**folder_id** | **int** | The folder receiving the file. It is the folder the upload was reserved against, or the sub-folder created for  it when the reservation declared a relative path. | [optional] 
**version** | **int** | The revision the content is being written as: 1 for a file that did not exist, the next number when the upload  took over a file of the same title, and the unchanged current number for an upload opened over an existing  file, which replaces its content in place. | [optional] 
**title** | **str** | The title the file is stored under, after characters a title cannot hold were replaced and, where a second  copy was asked for, a numeric suffix was added - so it can differ from the name that was sent. | [optional] 
**provider_key** | **str** | The third-party service holding the destination, such as `GoogleDrive` or `OneDrive`, and null for a folder  stored on the portal itself. | [optional] 
**uploaded** | **bool** | False while bytes are still missing, when the answer only reports progress; true in the answer that reports  the stored file, which is also the answer that arrives with 201. | [optional] 
**file** | [**FileDto**](FileDto.md) | The file as it stands. It is filled in both answers, but while `uploaded` is false it describes a file that  has not been written yet, so its identifier, size and links are only worth reading once that flag turns true. | [optional] 

## Example

```python
from docspace_api_sdk.models.upload_session_response_dto import UploadSessionResponseDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionResponseDto from a JSON string
upload_session_response_dto_instance = UploadSessionResponseDto.from_json(json)
# print the JSON string representation of the object
print(UploadSessionResponseDto.to_json())

# convert the object into a dict
upload_session_response_dto_dict = upload_session_response_dto_instance.to_dict()
# create an instance of UploadSessionResponseDto from a dict
upload_session_response_dto_from_dict = UploadSessionResponseDto.from_dict(upload_session_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


