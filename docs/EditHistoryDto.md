# EditHistoryDto
The file editing history parameters.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The document ID. | [optional] 
**key** | **str** | The document identifier used to unambiguously identify the document file. | [optional] 
**version** | **int** | The document version number. | [optional] 
**version_group** | **int** | The document version group. | [optional] 
**user** | [**EditHistoryAuthor**](EditHistoryAuthor.md) |  | [optional] 
**created** | [**ApiDateTime**](ApiDateTime.md) |  | [optional] 
**changes_history** | **str** | The file history changes in the string format. | [optional] 
**changes** | [**List[EditHistoryChangesWrapper]**](EditHistoryChangesWrapper.md) | The list of file history changes. | [optional] 
**server_version** | **str** | The current server version number. | [optional] 

## Example

```python
from docspace_api_sdk.models.edit_history_dto import EditHistoryDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryDto from a JSON string
edit_history_dto_instance = EditHistoryDto.from_json(json)
# print the JSON string representation of the object
print(EditHistoryDto.to_json())

# convert the object into a dict
edit_history_dto_dict = edit_history_dto_instance.to_dict()
# create an instance of EditHistoryDto from a dict
edit_history_dto_from_dict = EditHistoryDto.from_dict(edit_history_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


