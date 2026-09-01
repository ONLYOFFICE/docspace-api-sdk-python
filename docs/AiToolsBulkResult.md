# AiToolsBulkResult
Outcome of  {@link  ToolsEngine.replaceAllCustomServers }  — either every entry persisted, or no entries persisted plus a per-key error report.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**errors** | [**List[AiToolsBulkResultErrorsInner]**](AiToolsBulkResultErrorsInner.md) |  | [optional] 

## Example

```python
from docspace_api_sdk.models.ai_tools_bulk_result import AiToolsBulkResult

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsBulkResult from a JSON string
ai_tools_bulk_result_instance = AiToolsBulkResult.from_json(json)
# print the JSON string representation of the object
print(AiToolsBulkResult.to_json())

# convert the object into a dict
ai_tools_bulk_result_dict = ai_tools_bulk_result_instance.to_dict()
# create an instance of AiToolsBulkResult from a dict
ai_tools_bulk_result_from_dict = AiToolsBulkResult.from_dict(ai_tools_bulk_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


