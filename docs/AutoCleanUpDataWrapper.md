# AutoCleanUpDataWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AutoCleanUpData**](AutoCleanUpData.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-python.models.auto_clean_up_data_wrapper import AutoCleanUpDataWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AutoCleanUpDataWrapper from a JSON string
auto_clean_up_data_wrapper_instance = AutoCleanUpDataWrapper.from_json(json)
# print the JSON string representation of the object
print(AutoCleanUpDataWrapper.to_json())

# convert the object into a dict
auto_clean_up_data_wrapper_dict = auto_clean_up_data_wrapper_instance.to_dict()
# create an instance of AutoCleanUpDataWrapper from a dict
auto_clean_up_data_wrapper_from_dict = AutoCleanUpDataWrapper.from_dict(auto_clean_up_data_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


