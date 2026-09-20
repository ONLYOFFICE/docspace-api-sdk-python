# AiEditorToolsCall200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **str** | What the tool produced, as text. A structured result is JSON-encoded, and a tool that failed reports its error here rather than through a status code. | 

## Example

```python
from docspace_api_sdk.models.ai_editor_tools_call200_response import AiEditorToolsCall200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiEditorToolsCall200Response from a JSON string
ai_editor_tools_call200_response_instance = AiEditorToolsCall200Response.from_json(json)
# print the JSON string representation of the object
print(AiEditorToolsCall200Response.to_json())

# convert the object into a dict
ai_editor_tools_call200_response_dict = ai_editor_tools_call200_response_instance.to_dict()
# create an instance of AiEditorToolsCall200Response from a dict
ai_editor_tools_call200_response_from_dict = AiEditorToolsCall200Response.from_dict(ai_editor_tools_call200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


