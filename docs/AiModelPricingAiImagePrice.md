# AiModelPricingAiImagePrice

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**alias** | **str** |  | [optional] 
**owned_by** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**price** | [**AiImagePrice**](AiImagePrice.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_model_pricing_ai_image_price import AiModelPricingAiImagePrice

# TODO update the JSON string below
json = "{}"
# create an instance of AiModelPricingAiImagePrice from a JSON string
ai_model_pricing_ai_image_price_instance = AiModelPricingAiImagePrice.from_json(json)
# print the JSON string representation of the object
print(AiModelPricingAiImagePrice.to_json())

# convert the object into a dict
ai_model_pricing_ai_image_price_dict = ai_model_pricing_ai_image_price_instance.to_dict()
# create an instance of AiModelPricingAiImagePrice from a dict
ai_model_pricing_ai_image_price_from_dict = AiModelPricingAiImagePrice.from_dict(ai_model_pricing_ai_image_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


