# Balance
Represents a balance with an account number and a list of sub-accounts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **int** | The account number. | [optional] 
**sub_accounts** | [**List[SubAccount]**](SubAccount.md) | A list of sub-accounts. | [optional] 

## Example

```python
from docspace-api-sdk.models.balance import Balance

# TODO update the JSON string below
json = "{}"
# create an instance of Balance from a JSON string
balance_instance = Balance.from_json(json)
# print the JSON string representation of the object
print(Balance.to_json())

# convert the object into a dict
balance_dict = balance_instance.to_dict()
# create an instance of Balance from a dict
balance_from_dict = Balance.from_dict(balance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


