# KeyValuePairBooleanString

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **bool** |  | [optional] 
**value** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.key_value_pair_boolean_string import KeyValuePairBooleanString

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairBooleanString from a JSON string
key_value_pair_boolean_string_instance = KeyValuePairBooleanString.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairBooleanString.to_json())

# convert the object into a dict
key_value_pair_boolean_string_dict = key_value_pair_boolean_string_instance.to_dict()
# create an instance of KeyValuePairBooleanString from a dict
key_value_pair_boolean_string_from_dict = KeyValuePairBooleanString.from_dict(key_value_pair_boolean_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


