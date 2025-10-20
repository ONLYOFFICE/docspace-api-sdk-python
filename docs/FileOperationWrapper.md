# FileOperationWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileOperationDto**](FileOperationDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_operation_wrapper import FileOperationWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationWrapper from a JSON string
file_operation_wrapper_instance = FileOperationWrapper.from_json(json)
# print the JSON string representation of the object
print(FileOperationWrapper.to_json())

# convert the object into a dict
file_operation_wrapper_dict = file_operation_wrapper_instance.to_dict()
# create an instance of FileOperationWrapper from a dict
file_operation_wrapper_from_dict = FileOperationWrapper.from_dict(file_operation_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


