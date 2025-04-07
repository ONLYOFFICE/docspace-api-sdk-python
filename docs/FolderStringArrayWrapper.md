# FolderStringArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FolderDtoString]**](FolderDtoString.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.folder_string_array_wrapper import FolderStringArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderStringArrayWrapper from a JSON string
folder_string_array_wrapper_instance = FolderStringArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderStringArrayWrapper.to_json())

# convert the object into a dict
folder_string_array_wrapper_dict = folder_string_array_wrapper_instance.to_dict()
# create an instance of FolderStringArrayWrapper from a dict
folder_string_array_wrapper_from_dict = FolderStringArrayWrapper.from_dict(folder_string_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


