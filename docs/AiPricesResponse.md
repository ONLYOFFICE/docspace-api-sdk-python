# AiPricesResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**chat** | [**List[AiChatModelPricing]**](AiChatModelPricing.md) |  | 
**embedding** | [**List[AiEmbeddingModelPricing]**](AiEmbeddingModelPricing.md) |  | 
**image** | [**List[AiImageModelPricing]**](AiImageModelPricing.md) |  | 
**search** | [**List[AiWebSearchPricing]**](AiWebSearchPricing.md) |  | 
**currency** | [**CurrencyInfo**](CurrencyInfo.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_prices_response import AiPricesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AiPricesResponse from a JSON string
ai_prices_response_instance = AiPricesResponse.from_json(json)
# print the JSON string representation of the object
print(AiPricesResponse.to_json())

# convert the object into a dict
ai_prices_response_dict = ai_prices_response_instance.to_dict()
# create an instance of AiPricesResponse from a dict
ai_prices_response_from_dict = AiPricesResponse.from_dict(ai_prices_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


