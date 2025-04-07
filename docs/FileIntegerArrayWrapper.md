# FileIntegerArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[FileDtoInteger]**](FileDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.file_integer_array_wrapper import FileIntegerArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of FileIntegerArrayWrapper from a JSON string
file_integer_array_wrapper_instance = FileIntegerArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(FileIntegerArrayWrapper.to_json())

# convert the object into a dict
file_integer_array_wrapper_dict = file_integer_array_wrapper_instance.to_dict()
# create an instance of FileIntegerArrayWrapper from a dict
file_integer_array_wrapper_from_dict = FileIntegerArrayWrapper.from_dict(file_integer_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


