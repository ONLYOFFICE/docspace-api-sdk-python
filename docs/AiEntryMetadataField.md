# AiEntryMetadataField

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**name** | **str** |  | 
**type** | **float** | `MetadataFieldType`: 0 String, 1 Date, 2 Number, 3 SingleChoice, 4 MultiChoice. | 
**options** | [**List[AiEntryMetadataFieldOptionsInner]**](AiEntryMetadataFieldOptionsInner.md) |  | 
**value** | [**AiMetadataValue**](AiMetadataValue.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_entry_metadata_field import AiEntryMetadataField

# TODO update the JSON string below
json = "{}"
# create an instance of AiEntryMetadataField from a JSON string
ai_entry_metadata_field_instance = AiEntryMetadataField.from_json(json)
# print the JSON string representation of the object
print(AiEntryMetadataField.to_json())

# convert the object into a dict
ai_entry_metadata_field_dict = ai_entry_metadata_field_instance.to_dict()
# create an instance of AiEntryMetadataField from a dict
ai_entry_metadata_field_from_dict = AiEntryMetadataField.from_dict(ai_entry_metadata_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


