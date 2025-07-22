# STRINGArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | **List[str]** |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.string_array_wrapper import STRINGArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of STRINGArrayWrapper from a JSON string
string_array_wrapper_instance = STRINGArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(STRINGArrayWrapper.to_json())

# convert the object into a dict
string_array_wrapper_dict = string_array_wrapper_instance.to_dict()
# create an instance of STRINGArrayWrapper from a dict
string_array_wrapper_from_dict = STRINGArrayWrapper.from_dict(string_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


