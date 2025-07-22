# BooleanWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **bool** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.boolean_wrapper import BooleanWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanWrapper from a JSON string
boolean_wrapper_instance = BooleanWrapper.from_json(json)
# print the JSON string representation of the object
print(BooleanWrapper.to_json())

# convert the object into a dict
boolean_wrapper_dict = boolean_wrapper_instance.to_dict()
# create an instance of BooleanWrapper from a dict
boolean_wrapper_from_dict = BooleanWrapper.from_dict(boolean_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


