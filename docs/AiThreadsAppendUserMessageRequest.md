# AiThreadsAppendUserMessageRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** |  | 
**message** | [**AiThreadMessageLike**](AiThreadMessageLike.md) | Message to persist (id/createdAt are storage-assigned). | 
**profile_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_threads_append_user_message_request import AiThreadsAppendUserMessageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsAppendUserMessageRequest from a JSON string
ai_threads_append_user_message_request_instance = AiThreadsAppendUserMessageRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsAppendUserMessageRequest.to_json())

# convert the object into a dict
ai_threads_append_user_message_request_dict = ai_threads_append_user_message_request_instance.to_dict()
# create an instance of AiThreadsAppendUserMessageRequest from a dict
ai_threads_append_user_message_request_from_dict = AiThreadsAppendUserMessageRequest.from_dict(ai_threads_append_user_message_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


