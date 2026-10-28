# SubAccountDto
A sub-account of the wallet: its currency and balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**amount** | **float** | The amount in the specified currency. | [optional] 

## Example

```python
from docspace_api_sdk.models.sub_account_dto import SubAccountDto

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccountDto from a JSON string
sub_account_dto_instance = SubAccountDto.from_json(json)
# print the JSON string representation of the object
print(SubAccountDto.to_json())

# convert the object into a dict
sub_account_dto_dict = sub_account_dto_instance.to_dict()
# create an instance of SubAccountDto from a dict
sub_account_dto_from_dict = SubAccountDto.from_dict(sub_account_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


