# UploadResultDto
The upload result parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Specifies if the upload operation is successful or not. | [optional] 
**data** | **object** | The uploaded data. | [optional] 
**message** | **str** | The message sent after the successful upload operation. | [optional] 

## Example

```python
from docspace_api_sdk.models.upload_result_dto import UploadResultDto

# TODO update the JSON string below
json = "{}"
# create an instance of UploadResultDto from a JSON string
upload_result_dto_instance = UploadResultDto.from_json(json)
# print the JSON string representation of the object
print(UploadResultDto.to_json())

# convert the object into a dict
upload_result_dto_dict = upload_result_dto_instance.to_dict()
# create an instance of UploadResultDto from a dict
upload_result_dto_from_dict = UploadResultDto.from_dict(upload_result_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


