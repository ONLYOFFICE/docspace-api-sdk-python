# AiMetaGenerate200ResponseFieldsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Field name, at most 255 characters. | 
**value** | **str** | The value found in the documents, or null when the text does not state one. | 

## Example

```python
from docspace_api_sdk.models.ai_meta_generate200_response_fields_inner import AiMetaGenerate200ResponseFieldsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaGenerate200ResponseFieldsInner from a JSON string
ai_meta_generate200_response_fields_inner_instance = AiMetaGenerate200ResponseFieldsInner.from_json(json)
# print the JSON string representation of the object
print(AiMetaGenerate200ResponseFieldsInner.to_json())

# convert the object into a dict
ai_meta_generate200_response_fields_inner_dict = ai_meta_generate200_response_fields_inner_instance.to_dict()
# create an instance of AiMetaGenerate200ResponseFieldsInner from a dict
ai_meta_generate200_response_fields_inner_from_dict = AiMetaGenerate200ResponseFieldsInner.from_dict(ai_meta_generate200_response_fields_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


