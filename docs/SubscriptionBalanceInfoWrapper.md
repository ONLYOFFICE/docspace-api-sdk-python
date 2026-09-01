# SubscriptionBalanceInfoWrapper
The successful API response containing the SubscriptionBalanceInfo object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**SubscriptionBalanceInfo**](SubscriptionBalanceInfo.md) | The SubscriptionBalanceInfo object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.subscription_balance_info_wrapper import SubscriptionBalanceInfoWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionBalanceInfoWrapper from a JSON string
subscription_balance_info_wrapper_instance = SubscriptionBalanceInfoWrapper.from_json(json)
# print the JSON string representation of the object
print(SubscriptionBalanceInfoWrapper.to_json())

# convert the object into a dict
subscription_balance_info_wrapper_dict = subscription_balance_info_wrapper_instance.to_dict()
# create an instance of SubscriptionBalanceInfoWrapper from a dict
subscription_balance_info_wrapper_from_dict = SubscriptionBalanceInfoWrapper.from_dict(subscription_balance_info_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


