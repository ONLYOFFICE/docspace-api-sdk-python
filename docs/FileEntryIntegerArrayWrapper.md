# FileEntryIntegerArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FileEntryDtoInteger]**](FileEntryDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.file_entry_integer_array_wrapper import FileEntryIntegerArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileEntryIntegerArrayWrapper from a JSON string
file_entry_integer_array_wrapper_instance = FileEntryIntegerArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FileEntryIntegerArrayWrapper.to_json())

# convert the object into a dict
file_entry_integer_array_wrapper_dict = file_entry_integer_array_wrapper_instance.to_dict()
# create an instance of FileEntryIntegerArrayWrapper from a dict
file_entry_integer_array_wrapper_from_dict = FileEntryIntegerArrayWrapper.from_dict(file_entry_integer_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


