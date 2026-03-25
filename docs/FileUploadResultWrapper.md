# FileUploadResultWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileUploadResultDto**](FileUploadResultDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.file_upload_result_wrapper import FileUploadResultWrapper

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


