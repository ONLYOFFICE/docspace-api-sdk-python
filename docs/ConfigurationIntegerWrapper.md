# ConfigurationIntegerWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ConfigurationDtoInteger**](ConfigurationDtoInteger.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.configuration_integer_wrapper import ConfigurationIntegerWrapper

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


