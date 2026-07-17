# WalletServiceArrayWrapper

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**List[WalletServiceDto]**](WalletServiceDto.md) |  | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.wallet_service_array_wrapper import WalletServiceArrayWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of WalletServiceArrayWrapper from a JSON string
wallet_service_array_wrapper_instance = WalletServiceArrayWrapper.from_json(json)
# print the JSON string representation of the object
print(WalletServiceArrayWrapper.to_json())

# convert the object into a dict
wallet_service_array_wrapper_dict = wallet_service_array_wrapper_instance.to_dict()
# create an instance of WalletServiceArrayWrapper from a dict
wallet_service_array_wrapper_from_dict = WalletServiceArrayWrapper.from_dict(wallet_service_array_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


