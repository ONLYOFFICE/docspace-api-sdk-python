# ItemKeyValuePairBooleanString
A key-value pair of a list item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **bool** | The key that identifies the item within the list. | [optional] 
**value** | **str** | The value associated with the key. | [optional] 

## Example

```python
from docspace_api_sdk.models.item_key_value_pair_boolean_string import ItemKeyValuePairBooleanString

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKeyValuePairBooleanString from a JSON string
item_key_value_pair_boolean_string_instance = ItemKeyValuePairBooleanString.from_json(json)
# print the JSON string representation of the object
print(ItemKeyValuePairBooleanString.to_json())

# convert the object into a dict
item_key_value_pair_boolean_string_dict = item_key_value_pair_boolean_string_instance.to_dict()
# create an instance of ItemKeyValuePairBooleanString from a dict
item_key_value_pair_boolean_string_from_dict = ItemKeyValuePairBooleanString.from_dict(item_key_value_pair_boolean_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


