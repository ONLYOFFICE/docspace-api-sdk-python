# AiEntryMetadataTemplatesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**visible** | **bool** |  | 
**fields** | [**List[AiEntryMetadataField]**](AiEntryMetadataField.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_entry_metadata_templates_inner import AiEntryMetadataTemplatesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiEntryMetadataTemplatesInner from a JSON string
ai_entry_metadata_templates_inner_instance = AiEntryMetadataTemplatesInner.from_json(json)
# print the JSON string representation of the object
print(AiEntryMetadataTemplatesInner.to_json())

# convert the object into a dict
ai_entry_metadata_templates_inner_dict = ai_entry_metadata_templates_inner_instance.to_dict()
# create an instance of AiEntryMetadataTemplatesInner from a dict
ai_entry_metadata_templates_inner_from_dict = AiEntryMetadataTemplatesInner.from_dict(ai_entry_metadata_templates_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


