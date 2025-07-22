# AceShortWrapperArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[AceShortWrapper]**](AceShortWrapper.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.ace_short_wrapper_array_wrapper import AceShortWrapperArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AceShortWrapperArrayWrapper from a JSON string
ace_short_wrapper_array_wrapper_instance = AceShortWrapperArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(AceShortWrapperArrayWrapper.to_json())

# convert the object into a dict
ace_short_wrapper_array_wrapper_dict = ace_short_wrapper_array_wrapper_instance.to_dict()
# create an instance of AceShortWrapperArrayWrapper from a dict
ace_short_wrapper_array_wrapper_from_dict = AceShortWrapperArrayWrapper.from_dict(ace_short_wrapper_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


