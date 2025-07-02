# FileOperationArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FileOperationDto]**](FileOperationDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.file_operation_array_wrapper import FileOperationArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationArrayWrapper from a JSON string
file_operation_array_wrapper_instance = FileOperationArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FileOperationArrayWrapper.to_json())

# convert the object into a dict
file_operation_array_wrapper_dict = file_operation_array_wrapper_instance.to_dict()
# create an instance of FileOperationArrayWrapper from a dict
file_operation_array_wrapper_from_dict = FileOperationArrayWrapper.from_dict(file_operation_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


