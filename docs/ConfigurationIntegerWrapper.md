# ConfigurationIntegerWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ConfigurationDtoInteger**](ConfigurationDtoInteger.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.configuration_integer_wrapper import ConfigurationIntegerWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationIntegerWrapper from a JSON string
configuration_integer_wrapper_instance = ConfigurationIntegerWrapper.from_json(json)
# print the JSON string representation of the object
print(ConfigurationIntegerWrapper.to_json())

# convert the object into a dict
configuration_integer_wrapper_dict = configuration_integer_wrapper_instance.to_dict()
# create an instance of ConfigurationIntegerWrapper from a dict
configuration_integer_wrapper_from_dict = ConfigurationIntegerWrapper.from_dict(configuration_integer_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


