# DoubleWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **float** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.double_wrapper import DoubleWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of DoubleWrapper from a JSON string
double_wrapper_instance = DoubleWrapper.from_json(json)
# print the JSON string representation of the object
print(DoubleWrapper.to_json())

# convert the object into a dict
double_wrapper_dict = double_wrapper_instance.to_dict()
# create an instance of DoubleWrapper from a dict
double_wrapper_from_dict = DoubleWrapper.from_dict(double_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


