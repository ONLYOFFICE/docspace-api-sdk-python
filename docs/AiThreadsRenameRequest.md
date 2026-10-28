# AiThreadsRenameRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** |  | 
**title** | **str** | New thread title. | 

## Example

```python
from docspace_api_sdk.models.ai_threads_rename_request import AiThreadsRenameRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsRenameRequest from a JSON string
ai_threads_rename_request_instance = AiThreadsRenameRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsRenameRequest.to_json())

# convert the object into a dict
ai_threads_rename_request_dict = ai_threads_rename_request_instance.to_dict()
# create an instance of AiThreadsRenameRequest from a dict
ai_threads_rename_request_from_dict = AiThreadsRenameRequest.from_dict(ai_threads_rename_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


