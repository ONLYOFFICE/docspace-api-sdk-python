# FileUploadResultWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileUploadResultDto**](FileUploadResultDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.file_upload_result_wrapper import FileUploadResultWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileUploadResultWrapper from a JSON string
file_upload_result_wrapper_instance = FileUploadResultWrapper.from_json(json)
# print the JSON string representation of the object
print(FileUploadResultWrapper.to_json())

# convert the object into a dict
file_upload_result_wrapper_dict = file_upload_result_wrapper_instance.to_dict()
# create an instance of FileUploadResultWrapper from a dict
file_upload_result_wrapper_from_dict = FileUploadResultWrapper.from_dict(file_upload_result_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


