# AiSendCustomRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_stream** | **bool** | Stream the reply (ndjson) when true, else return a single message. | 
**system_prompt** | **str** | Caller-supplied system prompt for this one-turn call. | 
**user_message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) |  | 
**action_args** | [**AiActionArgs**](AiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_send_custom_request import AiSendCustomRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiSendCustomRequest from a JSON string
ai_send_custom_request_instance = AiSendCustomRequest.from_json(json)
# print the JSON string representation of the object
print(AiSendCustomRequest.to_json())

# convert the object into a dict
ai_send_custom_request_dict = ai_send_custom_request_instance.to_dict()
# create an instance of AiSendCustomRequest from a dict
ai_send_custom_request_from_dict = AiSendCustomRequest.from_dict(ai_send_custom_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


