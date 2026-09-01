# AiTMCPItem
Descriptor for a tool exposed by an MCP server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tool name as registered on the MCP server (e.g. `web_search`, `insert_text`). | 
**description** | **str** | Human-readable description shown to the AI model and in the tools list UI. | 
**input_schema** | **object** | JSON Schema describing the tool's input parameters. | 
**enabled** | **bool** | Whether this tool is currently enabled. Disabled tools are hidden from the AI model. | [optional] 
**server_type** | **str** | Server type (MCP server name / host tool group id) this tool belongs to — the key the persisted disabled map is stored under. Set by the source that enumerated the tool, so a caller-supplied tool can still be attributed to its group after being flattened into a single list: that is what lets the engine apply the disabled map to `actionArgs.tools` instead of trusting the caller to pre-filter. Wire-serializable, so it survives a remote (server-side) engine. | [optional] 
**require_approval** | **bool** | Whether the consumer must show an approval dialog before this tool runs. The engine reads it when deciding the `autoAllow` flag on a `tool-call-pending` event: `requireApproval === false` auto-allows the call (no dialog), `true` always prompts. `undefined` leaves the decision to the persisted always-allow list alone — so MCP / custom-server tools (which never set it) keep prompting as before, while host tools opt into auto-allow by default. Wire-serializable, so it survives a remote (server-side) engine. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tmcp_item import AiTMCPItem

# TODO update the JSON string below
json = "{}"
# create an instance of AiTMCPItem from a JSON string
ai_tmcp_item_instance = AiTMCPItem.from_json(json)
# print the JSON string representation of the object
print(AiTMCPItem.to_json())

# convert the object into a dict
ai_tmcp_item_dict = ai_tmcp_item_instance.to_dict()
# create an instance of AiTMCPItem from a dict
ai_tmcp_item_from_dict = AiTMCPItem.from_dict(ai_tmcp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


