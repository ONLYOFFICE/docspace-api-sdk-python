# AiOpenAIStreamError
OpenAI streaming error envelope. When the upstream request fails mid-stream the OpenAI API emits a single `data:` line carrying an `error` object (no `choices`), then closes the stream — the official SDK turns this into a thrown `APIError`. Mirrors that shape so a host exposing an OpenAI-compatible endpoint stays wire-compatible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | [**AiOpenAIStreamErrorError**](AiOpenAIStreamErrorError.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_stream_error import AiOpenAIStreamError

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIStreamError from a JSON string
ai_open_ai_stream_error_instance = AiOpenAIStreamError.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIStreamError.to_json())

# convert the object into a dict
ai_open_ai_stream_error_dict = ai_open_ai_stream_error_instance.to_dict()
# create an instance of AiOpenAIStreamError from a dict
ai_open_ai_stream_error_from_dict = AiOpenAIStreamError.from_dict(ai_open_ai_stream_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


