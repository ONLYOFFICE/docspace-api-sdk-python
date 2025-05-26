# UnknownWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **object** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.unknown_wrapper import UnknownWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of UnknownWrapper from a JSON string
unknown_wrapper_instance = UnknownWrapper.from_json(json)
# print the JSON string representation of the object
print(UnknownWrapper.to_json())

# convert the object into a dict
unknown_wrapper_dict = unknown_wrapper_instance.to_dict()
# create an instance of UnknownWrapper from a dict
unknown_wrapper_from_dict = UnknownWrapper.from_dict(unknown_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


