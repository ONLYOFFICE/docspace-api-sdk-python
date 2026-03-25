# KeyValuePairBooleanStringWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**KeyValuePairBooleanString**](KeyValuePairBooleanString.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.key_value_pair_boolean_string_wrapper import KeyValuePairBooleanStringWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairBooleanStringWrapper from a JSON string
key_value_pair_boolean_string_wrapper_instance = KeyValuePairBooleanStringWrapper.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairBooleanStringWrapper.to_json())

# convert the object into a dict
key_value_pair_boolean_string_wrapper_dict = key_value_pair_boolean_string_wrapper_instance.to_dict()
# create an instance of KeyValuePairBooleanStringWrapper from a dict
key_value_pair_boolean_string_wrapper_from_dict = KeyValuePairBooleanStringWrapper.from_dict(key_value_pair_boolean_string_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


