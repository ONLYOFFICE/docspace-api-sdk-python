# AiMetaGenerate200ResponseSourcesInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**title** | **str** |  | 
**truncated** | **bool** | Whether the document was cut to fit the model's budget. | 

## Example

```python
from docspace_api_sdk.models.ai_meta_generate200_response_sources_inner import AiMetaGenerate200ResponseSourcesInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaGenerate200ResponseSourcesInner from a JSON string
ai_meta_generate200_response_sources_inner_instance = AiMetaGenerate200ResponseSourcesInner.from_json(json)
# print the JSON string representation of the object
print(AiMetaGenerate200ResponseSourcesInner.to_json())

# convert the object into a dict
ai_meta_generate200_response_sources_inner_dict = ai_meta_generate200_response_sources_inner_instance.to_dict()
# create an instance of AiMetaGenerate200ResponseSourcesInner from a dict
ai_meta_generate200_response_sources_inner_from_dict = AiMetaGenerate200ResponseSourcesInner.from_dict(ai_meta_generate200_response_sources_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


