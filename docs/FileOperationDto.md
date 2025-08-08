# FileOperationDto
The file operation information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The file operation ID. | [optional] 
**operation** | [**FileOperationType**](FileOperationType.md) |  | [optional] 
**progress** | **int** | The file operation progress in percentage. | [optional] 
**error** | **str** | The file operation error message. | [optional] 
**processed** | **str** | The file operation processing status. | [optional] 
**finished** | **bool** | Specifies if the file operation is finished or not. | [optional] 
**url** | **str** | The file operation URL. | [optional] 
**files** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of files of the file operation. | [optional] 
**folders** | [**List[FileEntryBaseDto]**](FileEntryBaseDto.md) | The list of folders of the file operation. | [optional] 

## Example

```python
from docspace_api_sdk.models.file_operation_dto import FileOperationDto

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationDto from a JSON string
file_operation_dto_instance = FileOperationDto.from_json(json)
# print the JSON string representation of the object
print(FileOperationDto.to_json())

# convert the object into a dict
file_operation_dto_dict = file_operation_dto_instance.to_dict()
# create an instance of FileOperationDto from a dict
file_operation_dto_from_dict = FileOperationDto.from_dict(file_operation_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


