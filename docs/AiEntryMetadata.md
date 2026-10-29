# AiEntryMetadata

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[AiEntryMetadataTemplatesInner]**](AiEntryMetadataTemplatesInner.md) |  | 
**custom_fields** | [**List[AiEntryMetadataCustomFieldsInner]**](AiEntryMetadataCustomFieldsInner.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_entry_metadata import AiEntryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of AiEntryMetadata from a JSON string
ai_entry_metadata_instance = AiEntryMetadata.from_json(json)
# print the JSON string representation of the object
print(AiEntryMetadata.to_json())

# convert the object into a dict
ai_entry_metadata_dict = ai_entry_metadata_instance.to_dict()
# create an instance of AiEntryMetadata from a dict
ai_entry_metadata_from_dict = AiEntryMetadata.from_dict(ai_entry_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


