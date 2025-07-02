# FolderContentIntegerArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FolderContentDtoInteger]**](FolderContentDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.folder_content_integer_array_wrapper import FolderContentIntegerArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderContentIntegerArrayWrapper from a JSON string
folder_content_integer_array_wrapper_instance = FolderContentIntegerArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderContentIntegerArrayWrapper.to_json())

# convert the object into a dict
folder_content_integer_array_wrapper_dict = folder_content_integer_array_wrapper_instance.to_dict()
# create an instance of FolderContentIntegerArrayWrapper from a dict
folder_content_integer_array_wrapper_from_dict = FolderContentIntegerArrayWrapper.from_dict(folder_content_integer_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


