# AiSendRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action_type** | [**AiActionType**](AiActionType.md) | Which AI action to run — selects the assignment slot and action. | 
**user_message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | The user turn to send. | 
**action_args** | [**AiActionArgs**](AiActionArgs.md) | Per-request engine options: extra tools, reasoning, prompt override. | [optional] 
**entity_id** | **str** | Optional entity (room) scope for profile resolution. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_send_request import AiSendRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiSendRequest from a JSON string
ai_send_request_instance = AiSendRequest.from_json(json)
# print the JSON string representation of the object
print(AiSendRequest.to_json())

# convert the object into a dict
ai_send_request_dict = ai_send_request_instance.to_dict()
# create an instance of AiSendRequest from a dict
ai_send_request_from_dict = AiSendRequest.from_dict(ai_send_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


