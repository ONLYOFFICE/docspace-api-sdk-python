# ToolDecisionRequestBody
Parameters for the tool execution permission decision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**decision** | [**ToolExecutionDecision**](ToolExecutionDecision.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.tool_decision_request_body import ToolDecisionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ToolDecisionRequestBody from a JSON string
tool_decision_request_body_instance = ToolDecisionRequestBody.from_json(json)
# print the JSON string representation of the object
print(ToolDecisionRequestBody.to_json())

# convert the object into a dict
tool_decision_request_body_dict = tool_decision_request_body_instance.to_dict()
# create an instance of ToolDecisionRequestBody from a dict
tool_decision_request_body_from_dict = ToolDecisionRequestBody.from_dict(tool_decision_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


