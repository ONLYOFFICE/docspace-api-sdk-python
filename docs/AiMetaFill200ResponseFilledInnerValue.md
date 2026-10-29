# AiMetaFill200ResponseFilledInnerValue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**string_value** | **str** |  | [optional] 
**number_value** | **float** |  | [optional] 
**date_value** | **str** | ISO 8601 date-time, UTC midnight of the date. | [optional] 
**option_ids** | **List[str]** |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_meta_fill200_response_filled_inner_value import AiMetaFill200ResponseFilledInnerValue

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaFill200ResponseFilledInnerValue from a JSON string
ai_meta_fill200_response_filled_inner_value_instance = AiMetaFill200ResponseFilledInnerValue.from_json(json)
# print the JSON string representation of the object
print(AiMetaFill200ResponseFilledInnerValue.to_json())

# convert the object into a dict
ai_meta_fill200_response_filled_inner_value_dict = ai_meta_fill200_response_filled_inner_value_instance.to_dict()
# create an instance of AiMetaFill200ResponseFilledInnerValue from a dict
ai_meta_fill200_response_filled_inner_value_from_dict = AiMetaFill200ResponseFilledInnerValue.from_dict(ai_meta_fill200_response_filled_inner_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


