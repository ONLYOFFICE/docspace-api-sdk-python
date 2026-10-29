# AiMetaGenerate200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fields** | [**List[AiMetaGenerate200ResponseFieldsInner]**](AiMetaGenerate200ResponseFieldsInner.md) | The proposed custom metadata fields with the values the text supports. | 
**sources** | [**List[AiMetaGenerate200ResponseSourcesInner]**](AiMetaGenerate200ResponseSourcesInner.md) | The documents the proposal was read from. | 
**skipped** | [**List[AiMetaGenerate200ResponseSkippedInner]**](AiMetaGenerate200ResponseSkippedInner.md) | The entries that were left out, with the reason for each. | 

## Example

```python
from docspace_api_sdk.models.ai_meta_generate200_response import AiMetaGenerate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaGenerate200Response from a JSON string
ai_meta_generate200_response_instance = AiMetaGenerate200Response.from_json(json)
# print the JSON string representation of the object
print(AiMetaGenerate200Response.to_json())

# convert the object into a dict
ai_meta_generate200_response_dict = ai_meta_generate200_response_instance.to_dict()
# create an instance of AiMetaGenerate200Response from a dict
ai_meta_generate200_response_from_dict = AiMetaGenerate200Response.from_dict(ai_meta_generate200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


