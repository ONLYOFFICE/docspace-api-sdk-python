# AiPricesWrapper
The successful API response containing the AiPricesDto object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response** | [**AiPricesDto**](AiPricesDto.md) | The AiPricesDto object returned by the operation. | [optional] 
**count** | **int** | The total number of items in the response | [optional] 
**links** | [**List[GetPortalPrices200ResponseLinksInner]**](GetPortalPrices200ResponseLinksInner.md) | List of links related to the response | [optional] 
**status** | **int** | HTTP status code of the response | [optional] 
**status_code** | **int** | HTTP status code of the response (duplicate of status) | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_prices_wrapper import AiPricesWrapper

# TODO update the JSON string below
json = "{}"
# create an instance of AiPricesWrapper from a JSON string
ai_prices_wrapper_instance = AiPricesWrapper.from_json(json)
# print the JSON string representation of the object
print(AiPricesWrapper.to_json())

# convert the object into a dict
ai_prices_wrapper_dict = ai_prices_wrapper_instance.to_dict()
# create an instance of AiPricesWrapper from a dict
ai_prices_wrapper_from_dict = AiPricesWrapper.from_dict(ai_prices_wrapper_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


