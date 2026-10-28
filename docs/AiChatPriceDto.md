# AiChatPriceDto
What a chat model charges, split by the direction the tokens flow in.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt** | **float** | The cost of one million tokens sent to the model, which includes the conversation history resent with  every turn and not just the newest message. | [optional] 
**completion** | **float** | The cost of one million tokens the model writes back. It is normally the dearer of the two directions. | [optional] 
**prompt_cache_read** | **float** | The cost of one million prompt tokens served from the prompt cache. It is absent when the model does not  support prompt caching. | [optional] 
**prompt_cache_write** | **float** | The cost of one million prompt tokens written to the prompt cache with the default lifetime. It is absent  when the model does not support prompt caching. | [optional] 
**prompt_cache_write1_h** | **float** | The cost of one million prompt tokens written to the prompt cache with a one-hour lifetime. It is absent  when the model offers no such option. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_chat_price_dto import AiChatPriceDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatPriceDto from a JSON string
ai_chat_price_dto_instance = AiChatPriceDto.from_json(json)
# print the JSON string representation of the object
print(AiChatPriceDto.to_json())

# convert the object into a dict
ai_chat_price_dto_dict = ai_chat_price_dto_instance.to_dict()
# create an instance of AiChatPriceDto from a dict
ai_chat_price_dto_from_dict = AiChatPriceDto.from_dict(ai_chat_price_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


