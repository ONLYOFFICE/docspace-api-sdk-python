# AiImageModelPricing

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
from docspace_api_sdk.models.ai_image_model_pricing import AiImageModelPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AiImageModelPricing from a JSON string
ai_image_model_pricing_instance = AiImageModelPricing.from_json(json)
# print the JSON string representation of the object
print(AiImageModelPricing.to_json())

# convert the object into a dict
ai_image_model_pricing_dict = ai_image_model_pricing_instance.to_dict()
# create an instance of AiImageModelPricing from a dict
ai_image_model_pricing_from_dict = AiImageModelPricing.from_dict(ai_image_model_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


