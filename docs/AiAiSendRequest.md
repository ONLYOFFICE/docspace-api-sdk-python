# AiAiSendRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**AiActionType**](AiActionType.md) | Which AI action to run — selects the assignment slot and action. | 
**user_message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | The user turn to send. | 
**action_args** | [**AiAiActionArgs**](AiAiActionArgs.md) |  | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_ai_send_request import AiAiSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiAiSendRequest from a JSON string
ai_ai_send_request_instance = AiAiSendRequest.from_json(json)
# print the JSON string representation of the object
print(AiAiSendRequest.to_json())

# convert the object into a dict
ai_ai_send_request_dict = ai_ai_send_request_instance.to_dict()
# create an instance of AiAiSendRequest from a dict
ai_ai_send_request_from_dict = AiAiSendRequest.from_dict(ai_ai_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


