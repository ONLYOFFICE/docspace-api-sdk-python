# AiMetadataValue
A metadata value: exactly one member, by the field's type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** |  | [optional] 
**number_value** | **float** |  | [optional] 
**date_value** | **str** | ISO 8601 date-time, UTC midnight of the date. | [optional] 
**option_ids** | **List[str]** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_metadata_value import AiMetadataValue

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetadataValue from a JSON string
ai_metadata_value_instance = AiMetadataValue.from_json(json)
# print the JSON string representation of the object
print(AiMetadataValue.to_json())

# convert the object into a dict
ai_metadata_value_dict = ai_metadata_value_instance.to_dict()
# create an instance of AiMetadataValue from a dict
ai_metadata_value_from_dict = AiMetadataValue.from_dict(ai_metadata_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


