# AiChatModelPricing
The pricing of a single chat model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The identifier of the model, as the provider expects it on the wire. | 
**alias** | **str** | The display name of the model. | [optional] 
**owned_by** | **str** | The owner of the model, as reported by the provider. | [optional] 
**provider** | **str** | The provider that serves the model. | [optional] 
**link** | **str** | The link to the pricing page of the model. | [optional] 
**price** | [**AiChatPrice**](AiChatPrice.md) | The price of a chat model, per token. | 

## Example

```python
from docspace_api_sdk.models.ai_chat_model_pricing import AiChatModelPricing

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatModelPricing from a JSON string
ai_chat_model_pricing_instance = AiChatModelPricing.from_json(json)
# print the JSON string representation of the object
print(AiChatModelPricing.to_json())

# convert the object into a dict
ai_chat_model_pricing_dict = ai_chat_model_pricing_instance.to_dict()
# create an instance of AiChatModelPricing from a dict
ai_chat_model_pricing_from_dict = AiChatModelPricing.from_dict(ai_chat_model_pricing_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


