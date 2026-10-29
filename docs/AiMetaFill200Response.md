# AiMetaFill200Response

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dry_run** | **bool** | Whether the values were only proposed (`true`) or written as well. | 
**metadata** | [**AiEntryMetadata**](AiEntryMetadata.md) | The entry's metadata after the write (or as it stands, with `dryRun`), as `GET api/2.0/files/metadata/{kind}/{id}` returns it. | 
**filled** | [**List[AiMetaFill200ResponseFilledInner]**](AiMetaFill200ResponseFilledInner.md) | The values written, or proposed with `dryRun`: a typed value for a template field, a string for a custom field. | 
**unresolved** | [**List[AiMetaFill200ResponseUnresolvedInner]**](AiMetaFill200ResponseUnresolvedInner.md) | The fields left as they were, with the reason for each. | 
**sources** | [**List[AiMetaFill200ResponseSourcesInner]**](AiMetaFill200ResponseSourcesInner.md) | The documents the values were read from. | 
**skipped** | [**List[AiMetaGenerate200ResponseSkippedInner]**](AiMetaGenerate200ResponseSkippedInner.md) | The entries that were left out, with the reason for each. | 

## Example

```python
from docspace_api_sdk.models.ai_meta_fill200_response import AiMetaFill200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaFill200Response from a JSON string
ai_meta_fill200_response_instance = AiMetaFill200Response.from_json(json)
# print the JSON string representation of the object
print(AiMetaFill200Response.to_json())

# convert the object into a dict
ai_meta_fill200_response_dict = ai_meta_fill200_response_instance.to_dict()
# create an instance of AiMetaFill200Response from a dict
ai_meta_fill200_response_from_dict = AiMetaFill200Response.from_dict(ai_meta_fill200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


