# FileOperationRequestBaseDto
The base operation request parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**return_single_operation** | **bool** | Specifies whether to return only the current operation | [optional] 

## Example

```python
from docspace_api_sdk.models.file_operation_request_base_dto import FileOperationRequestBaseDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationRequestBaseDto from a JSON string
file_operation_request_base_dto_instance = FileOperationRequestBaseDto.from_json(json)
# print the JSON string representation of the object
print(FileOperationRequestBaseDto.to_json())

# convert the object into a dict
file_operation_request_base_dto_dict = file_operation_request_base_dto_instance.to_dict()
# create an instance of FileOperationRequestBaseDto from a dict
file_operation_request_base_dto_from_dict = FileOperationRequestBaseDto.from_dict(file_operation_request_base_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


