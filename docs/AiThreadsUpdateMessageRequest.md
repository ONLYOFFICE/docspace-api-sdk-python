# AiThreadsUpdateMessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message_id** | **str** |  | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | Replacement message content. | 

## Example

```python
from docspace_api_sdk.models.ai_threads_update_message_request import AiThreadsUpdateMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsUpdateMessageRequest from a JSON string
ai_threads_update_message_request_instance = AiThreadsUpdateMessageRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsUpdateMessageRequest.to_json())

# convert the object into a dict
ai_threads_update_message_request_dict = ai_threads_update_message_request_instance.to_dict()
# create an instance of AiThreadsUpdateMessageRequest from a dict
ai_threads_update_message_request_from_dict = AiThreadsUpdateMessageRequest.from_dict(ai_threads_update_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


