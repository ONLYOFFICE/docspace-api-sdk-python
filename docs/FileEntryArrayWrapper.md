# FileEntryArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FileEntryDto]**](FileEntryDto.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.file_entry_array_wrapper import FileEntryArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryArrayWrapper from a JSON string
file_entry_array_wrapper_instance = FileEntryArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FileEntryArrayWrapper.to_json())

# convert the object into a dict
file_entry_array_wrapper_dict = file_entry_array_wrapper_instance.to_dict()
# create an instance of FileEntryArrayWrapper from a dict
file_entry_array_wrapper_from_dict = FileEntryArrayWrapper.from_dict(file_entry_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


