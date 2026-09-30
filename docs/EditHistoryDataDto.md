# EditHistoryDataDto
Everything an editor needs in order to show what one revision of a file changed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes_url** | **str** | The address the editor downloads the recorded changes of this revision from. It is filled in only when the  portal has a change record for the revision; without it the revision can be shown as a whole document but not  as a set of changes. | [optional] 
**key** | **str** | The document key of the revision being shown, which the editing service uses to identify it and to reuse the  copy it has cached. | 
**previous** | [**EditHistoryUrl**](EditHistoryUrl.md) | The revision this one is compared against. It arrives together with `changesUrl`, and when the revision shown  is the first one the file ever had, it points at the blank template the file was created from instead of at an  earlier revision. | [optional] 
**token** | **str** | The signature over the whole answer, as a JSON Web Token that the editing service verifies before it accepts  the addresses in it. Empty when the portal runs without a document-service secret. | [optional] 
**url** | **str** | The address the content of this revision is served from. It is meant for the editing service and carries its  own key, which is valid for a limited time. | 
**version** | **int** | Echoes the revision that was asked for, so it reports 0 when the request named no version and the current  revision was taken. | 
**file_type** | **str** | The format of the revision being shown, as an extension without the leading dot. | 

## Example

```python
from docspace_api_sdk.models.edit_history_data_dto import EditHistoryDataDto

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


