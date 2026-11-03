# AiSuggestedQuestionsResult
The starter questions of an attached form, and whether they are ready.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | `ready` - the questions are there; `pending` - they are being generated and arrive over the socket, ask again later; `unavailable` - the attachment is not a form that can have any. | 
**questions** | [**List[AiSuggestedQuestion]**](AiSuggestedQuestion.md) | The questions; empty unless `status` is `ready`. | 

## Example

```python
from docspace_api_sdk.models.ai_suggested_questions_result import AiSuggestedQuestionsResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiSuggestedQuestionsResult from a JSON string
ai_suggested_questions_result_instance = AiSuggestedQuestionsResult.from_json(json)
# print the JSON string representation of the object
print(AiSuggestedQuestionsResult.to_json())

# convert the object into a dict
ai_suggested_questions_result_dict = ai_suggested_questions_result_instance.to_dict()
# create an instance of AiSuggestedQuestionsResult from a dict
ai_suggested_questions_result_from_dict = AiSuggestedQuestionsResult.from_dict(ai_suggested_questions_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


