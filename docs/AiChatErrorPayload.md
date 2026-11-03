# AiChatErrorPayload
Why a round failed or stopped early, as the message status and the stream report it: a stable `code`, a message safe to show the user, and the cause when there is one.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **str** | Stable machine-readable code. One of a canonical set — `auth`, `model_not_found`, `rate_limit`, `timeout`, `network`, `bad_request`, `server`, `not_found`, `insufficient_funds`, `aborted`, `unknown` — or a provider-specific string when the SDK supplies one verbatim. | 
**message** | **str** | Human-readable, end-user-safe message. | 
**cause** | [**AiChatErrorPayload**](AiChatErrorPayload.md) | Optional nested cause, normalized through the same helper. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_chat_error_payload import AiChatErrorPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AiChatErrorPayload from a JSON string
ai_chat_error_payload_instance = AiChatErrorPayload.from_json(json)
# print the JSON string representation of the object
print(AiChatErrorPayload.to_json())

# convert the object into a dict
ai_chat_error_payload_dict = ai_chat_error_payload_instance.to_dict()
# create an instance of AiChatErrorPayload from a dict
ai_chat_error_payload_from_dict = AiChatErrorPayload.from_dict(ai_chat_error_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


