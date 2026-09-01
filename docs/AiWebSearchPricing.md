# AiWebSearchPricing
The pricing of a single web search provider, per request.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the web search provider. | [optional] 
**provider** | **str** | The provider that serves the web search requests. | [optional] 
**price** | **float** | The price of a single web search request. | [optional] 
**link** | **str** | The link to the pricing page of the provider. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_web_search_pricing import AiWebSearchPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AiWebSearchPricing from a JSON string
ai_web_search_pricing_instance = AiWebSearchPricing.from_json(json)
# print the JSON string representation of the object
print(AiWebSearchPricing.to_json())

# convert the object into a dict
ai_web_search_pricing_dict = ai_web_search_pricing_instance.to_dict()
# create an instance of AiWebSearchPricing from a dict
ai_web_search_pricing_from_dict = AiWebSearchPricing.from_dict(ai_web_search_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


