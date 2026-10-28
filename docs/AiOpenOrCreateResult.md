# AiOpenOrCreateResult
Resolved thread state returned by `ThreadsEngine.openOrCreate`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** | The thread that was opened, or the one just created. | 
**title** | **str** | Empty string for existing threads — the engine doesn't re-fetch. | 
**prior_messages** | [**List[AiThreadMessageLike]**](AiThreadMessageLike.md) | The messages already in the thread - empty for a thread that was just created. | 

## Example

```python
from docspace_api_sdk.models.ai_open_or_create_result import AiOpenOrCreateResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenOrCreateResult from a JSON string
ai_open_or_create_result_instance = AiOpenOrCreateResult.from_json(json)
# print the JSON string representation of the object
print(AiOpenOrCreateResult.to_json())

# convert the object into a dict
ai_open_or_create_result_dict = ai_open_or_create_result_instance.to_dict()
# create an instance of AiOpenOrCreateResult from a dict
ai_open_or_create_result_from_dict = AiOpenOrCreateResult.from_dict(ai_open_or_create_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


