# ItemKeyValuePairObjectObject
One entry of a keyed collection, carried as an explicit pair of `key` and `value` fields instead of as a member  of a JSON object, so that the key is not restricted to a string and the entries keep the order they are sent in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **object** |  | [optional] 
**value** | **object** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.item_key_value_pair_object_object import ItemKeyValuePairObjectObject

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKeyValuePairObjectObject from a JSON string
item_key_value_pair_object_object_instance = ItemKeyValuePairObjectObject.from_json(json)
# print the JSON string representation of the object
print(ItemKeyValuePairObjectObject.to_json())

# convert the object into a dict
item_key_value_pair_object_object_dict = item_key_value_pair_object_object_instance.to_dict()
# create an instance of ItemKeyValuePairObjectObject from a dict
item_key_value_pair_object_object_from_dict = ItemKeyValuePairObjectObject.from_dict(item_key_value_pair_object_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


