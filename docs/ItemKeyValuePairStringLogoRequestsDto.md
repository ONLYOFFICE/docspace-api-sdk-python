# ItemKeyValuePairStringLogoRequestsDto
One entry of a keyed collection, carried as an explicit pair of `key` and `value` fields instead of as a member  of a JSON object, so that the key is not restricted to a string and the entries keep the order they are sent in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The left half of the pair. Where the pair configures something, this is the identifier the value belongs to -  a setting name, a module id, a logo slot; where the pair reports the result of a call, this is the result  itself, such as the flag telling whether the call succeeded. Which of the two it is, and which keys are  accepted, is stated by the operation that sends or returns the pair. | [optional] 
**value** | [**LogoRequestsDto**](LogoRequestsDto.md) | The right half of the pair: what is assigned to the key next to it, or what is reported for it. Its meaning  and its accepted values follow from the key, so read them from the operation that sends or returns the pair. | [optional] 

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


