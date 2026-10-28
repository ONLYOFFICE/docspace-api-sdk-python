# ItemKeyValuePairBooleanStringWrapper
The successful API response containing the ItemKeyValuePairBooleanString object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**ItemKeyValuePairBooleanString**](ItemKeyValuePairBooleanString.md) | The ItemKeyValuePairBooleanString object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.item_key_value_pair_boolean_string_wrapper import ItemKeyValuePairBooleanStringWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKeyValuePairBooleanStringWrapper from a JSON string
item_key_value_pair_boolean_string_wrapper_instance = ItemKeyValuePairBooleanStringWrapper.from_json(json)
# print the JSON string representation of the object
print(ItemKeyValuePairBooleanStringWrapper.to_json())

# convert the object into a dict
item_key_value_pair_boolean_string_wrapper_dict = item_key_value_pair_boolean_string_wrapper_instance.to_dict()
# create an instance of ItemKeyValuePairBooleanStringWrapper from a dict
item_key_value_pair_boolean_string_wrapper_from_dict = ItemKeyValuePairBooleanStringWrapper.from_dict(item_key_value_pair_boolean_string_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


