# BalanceWrapper
The successful API response containing the Balance object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**Balance**](Balance.md) | The Balance object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.balance_wrapper import BalanceWrapper

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


