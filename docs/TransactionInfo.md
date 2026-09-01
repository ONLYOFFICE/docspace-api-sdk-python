# TransactionInfo
Represents information about the transaction applied to an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency** | **str** | The three-character ISO 4217 currency symbol. | [optional] 
**amount** | **float** | The amount in the specified currency. | [optional] 
**var_date** | **datetime** | The date and time when the credit transaction occurred. | [optional] 

## Example

```python
from docspace_api_sdk.models.transaction_info import TransactionInfo

# TODO update the JSON string below
json = "{}"
# create an instance of TransactionInfo from a JSON string
transaction_info_instance = TransactionInfo.from_json(json)
# print the JSON string representation of the object
print(TransactionInfo.to_json())

# convert the object into a dict
transaction_info_dict = transaction_info_instance.to_dict()
# create an instance of TransactionInfo from a dict
transaction_info_from_dict = TransactionInfo.from_dict(transaction_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


