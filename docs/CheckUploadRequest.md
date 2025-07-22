# CheckUploadRequest
The request parameters for checking file uploads.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**files_title** | **List[str]** | The list of file titles. | [optional] 

## Example

```python
from docspace-api-sdk.models.check_upload_request import CheckUploadRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CheckUploadRequest from a JSON string
check_upload_request_instance = CheckUploadRequest.from_json(json)
# print the JSON string representation of the object
print(CheckUploadRequest.to_json())

# convert the object into a dict
check_upload_request_dict = check_upload_request_instance.to_dict()
# create an instance of CheckUploadRequest from a dict
check_upload_request_from_dict = CheckUploadRequest.from_dict(check_upload_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


