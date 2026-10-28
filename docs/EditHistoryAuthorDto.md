# EditHistoryAuthorDto
The person a saved revision of a file, or one single change in it, is attributed to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The account the revision or the change is attributed to, as the editing service stored it. It is normally the  identifier of a portal account; the empty identifier stands for a change nobody could be named for. | 
**name** | **str** | The display name of that account as the portal spells it now, which need not be the name that was stored with  the revision. An account that cannot be resolved - one removed from the portal, or a change made through an  anonymous link - is reported as a guest. | [optional] 

## Example

```python
from docspace_api_sdk.models.edit_history_author_dto import EditHistoryAuthorDto

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryAuthorDto from a JSON string
edit_history_author_dto_instance = EditHistoryAuthorDto.from_json(json)
# print the JSON string representation of the object
print(EditHistoryAuthorDto.to_json())

# convert the object into a dict
edit_history_author_dto_dict = edit_history_author_dto_instance.to_dict()
# create an instance of EditHistoryAuthorDto from a dict
edit_history_author_dto_from_dict = EditHistoryAuthorDto.from_dict(edit_history_author_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


