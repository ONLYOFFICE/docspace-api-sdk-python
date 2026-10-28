# ItemKeyValuePairStringString
One entry of a keyed collection, carried as an explicit pair of `key` and `value` fields instead of as a member  of a JSON object, so that the key is not restricted to a string and the entries keep the order they are sent in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The left half of the pair. Where the pair configures something, this is the identifier the value belongs to -  a setting name, a module id, a logo slot; where the pair reports the result of a call, this is the result  itself, such as the flag telling whether the call succeeded. Which of the two it is, and which keys are  accepted, is stated by the operation that sends or returns the pair. | [optional] 
**value** | **str** | The right half of the pair: what is assigned to the key next to it, or what is reported for it. Its meaning  and its accepted values follow from the key, so read them from the operation that sends or returns the pair. | [optional] 

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


