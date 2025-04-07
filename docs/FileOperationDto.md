# FileOperationDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Operation ID | [optional] 
**operation** | [**FileOperationType**](FileOperationType.md) |  | [optional] 
**progress** | **int** | Operation progress | [optional] 
**error** | **str** | Error | [optional] 
**processed** | **str** | Processing status | [optional] 
**finished** | **bool** | Specifies if the operation is finished or not | [optional] 
**url** | **str** | URL | [optional] 
**files** | [**List[FileEntryDto]**](FileEntryDto.md) | List of files | [optional] 
**folders** | [**List[FileEntryDto]**](FileEntryDto.md) | List of folders | [optional] 

## Example

```python
from docspace.models.file_operation_dto import FileOperationDto

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


