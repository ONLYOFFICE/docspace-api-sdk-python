# ArrayArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **List[List[str]]** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.array_array_wrapper import ArrayArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ArrayArrayWrapper from a JSON string
array_array_wrapper_instance = ArrayArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ArrayArrayWrapper.to_json())

# convert the object into a dict
array_array_wrapper_dict = array_array_wrapper_instance.to_dict()
# create an instance of ArrayArrayWrapper from a dict
array_array_wrapper_from_dict = ArrayArrayWrapper.from_dict(array_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


