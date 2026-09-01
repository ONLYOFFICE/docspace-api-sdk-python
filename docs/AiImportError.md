# AiImportError
Per-entry error reported by `PromptsEngine.importBundle`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kind** | **str** | `folder` or `prompt`, plus the offending name or id. | 
**ref** | **str** | The offending entry - its name or its id. | 
**error** | [**AiTErrorData**](AiTErrorData.md) | Why the entry was rejected. | 

## Example

```python
from docspace_api_sdk.models.ai_import_error import AiImportError

# TODO update the JSON string below
json = "{}"
# create an instance of AiImportError from a JSON string
ai_import_error_instance = AiImportError.from_json(json)
# print the JSON string representation of the object
print(AiImportError.to_json())

# convert the object into a dict
ai_import_error_dict = ai_import_error_instance.to_dict()
# create an instance of AiImportError from a dict
ai_import_error_from_dict = AiImportError.from_dict(ai_import_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


