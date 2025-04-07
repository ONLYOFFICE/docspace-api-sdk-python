# ModuleArrayWrapper


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[Module]**](Module.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace.models.module_array_wrapper import ModuleArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ModuleArrayWrapper from a JSON string
module_array_wrapper_instance = ModuleArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(ModuleArrayWrapper.to_json())

# convert the object into a dict
module_array_wrapper_dict = module_array_wrapper_instance.to_dict()
# create an instance of ModuleArrayWrapper from a dict
module_array_wrapper_from_dict = ModuleArrayWrapper.from_dict(module_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


