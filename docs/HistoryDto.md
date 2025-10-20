# HistoryDto
The file history information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | [**HistoryAction**](HistoryAction.md) |  | 
**initiator** | [**EmployeeDto**](EmployeeDto.md) |  | 
**var_date** | [**ApiDateTime**](ApiDateTime.md) |  | 
**data** | [**HistoryData**](HistoryData.md) |  | 
**related** | [**List[HistoryDto]**](HistoryDto.md) | The list of related history. | [optional] 

## Example

```python
from docspace_api_sdk.models.history_dto import HistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryDto from a JSON string
history_dto_instance = HistoryDto.from_json(json)
# print the JSON string representation of the object
print(HistoryDto.to_json())

# convert the object into a dict
history_dto_dict = history_dto_instance.to_dict()
# create an instance of HistoryDto from a dict
history_dto_from_dict = HistoryDto.from_dict(history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


