# StringWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **str** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.string_wrapper import StringWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of StringWrapper from a JSON string
string_wrapper_instance = StringWrapper.from_json(json)
# print the JSON string representation of the object
print(StringWrapper.to_json())

# convert the object into a dict
string_wrapper_dict = string_wrapper_instance.to_dict()
# create an instance of StringWrapper from a dict
string_wrapper_from_dict = StringWrapper.from_dict(string_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


