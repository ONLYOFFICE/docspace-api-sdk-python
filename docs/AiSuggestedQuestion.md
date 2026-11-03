# AiSuggestedQuestion
A starter question proposed for an attached form.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**question** | **str** | The question as it is shown to the user. | 
**prompt** | **str** | The prompt sent to the chat when the user picks the question. | 

## Example

```python
from docspace_api_sdk.models.ai_suggested_question import AiSuggestedQuestion

# TODO update the JSON string below
json = "{}"
# create an instance of AiSuggestedQuestion from a JSON string
ai_suggested_question_instance = AiSuggestedQuestion.from_json(json)
# print the JSON string representation of the object
print(AiSuggestedQuestion.to_json())

# convert the object into a dict
ai_suggested_question_dict = ai_suggested_question_instance.to_dict()
# create an instance of AiSuggestedQuestion from a dict
ai_suggested_question_from_dict = AiSuggestedQuestion.from_dict(ai_suggested_question_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


