# AiThread
Chat conversation metadata. Represents a single chat session (thread).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | Unique thread identifier (UUID). | 
**title** | **str** | Optional thread title. Auto-generated from the first message if not set. | [optional] 
**last_edit_date** | **float** | Timestamp (ms since epoch) of the last message in this thread. Used for sorting. | [optional] 
**provider** | [**AiTProvider**](AiTProvider.md) | Provider configuration at the time of last message. Used for thread-level provider display. | [optional] 
**model** | [**AiModel**](AiModel.md) | Model info at the time of last message. | [optional] 
**profile_id** | **str** | ID of the profile used for this thread. Links to  {@link  Profile.id } . | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_thread import AiThread

# TODO update the JSON string below
json = "{}"
# create an instance of AiThread from a JSON string
ai_thread_instance = AiThread.from_json(json)
# print the JSON string representation of the object
print(AiThread.to_json())

# convert the object into a dict
ai_thread_dict = ai_thread_instance.to_dict()
# create an instance of AiThread from a dict
ai_thread_from_dict = AiThread.from_dict(ai_thread_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


