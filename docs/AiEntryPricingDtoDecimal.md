# AiEntryPricingDtoDecimal
One AI model or service on the price list: how to name it, who provides it, and what it costs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The model identifier to send to the AI operations. It is the value to branch on, while `alias` is for display  only. | 
**alias** | **str** | The model name as the vendor writes it, meant to be shown to a person rather than matched on. | 
**provider** | **str** | Who runs the model. Two entries can share a provider, and one provider's models can be priced quite  differently, so the price always belongs to the entry and never to the provider. | 
**image** | **str** | The absolute URL of the provider's icon, for rendering next to the entry. | 
**price** | **float** | What the entry costs, in the currency the answer names. Amounts per token are normalised per million  tokens, so they are not the price of a single call. | 
**link** | **str** | The provider's own page for the model, for a person to read the model's terms. It is empty when the  provider publishes none. | 

## Example

```python
from docspace_api_sdk.models.ai_entry_pricing_dto_decimal import AiEntryPricingDtoDecimal

# TODO update the JSON string below
json = "{}"
# create an instance of AiEntryPricingDtoDecimal from a JSON string
ai_entry_pricing_dto_decimal_instance = AiEntryPricingDtoDecimal.from_json(json)
# print the JSON string representation of the object
print(AiEntryPricingDtoDecimal.to_json())

# convert the object into a dict
ai_entry_pricing_dto_decimal_dict = ai_entry_pricing_dto_decimal_instance.to_dict()
# create an instance of AiEntryPricingDtoDecimal from a dict
ai_entry_pricing_dto_decimal_from_dict = AiEntryPricingDtoDecimal.from_dict(ai_entry_pricing_dto_decimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


