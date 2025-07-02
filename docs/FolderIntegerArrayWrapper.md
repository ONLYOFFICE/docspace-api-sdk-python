# FolderIntegerArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FolderDtoInteger]**](FolderDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.folder_integer_array_wrapper import FolderIntegerArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderIntegerArrayWrapper from a JSON string
folder_integer_array_wrapper_instance = FolderIntegerArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderIntegerArrayWrapper.to_json())

# convert the object into a dict
folder_integer_array_wrapper_dict = folder_integer_array_wrapper_instance.to_dict()
# create an instance of FolderIntegerArrayWrapper from a dict
folder_integer_array_wrapper_from_dict = FolderIntegerArrayWrapper.from_dict(folder_integer_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


