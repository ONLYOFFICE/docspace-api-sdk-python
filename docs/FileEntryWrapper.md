# FileEntryWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**FileEntryDto**](FileEntryDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.file_entry_wrapper import FileEntryWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryWrapper from a JSON string
file_entry_wrapper_instance = FileEntryWrapper.from_json(json)
# print the JSON string representation of the object
print(FileEntryWrapper.to_json())

# convert the object into a dict
file_entry_wrapper_dict = file_entry_wrapper_instance.to_dict()
# create an instance of FileEntryWrapper from a dict
file_entry_wrapper_from_dict = FileEntryWrapper.from_dict(file_entry_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


