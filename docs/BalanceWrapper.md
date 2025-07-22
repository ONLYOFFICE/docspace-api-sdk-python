# BalanceWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Balance**](Balance.md) |  | [optional] 
**count** | **int** |  | [optional] 
**links** | [**List[ActiveConnectionsWrapperLinksInner]**](ActiveConnectionsWrapperLinksInner.md) |  | [optional] 
**status** | **int** |  | [optional] 
**status_code** | **int** |  | [optional] 

## Example

```python
from docspace-api-sdk.models.balance_wrapper import BalanceWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of BalanceWrapper from a JSON string
balance_wrapper_instance = BalanceWrapper.from_json(json)
# print the JSON string representation of the object
print(BalanceWrapper.to_json())

# convert the object into a dict
balance_wrapper_dict = balance_wrapper_instance.to_dict()
# create an instance of BalanceWrapper from a dict
balance_wrapper_from_dict = BalanceWrapper.from_dict(balance_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


