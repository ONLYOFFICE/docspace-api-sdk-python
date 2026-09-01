# ItemKeyValuePairStringLogoRequestsDto
A key-value pair of a list item.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key that identifies the item within the list. | [optional] 
**value** | [**LogoRequestsDto**](LogoRequestsDto.md) | The value associated with the key. | [optional] 

## Example

```python
from docspace_api_sdk.models.item_key_value_pair_string_logo_requests_dto import ItemKeyValuePairStringLogoRequestsDto

# TODO update the JSON string below
json = "{}"
# create an instance of ItemKeyValuePairStringLogoRequestsDto from a JSON string
item_key_value_pair_string_logo_requests_dto_instance = ItemKeyValuePairStringLogoRequestsDto.from_json(json)
# print the JSON string representation of the object
print(ItemKeyValuePairStringLogoRequestsDto.to_json())

# convert the object into a dict
item_key_value_pair_string_logo_requests_dto_dict = item_key_value_pair_string_logo_requests_dto_instance.to_dict()
# create an instance of ItemKeyValuePairStringLogoRequestsDto from a dict
item_key_value_pair_string_logo_requests_dto_from_dict = ItemKeyValuePairStringLogoRequestsDto.from_dict(item_key_value_pair_string_logo_requests_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


