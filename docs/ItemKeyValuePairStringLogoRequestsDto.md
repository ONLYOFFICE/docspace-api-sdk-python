# ItemKeyValuePairStringLogoRequestsDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | [optional] 
**value** | [**LogoRequestsDto**](LogoRequestsDto.md) |  | [optional] 

## Example

```python
from docspace.models.item_key_value_pair_string_logo_requests_dto import ItemKeyValuePairStringLogoRequestsDto

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


