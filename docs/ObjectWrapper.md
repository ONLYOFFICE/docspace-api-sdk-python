# ObjectWrapper

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
from docspace-api-sdk.models.object_wrapper import ObjectWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectWrapper from a JSON string
object_wrapper_instance = ObjectWrapper.from_json(json)
# print the JSON string representation of the object
print(ObjectWrapper.to_json())

# convert the object into a dict
object_wrapper_dict = object_wrapper_instance.to_dict()
# create an instance of ObjectWrapper from a dict
object_wrapper_from_dict = ObjectWrapper.from_dict(object_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


