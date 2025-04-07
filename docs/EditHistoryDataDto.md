# EditHistoryDataDto


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes_url** | **str** | URL to the file changes | [optional] 
**key** | **str** | Key | [optional] 
**previous** | [**EditHistoryUrl**](EditHistoryUrl.md) |  | [optional] 
**token** | **str** | Token | [optional] 
**url** | **str** | File URL | [optional] 
**version** | **int** | File version | [optional] 
**file_type** | **str** | File type | [optional] 

## Example

```python
from docspace.models.edit_history_data_dto import EditHistoryDataDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryDataDto from a JSON string
edit_history_data_dto_instance = EditHistoryDataDto.from_json(json)
# print the JSON string representation of the object
print(EditHistoryDataDto.to_json())

# convert the object into a dict
edit_history_data_dto_dict = edit_history_data_dto_instance.to_dict()
# create an instance of EditHistoryDataDto from a dict
edit_history_data_dto_from_dict = EditHistoryDataDto.from_dict(edit_history_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


