# EditHistoryAuthor
The information about the file editing history author.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The author ID. | 
**name** | **str** | The author name. | [optional] 

## Example

```python
from docspace_api_sdk.models.edit_history_author import EditHistoryAuthor

# TODO update the JSON string below
json = "{}"
# create an instance of EditHistoryAuthor from a JSON string
edit_history_author_instance = EditHistoryAuthor.from_json(json)
# print the JSON string representation of the object
print(EditHistoryAuthor.to_json())

# convert the object into a dict
edit_history_author_dict = edit_history_author_instance.to_dict()
# create an instance of EditHistoryAuthor from a dict
edit_history_author_from_dict = EditHistoryAuthor.from_dict(edit_history_author_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


