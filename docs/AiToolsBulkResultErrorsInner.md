# AiToolsBulkResultErrorsInner

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**error** | [**AiTErrorData**](AiTErrorData.md) |  | 

## Example

```python
from docspace_api_sdk.models.ai_tools_bulk_result_errors_inner import AiToolsBulkResultErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of AiToolsBulkResultErrorsInner from a JSON string
ai_tools_bulk_result_errors_inner_instance = AiToolsBulkResultErrorsInner.from_json(json)
# print the JSON string representation of the object
print(AiToolsBulkResultErrorsInner.to_json())

# convert the object into a dict
ai_tools_bulk_result_errors_inner_dict = ai_tools_bulk_result_errors_inner_instance.to_dict()
# create an instance of AiToolsBulkResultErrorsInner from a dict
ai_tools_bulk_result_errors_inner_from_dict = AiToolsBulkResultErrorsInner.from_dict(ai_tools_bulk_result_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


