# AiMCPItem
Descriptor for a tool exposed by an MCP server.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Tool name as registered on the MCP server (e.g. `web_search`, `insert_text`). | 
**description** | **str** | Human-readable description shown to the AI model and in the tools list UI. | 
**input_schema** | **object** | JSON Schema describing the tool's input parameters. | 
**enabled** | **bool** | Whether this tool is currently enabled. Disabled tools are hidden from the AI model. | [optional] 
**server_type** | **str** | Server type (MCP server name / host tool group id) this tool belongs to — the key the persisted disabled map is stored under. Set by the source that enumerated the tool, so a caller-supplied tool can still be attributed to its group after being flattened into a single list: that is what lets the engine apply the disabled map to `actionArgs.tools` instead of trusting the caller to pre-filter. Wire-serializable, so it survives a remote (server-side) engine. | [optional] 
**require_approval** | **bool** | Whether the consumer must show an approval dialog before this tool runs. Feeds the `autoAllow` flag on a `tool-call-pending` event together with the user's tool permission mode: `false` skips the dialog under the auto mode, the default (under ask only the persisted always-allow list does), `true` and `undefined` defer to that list; allow skips it for every tool. Host tools set it and default to `false`; MCP / custom-server tools leave it unset. Wire-serializable, so it survives a remote (server-side) engine. | [optional] 
**annotations** | [**AiToolAnnotations**](AiToolAnnotations.md) | The MCP tool annotations as the server declared them in `tools/list` (kept verbatim on the descriptor; never sent to the model). The approval flow reads two of them under the auto permission mode: `readOnlyHint: true` and `destructiveHint: false` run without the dialog, a destructive or unannotated tool keeps asking — see `resolveAutoAllow`. Wire-serializable. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_mcp_item import AiMCPItem

# TODO update the JSON string below
json = "{}"
# create an instance of AiMCPItem from a JSON string
ai_mcp_item_instance = AiMCPItem.from_json(json)
# print the JSON string representation of the object
print(AiMCPItem.to_json())

# convert the object into a dict
ai_mcp_item_dict = ai_mcp_item_instance.to_dict()
# create an instance of AiMCPItem from a dict
ai_mcp_item_from_dict = AiMCPItem.from_dict(ai_mcp_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


