# AiSettingsDto
The AI module settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**web_search_enabled** | **bool** | Indicates whether web search is enabled for AI chat sessions. | [optional] 
**web_search_need_reset** | **bool** | Indicates whether the web search API key needs to be reconfigured. | [optional] 
**vectorization_enabled** | **bool** | Indicates whether document vectorization is enabled. | [optional] 
**vectorization_need_reset** | **bool** | Indicates whether the embedding provider API key needs to be reconfigured. | [optional] 
**ai_ready** | **bool** | Indicates whether the AI subsystem is fully configured and operational. | [optional] 
**ai_ready_need_reset** | **bool** | Indicates whether the AI provider API key needs to be reconfigured. | [optional] 
**portal_mcp_server_id** | **UUID** | The unique identifier of the portal-level MCP server, if configured. | [optional] 
**embedding_model** | **str** | The name of the embedding model used for document vectorization. | 
**model_aliases** | **Dict[str, str]** | Mapping of model identifiers to human-readable aliases. | 
**knowledge_search_tool_name** | **str** | The tool name used by the AI assistant for knowledge base search. | 
**web_search_tool_name** | **str** | The tool name used by the AI assistant for web search. | 
**web_crawling_tool_name** | **str** | The tool name used by the AI assistant for web page crawling. | 
**generate_docx_tool_name** | **str** | The tool name used by the AI to launch docx creation in the editor. | 
**generate_form_tool_name** | **str** | The tool name used by the AI assistant to launch form creation in the editor. | 
**generate_presentation_tool_name** | **str** | The tool name used by the AI assistant to launch presentation creation in the editor. | 
**system_ai_enabled** | **bool** | Indicates whether the system-level AI provider is enabled. | [optional] 
**recommended_model_for_forms** | **str** | The identifier of the model recommended for form generation. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_settings_dto import AiSettingsDto

# TODO update the JSON string below
json = "{}"
# create an instance of AiSettingsDto from a JSON string
ai_settings_dto_instance = AiSettingsDto.from_json(json)
# print the JSON string representation of the object
print(AiSettingsDto.to_json())

# convert the object into a dict
ai_settings_dto_dict = ai_settings_dto_instance.to_dict()
# create an instance of AiSettingsDto from a dict
ai_settings_dto_from_dict = AiSettingsDto.from_dict(ai_settings_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


