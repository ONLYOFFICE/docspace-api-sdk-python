# KeyValuePairStringStringValues


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | **List[str]** |  | [optional] 

## Example

```python
from docspace.models.key_value_pair_string_string_values import KeyValuePairStringStringValues

# TODO update the JSON string below
json = "{}"
# create an instance of KeyValuePairStringStringValues from a JSON string
key_value_pair_string_string_values_instance = KeyValuePairStringStringValues.from_json(json)
# print the JSON string representation of the object
print(KeyValuePairStringStringValues.to_json())

# convert the object into a dict
key_value_pair_string_string_values_dict = key_value_pair_string_string_values_instance.to_dict()
# create an instance of KeyValuePairStringStringValues from a dict
key_value_pair_string_string_values_from_dict = KeyValuePairStringStringValues.from_dict(key_value_pair_string_string_values_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


