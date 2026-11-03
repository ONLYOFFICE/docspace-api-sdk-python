# AiImportResult
The outcome of a prompt bundle import: either every entry was stored, with counts, or none was and the errors are reported per entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the whole bundle was imported. | 
**imported** | [**AiImportResultImported**](AiImportResultImported.md) |  | [optional] 
**errors** | [**List[AiImportError]**](AiImportError.md) | What was rejected, per entry. Present on failure - and then nothing was imported. | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_import_result import AiImportResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiImportResult from a JSON string
ai_import_result_instance = AiImportResult.from_json(json)
# print the JSON string representation of the object
print(AiImportResult.to_json())

# convert the object into a dict
ai_import_result_dict = ai_import_result_instance.to_dict()
# create an instance of AiImportResult from a dict
ai_import_result_from_dict = AiImportResult.from_dict(ai_import_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


