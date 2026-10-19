# AiToolAnnotations
MCP tool annotations (`Tool.annotations` in the protocol). All hints are advisory and optional; the protocol's defaults are `readOnlyHint: false` and `destructiveHint: true`, which is why an unannotated tool is treated as one that may destroy state.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**read_only_hint** | **bool** |  | [optional] 
**destructive_hint** | **bool** |  | [optional] 
**idempotent_hint** | **bool** |  | [optional] 
**open_world_hint** | **bool** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tool_annotations import AiToolAnnotations

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolAnnotations from a JSON string
ai_tool_annotations_instance = AiToolAnnotations.from_json(json)
# print the JSON string representation of the object
print(AiToolAnnotations.to_json())

# convert the object into a dict
ai_tool_annotations_dict = ai_tool_annotations_instance.to_dict()
# create an instance of AiToolAnnotations from a dict
ai_tool_annotations_from_dict = AiToolAnnotations.from_dict(ai_tool_annotations_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


