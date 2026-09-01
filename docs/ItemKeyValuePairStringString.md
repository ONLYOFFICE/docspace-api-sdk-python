# ItemKeyValuePairStringString
A key-value pair of a list item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that identifies the item within the list. | [optional] 
**value** | **str** | The value associated with the key. | [optional] 

## Example

```python
from docspace_api_sdk.models.item_key_value_pair_string_string import ItemKeyValuePairStringString

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKeyValuePairStringString from a JSON string
item_key_value_pair_string_string_instance = ItemKeyValuePairStringString.from_json(json)
# print the JSON string representation of the object
print(ItemKeyValuePairStringString.to_json())

# convert the object into a dict
item_key_value_pair_string_string_dict = item_key_value_pair_string_string_instance.to_dict()
# create an instance of ItemKeyValuePairStringString from a dict
item_key_value_pair_string_string_from_dict = ItemKeyValuePairStringString.from_dict(item_key_value_pair_string_string_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


