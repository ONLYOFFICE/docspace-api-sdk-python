# EditorToolDecisionRequestBody
Parameters for an editor file-generation tool decision.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow** | **bool** | Whether the user approved creating the file. | [optional] 

## Example

```python
from docspace_api_sdk.models.editor_tool_decision_request_body import EditorToolDecisionRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of EditorToolDecisionRequestBody from a JSON string
editor_tool_decision_request_body_instance = EditorToolDecisionRequestBody.from_json(json)
# print the JSON string representation of the object
print(EditorToolDecisionRequestBody.to_json())

# convert the object into a dict
editor_tool_decision_request_body_dict = editor_tool_decision_request_body_instance.to_dict()
# create an instance of EditorToolDecisionRequestBody from a dict
editor_tool_decision_request_body_from_dict = EditorToolDecisionRequestBody.from_dict(editor_tool_decision_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


