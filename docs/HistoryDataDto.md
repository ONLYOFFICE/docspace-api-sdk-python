# HistoryDataDto
The history data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initiator_name** | **str** | The name of the action initiator. | [optional] [readonly] 

## Example

```python
from docspace_api_sdk.models.history_data_dto import HistoryDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of HistoryDataDto from a JSON string
history_data_dto_instance = HistoryDataDto.from_json(json)
# print the JSON string representation of the object
print(HistoryDataDto.to_json())

# convert the object into a dict
history_data_dto_dict = history_data_dto_instance.to_dict()
# create an instance of HistoryDataDto from a dict
history_data_dto_from_dict = HistoryDataDto.from_dict(history_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


