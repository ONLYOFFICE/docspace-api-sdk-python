# FolderIntegerWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FolderDtoInteger**](FolderDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.folder_integer_wrapper import FolderIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FolderIntegerWrapper from a JSON string
folder_integer_wrapper_instance = FolderIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(FolderIntegerWrapper.to_json())

# convert the object into a dict
folder_integer_wrapper_dict = folder_integer_wrapper_instance.to_dict()
# create an instance of FolderIntegerWrapper from a dict
folder_integer_wrapper_from_dict = FolderIntegerWrapper.from_dict(folder_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


