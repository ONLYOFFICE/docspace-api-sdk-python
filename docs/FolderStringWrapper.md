# FolderStringWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FolderDtoString**](FolderDtoString.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.folder_string_wrapper import FolderStringWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderStringWrapper from a JSON string
folder_string_wrapper_instance = FolderStringWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderStringWrapper.to_json())

# convert the object into a dict
folder_string_wrapper_dict = folder_string_wrapper_instance.to_dict()
# create an instance of FolderStringWrapper from a dict
folder_string_wrapper_from_dict = FolderStringWrapper.from_dict(folder_string_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


