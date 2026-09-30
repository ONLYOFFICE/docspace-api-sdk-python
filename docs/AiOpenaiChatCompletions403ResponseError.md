# AiOpenaiChatCompletions403ResponseError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Human-readable description of the failure. | 
**type** | **str** | OpenAI error class, for example `invalid_request_error`. | 
**code** | **str** | Machine-readable code, when the provider supplies one. | [optional] 
**param** | **str** | The request parameter at fault, when the failure names one. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_openai_chat_completions403_response_error import AiOpenaiChatCompletions403ResponseError

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenaiChatCompletions403ResponseError from a JSON string
ai_openai_chat_completions403_response_error_instance = AiOpenaiChatCompletions403ResponseError.from_json(json)
# print the JSON string representation of the object
print(AiOpenaiChatCompletions403ResponseError.to_json())

# convert the object into a dict
ai_openai_chat_completions403_response_error_dict = ai_openai_chat_completions403_response_error_instance.to_dict()
# create an instance of AiOpenaiChatCompletions403ResponseError from a dict
ai_openai_chat_completions403_response_error_from_dict = AiOpenaiChatCompletions403ResponseError.from_dict(ai_openai_chat_completions403_response_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


