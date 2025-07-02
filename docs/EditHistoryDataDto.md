# EditHistoryDataDto
The file editing history data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes_url** | **str** | The URL address of the file with the document changes data. | [optional] 
**key** | **str** | The document identifier used to unambiguously identify the document file. | [optional] 
**previous** | [**EditHistoryUrl**](EditHistoryUrl.md) |  | [optional] 
**token** | **str** | The encrypted signature added to the parameter in the form of a token. | [optional] 
**url** | **str** | The URL address of the current document version. | [optional] 
**version** | **int** | The document version number. | [optional] 
**file_type** | **str** | The document extension. | [optional] 

## Example

```python
from docspace-api-python.models.edit_history_data_dto import EditHistoryDataDto

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


