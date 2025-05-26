# ScopeResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**group** | **str** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from docspace.models.scope_response import ScopeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeResponse from a JSON string
scope_response_instance = ScopeResponse.from_json(json)
# print the JSON string representation of the object
print(ScopeResponse.to_json())

# convert the object into a dict
scope_response_dict = scope_response_instance.to_dict()
# create an instance of ScopeResponse from a dict
scope_response_from_dict = ScopeResponse.from_dict(scope_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


