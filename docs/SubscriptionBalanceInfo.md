# SubscriptionBalanceInfo
The information about the current subscription and its unused balance.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_cost** | **float** | The total cost of the current billing period (the sum across all subscription items). | [optional] 
**currency** | **str** | The three-character ISO 4217 currency symbol of the subscription. | [optional] 
**period_start** | **datetime** | The start of the current billing period. | [optional] 
**period_end** | **datetime** | The end of the current billing period. | [optional] 
**period_used_until** | **datetime** | The boundary of the used part of the period (the moment of the request). | [optional] 
**days_elapsed** | **int** | The number of days elapsed since the start of the period (inclusive). | [optional] 
**remaining_balance** | **float** | The unused balance of the subscription, in the subscription currency. | [optional] 
**remaining_balance_in_wallet_currency** | **float** | The unused balance of the subscription, converted to the wallet currency. | [optional] 
**wallet_currency** | **str** | The three-character ISO 4217 currency symbol of the wallet. | [optional] 

## Example

```python
from docspace_api_sdk.models.subscription_balance_info import SubscriptionBalanceInfo

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionBalanceInfo from a JSON string
subscription_balance_info_instance = SubscriptionBalanceInfo.from_json(json)
# print the JSON string representation of the object
print(SubscriptionBalanceInfo.to_json())

# convert the object into a dict
subscription_balance_info_dict = subscription_balance_info_instance.to_dict()
# create an instance of SubscriptionBalanceInfo from a dict
subscription_balance_info_from_dict = SubscriptionBalanceInfo.from_dict(subscription_balance_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


