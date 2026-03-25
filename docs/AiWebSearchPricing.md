# AiWebSearchPricing

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | **str** |  | [optional] 
**search** | **float** |  | [optional] 
**contents** | **float** |  | [optional] 

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


