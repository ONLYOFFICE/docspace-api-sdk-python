# AiMetaGenerateRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The entry's table. Only `file` for now: a folder or a room answers 400. | 
**id** | [**AiMetaGenerateRequestId**](AiMetaGenerateRequestId.md) |  | 
**prompt** | **str** | What kind of metadata fields the caller is interested in; a hint for the model. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_meta_generate_request import AiMetaGenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaGenerateRequest from a JSON string
ai_meta_generate_request_instance = AiMetaGenerateRequest.from_json(json)
# print the JSON string representation of the object
print(AiMetaGenerateRequest.to_json())

# convert the object into a dict
ai_meta_generate_request_dict = ai_meta_generate_request_instance.to_dict()
# create an instance of AiMetaGenerateRequest from a dict
ai_meta_generate_request_from_dict = AiMetaGenerateRequest.from_dict(ai_meta_generate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


