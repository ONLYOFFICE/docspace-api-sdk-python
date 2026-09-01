# UploadSessionResponseDtoInteger
The upload session response parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The upload session ID. | [optional] 
**folder_id** | **int** | The folder ID where the file is being uploaded. | [optional] 
**version** | **int** | The file version number. | [optional] 
**title** | **str** | The file title. | [optional] 
**provider_key** | **str** | The third-party provider key. | [optional] 
**uploaded** | **bool** | Specifies whether the file has been uploaded. | [optional] 
**file** | [**FileDtoInteger**](FileDtoInteger.md) | The file parameters. | [optional] 

## Example

```python
from docspace_api_sdk.models.upload_session_response_dto_integer import UploadSessionResponseDtoInteger

# TODO update the JSON string below
json = "{}"
# create an instance of UploadSessionResponseDtoInteger from a JSON string
upload_session_response_dto_integer_instance = UploadSessionResponseDtoInteger.from_json(json)
# print the JSON string representation of the object
print(UploadSessionResponseDtoInteger.to_json())

# convert the object into a dict
upload_session_response_dto_integer_dict = upload_session_response_dto_integer_instance.to_dict()
# create an instance of UploadSessionResponseDtoInteger from a dict
upload_session_response_dto_integer_from_dict = UploadSessionResponseDtoInteger.from_dict(upload_session_response_dto_integer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


