# AiChatPrice
The price of a chat model, per token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **float** | The price of a single prompt token. | [optional] 
**completion** | **float** | The price of a single completion token. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_chat_price import AiChatPrice

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatPrice from a JSON string
ai_chat_price_instance = AiChatPrice.from_json(json)
# print the JSON string representation of the object
print(AiChatPrice.to_json())

# convert the object into a dict
ai_chat_price_dict = ai_chat_price_instance.to_dict()
# create an instance of AiChatPrice from a dict
ai_chat_price_from_dict = AiChatPrice.from_dict(ai_chat_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


