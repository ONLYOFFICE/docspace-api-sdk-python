# AiAiSendCustomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_stream** | **bool** | Stream the reply (ndjson) when true, else return a single message. | 
**system_prompt** | **str** | Caller-supplied system prompt for this one-turn call. | 
**user_message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) |  | 
**action_args** | [**AiAiActionArgs**](AiAiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_send_custom_request import AiAiSendCustomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiSendCustomRequest from a JSON string
ai_ai_send_custom_request_instance = AiAiSendCustomRequest.from_json(json)
# print the JSON string representation of the object
print(AiAiSendCustomRequest.to_json())

# convert the object into a dict
ai_ai_send_custom_request_dict = ai_ai_send_custom_request_instance.to_dict()
# create an instance of AiAiSendCustomRequest from a dict
ai_ai_send_custom_request_from_dict = AiAiSendCustomRequest.from_dict(ai_ai_send_custom_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


