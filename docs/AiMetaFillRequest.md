# AiMetaFillRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | The entry's table. Only `file` for now: a folder or a room answers 400. | 
**id** | [**AiMetaGenerateRequestId**](AiMetaGenerateRequestId.md) |  | 
**prompt** | **str** | What to pay attention to; a hint for the model. | [optional] 
**overwrite** | **bool** | Also replace the fields that already carry a value. Default false. | [optional] 
**dry_run** | **bool** | Resolve the values but write nothing; the caller writes what the user confirms. Default true: a write needs an explicit false. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_meta_fill_request import AiMetaFillRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AiMetaFillRequest from a JSON string
ai_meta_fill_request_instance = AiMetaFillRequest.from_json(json)
# print the JSON string representation of the object
print(AiMetaFillRequest.to_json())

# convert the object into a dict
ai_meta_fill_request_dict = ai_meta_fill_request_instance.to_dict()
# create an instance of AiMetaFillRequest from a dict
ai_meta_fill_request_from_dict = AiMetaFillRequest.from_dict(ai_meta_fill_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


