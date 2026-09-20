# UploadResultDto
The outcome of storing an image in temporary storage before it is used as a room logo.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the image was stored and its path is in the data field. A rejected image is reported with an error  response rather than with a false here, so this field is true in every answer that carries a body. | [optional] 
**data** | **object** |  | [optional] 
**message** | **str** | Left empty by this operation: nothing is reported here, and a refused image comes back as an error response  instead. | [optional] 

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


