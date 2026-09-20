# AiEditorToolsList200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tools** | [**List[AiEditorToolsList200ResponseToolsInner]**](AiEditorToolsList200ResponseToolsInner.md) | The tools the editor may offer, flattened across every server. | 

## Example

```python
from docspace_api_sdk.models.ai_editor_tools_list200_response import AiEditorToolsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiEditorToolsList200Response from a JSON string
ai_editor_tools_list200_response_instance = AiEditorToolsList200Response.from_json(json)
# print the JSON string representation of the object
print(AiEditorToolsList200Response.to_json())

# convert the object into a dict
ai_editor_tools_list200_response_dict = ai_editor_tools_list200_response_instance.to_dict()
# create an instance of AiEditorToolsList200Response from a dict
ai_editor_tools_list200_response_from_dict = AiEditorToolsList200Response.from_dict(ai_editor_tools_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


