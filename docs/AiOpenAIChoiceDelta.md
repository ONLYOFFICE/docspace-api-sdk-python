# AiOpenAIChoiceDelta

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**tool_calls** | [**List[AiOpenAIToolCallDelta]**](AiOpenAIToolCallDelta.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_open_ai_choice_delta import AiOpenAIChoiceDelta

# TODO update the JSON string below
json = "{}"
# create an instance of AiOpenAIChoiceDelta from a JSON string
ai_open_ai_choice_delta_instance = AiOpenAIChoiceDelta.from_json(json)
# print the JSON string representation of the object
print(AiOpenAIChoiceDelta.to_json())

# convert the object into a dict
ai_open_ai_choice_delta_dict = ai_open_ai_choice_delta_instance.to_dict()
# create an instance of AiOpenAIChoiceDelta from a dict
ai_open_ai_choice_delta_from_dict = AiOpenAIChoiceDelta.from_dict(ai_open_ai_choice_delta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


