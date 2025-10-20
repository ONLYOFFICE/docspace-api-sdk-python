# SubAccount
Represents a sub-account with a specific currency and balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The three-character ISO 4217 currency symbol of the sub-account. | [optional] 
**amount** | **float** | The balance of the sub-account in the specified currency. | [optional] 

## Example

```python
from docspace_api_sdk.models.sub_account import SubAccount

# TODO update the JSON string below
json = "{}"
# create an instance of SubAccount from a JSON string
sub_account_instance = SubAccount.from_json(json)
# print the JSON string representation of the object
print(SubAccount.to_json())

# convert the object into a dict
sub_account_dict = sub_account_instance.to_dict()
# create an instance of SubAccount from a dict
sub_account_from_dict = SubAccount.from_dict(sub_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


