# AiThreadsTouchRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** |  | 
**profile_id** | **str** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_threads_touch_request import AiThreadsTouchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiThreadsTouchRequest from a JSON string
ai_threads_touch_request_instance = AiThreadsTouchRequest.from_json(json)
# print the JSON string representation of the object
print(AiThreadsTouchRequest.to_json())

# convert the object into a dict
ai_threads_touch_request_dict = ai_threads_touch_request_instance.to_dict()
# create an instance of AiThreadsTouchRequest from a dict
ai_threads_touch_request_from_dict = AiThreadsTouchRequest.from_dict(ai_threads_touch_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


