# FolderContentIntegerWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FolderContentDtoInteger**](FolderContentDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.folder_content_integer_wrapper import FolderContentIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderContentIntegerWrapper from a JSON string
folder_content_integer_wrapper_instance = FolderContentIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderContentIntegerWrapper.to_json())

# convert the object into a dict
folder_content_integer_wrapper_dict = folder_content_integer_wrapper_instance.to_dict()
# create an instance of FolderContentIntegerWrapper from a dict
folder_content_integer_wrapper_from_dict = FolderContentIntegerWrapper.from_dict(folder_content_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


